from bson.json_util import dumps
from flask import Flask, Response
from flask_cors import CORS
from flask_pymongo import PyMongo, ObjectId
from flask_restful import Api, Resource, reqparse, abort
from datetime import datetime

from utils import download_as_audio, upload_audio_to_s3, download_audio_from_s3, parse_to_json

app = Flask(__name__)

CORS(app)
api = Api(app)
mongo = PyMongo(app,
                uri="mongodb+srv://flask_mongo:flask_mongo@cluster0.xmsvz.mongodb.net/youtube_converter?retryWrites=true&w=majority")

video_collection = mongo.db.videos

video_args = reqparse.RequestParser()
video_args.add_argument('name', type=str, help="Name is required", required=True)
video_args.add_argument('userId', type=int, help="UserId is required", required=True)
video_args.add_argument('url', type=str, help="URL is required", required=True)

converter_args = reqparse.RequestParser()
converter_args.add_argument('url', type=str, help="Url is required", required=True)
converter_args.add_argument('userId', type=str, help="UserId is required", required=True)


class VideoList(Resource):
    def get(self):
        videos = video_collection.find()
        return Response(response=dumps(parse_to_json(videos)), status=200, mimetype='application/json')


class Video(Resource):
    def delete(self, video_id):
        video_collection.delete_one({"_id": ObjectId(video_id)})
        return Response(response="The video has been deleted!", status=204, mimetype='application/json')


class Converter(Resource):
    def post(self):
        args = converter_args.parse_args()
        file_id, file_name = download_as_audio(args['url'])
        is_uploaded = upload_audio_to_s3(f"{file_name}.mp3", f"{file_name}-{file_id}.mp3")
        if is_uploaded:
            args.update({'created_at': datetime.utcnow()})
            video_collection.insert_one(args)
            return Response(response=file_name, status=201)
        else:
            return Response(response=f"Failed to save the file", status=404)


api.add_resource(VideoList, "/video_list")
api.add_resource(Video, "/video/<string:video_id>")

api.add_resource(Converter, '/convert')

if __name__ == "__main__":
    app.run(debug=True)
