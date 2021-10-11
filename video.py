from flask_restful import Resource, reqparse, abort

video_args = reqparse.RequestParser()
video_args.add_argument('name', type=str, help="Name is required", required=False)
video_args.add_argument('age', type=int, help="Age is required", required=False)
video_args.add_argument('url', type=str, help="URL is required", required=False)

videos = {1: {"name": "ivan", "age": 15}, 2: {"name": "gosho", "age": 20}}


class VideoList(Resource):
    def get(self):
        return videos, 200

    def post(self):
        args = video_args.parse_args()
        video_id = len(videos) + 1
        videos[video_id] = args
        return args, 201


class Video(Resource):
    def get(self, video_id):
        _doesnt_exist_error(video_id)
        return videos[video_id]

    def put(self, video_id):
        _doesnt_exist_error(video_id)
        args = video_args.parse_args()
        videos[video_id] = args
        return "", 204

    def delete(self, video_id):
        _doesnt_exist_error(video_id)
        del videos[video_id]
        return "", 204


def _doesnt_exist_error(video_id):
    if video_id not in videos:
        return abort(404, message=f"This Video doesn't exist!")
