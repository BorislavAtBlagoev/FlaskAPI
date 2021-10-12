import os

import boto3
from youtube_dl import YoutubeDL

BUCKET_NAME = "pytube-downloads"
YDL_OPTS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


def save_audio_to_s3(file_name, source):
    try:
        s3_client = boto3.client('s3')
        s3_client.upload_file(source, BUCKET_NAME, file_name)
        os.remove(source)
        return True
    except Exception as e:
        return False


def download_as_audio(url):
    with YoutubeDL(YDL_OPTS) as ydl:
        data = ydl.extract_info(url, download=False)
        ydl.download([url])

    return data['id'], data['title']
