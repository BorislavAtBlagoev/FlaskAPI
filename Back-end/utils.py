import boto3
import json
import os
from bson.json_util import dumps, loads
from dotenv import load_dotenv
from youtube_dl import YoutubeDL

load_dotenv()

BUCKET_NAME = "pytube-downloads"
YDL_OPTS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

s3_client = boto3.client('s3', aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                         aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                         region_name=os.getenv("AWS_REGION_NAME"))


def upload_audio_to_s3(file_name, source):
    try:
        s3_client.upload_file(source, BUCKET_NAME, file_name)
        return True
    except Exception:
        return False
    finally:
        os.remove(source)


def download_audio_from_s3(file_name):
    s3_client.download_file(BUCKET_NAME, file_name, file_name)


def download_as_audio(url):
    with YoutubeDL(YDL_OPTS) as ydl:
        data = ydl.extract_info(url, download=False)
        ydl.download([url])

    return data['id'], data['title']


def transform_json(x):
    x['_id'] = x['_id']['$oid']
    x['created_at'] = x['created_at']['$date']

    return x


def parse_to_json(data):
    return list(map(transform_json, json.loads(dumps(data))))
