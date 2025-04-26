import yt_dlp
import os

output_dir = os.path.join(os.getcwd(), "musicas")
os.makedirs(output_dir, exist_ok=True)

with open('urls.txt', 'r') as f:
    urls = [line.strip() for line in f if line.strip()]

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'), 
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '128',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)

print("✅ Downloads finalizados!")
