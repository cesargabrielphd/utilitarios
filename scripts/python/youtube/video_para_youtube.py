import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Diretório onde estão os vídeos
video_directory = './videos'
# Arquivo de credenciais OAuth 2.0
client_secrets_file = 'client_secret.json'

# Obtenha credenciais e crie um cliente da API
scopes = ["https://www.googleapis.com/auth/youtube.upload"]
api_service_name = "youtube"
api_version = "v3"

# Realiza a autenticação e cria o cliente da API
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

def upload_video(youtube, video_file):
    request_body = {
        'snippet': {
            'title': 'Título do Vídeo',
            'description': 'Descrição do Vídeo',
            'tags': ['tag1', 'tag2'],
            'categoryId': '22'  # Categoria de vídeos (22 é a ID para People & Blogs)
        },
        'status': {
            'privacyStatus': 'private'  # Define o status do vídeo (public, private ou unlisted)
        }
    }

    media_file = googleapiclient.http.MediaFileUpload(video_file)
    request = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media_file
    )
    response = request.execute()
    print(f'Upload do vídeo "{video_file}" concluído. ID do vídeo: {response["id"]}')

# Percorre todos os arquivos de vídeo no diretório e faz o upload
for video_file in os.listdir(video_directory):
    if video_file.endswith('.mp4'):  # Verifica se o arquivo é um vídeo MP4
        upload_video(youtube, os.path.join(video_directory, video_file))