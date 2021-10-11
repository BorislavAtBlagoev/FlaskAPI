import shutil

from youtube_dl import YoutubeDL

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


def download_as_audio(url):
    with YoutubeDL(ydl_opts) as ydl:
        data = ydl.extract_info(url, download=False)
        ydl.download([url])

    song_name = f"{data['title']}"
    shutil.move(f"{song_name}-{data['id']}.mp3", f"./downloads/{song_name}.mp3")
    return song_name
