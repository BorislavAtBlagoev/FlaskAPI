from flask_restful import Resource, reqparse, abort

from utils import download_as_audio, save_audio_to_s3, download_audio_from_s3

converter_args = reqparse.RequestParser()
converter_args.add_argument('url', type=str, help="Url is required", required=True)


class Converter(Resource):
    def post(self):
        args = converter_args.parse_args()
        file_id, file_name = download_as_audio(args['url'])
        is_saved = save_audio_to_s3(f"{file_name}.mp3", f"{file_name}-{file_id}.mp3")
        download_audio_from_s3(f"{file_name}.mp3")
        if is_saved:
            return file_name, 200
        else:
            return abort(404, message=f"Failed to save the file")
