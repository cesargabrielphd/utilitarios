import yt_dlp

# URL da playlist
playlist_url = 'https://youtube.com/playlist?list=PLX-4skTGVrWUNh2VGFIyoWVGEVRQq3gkB&si=uCws3gRSujmWAHKd'

# Opções de configuração para o yt-dlp
ydl_opts = {
    'format': 'best',  # baixa a melhor qualidade disponível
    'outtmpl': '%(title)s.%(ext)s',  # salva os vídeos com o título como nome do arquivo
    'noplaylist': False,  # garante que toda a playlist será baixada
}

# Baixar a playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])