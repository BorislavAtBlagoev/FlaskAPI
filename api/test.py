# import youtube_dl
#
# ydl_opts = {
#     'format': 'bestaudio/best',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }],
# }
#
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(["https://www.youtube.com/watch?v=ZRqCwAJDZA0"])


import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')
for x in s3.buckets.all():
    print(x)

# s3.upload_file(local_file, bucket, s3_file)
s3_client = boto3.client('s3')

try:
    s3_client.upload_file("downloads/1.mp3", "pytube-downloads", "1.mp3")
except Exception as e:
    print(e)

s3_client.download_file('pytube-downloads', '1.mp3', '1.mp3')