from flask import Flask
from flask_restful import Api

from converter import Converter
from video import VideoList, Video

app = Flask(__name__)
api = Api(app)

api.add_resource(VideoList, "/video_list")
api.add_resource(Video, "/video/<int:video_id>")
api.add_resource(Converter, '/convert')

if __name__ == "__main__":
    app.run(debug=True)
