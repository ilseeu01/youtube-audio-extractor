import yt_dlp

def download_audio_from_youtube(url, output_path="./"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# 사용 예시
if __name__ == "__main__":
    youtube_url = input("YouTube URL을 입력하세요: ")
    download_audio_from_youtube(youtube_url)