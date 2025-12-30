import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import pandas as pd

load_dotenv()

API_KEY = os.getenv('YOUTUBE_API_KEY')

if not API_KEY:
    raise ValueError("ERROR: Variable YOUTUBE_API_KEY not found. see if .env existis")

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_youtube_service():
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

def search_video(query, max_results=5):
    try:
        youtube = get_youtube_service()
        
        search_response = youtube.search().list(
            q=query,
            part='id,snippet',
            maxResults=max_results,
            type='video',
            videoCategoryId='10' # <-- Music filter
        ).execute()

        results = []

        for search_result in search_response.get('items', []):
            video_data = {
                'video_id': search_result['id']['videoId'],
                'title': search_result['snippet']['title'],
                'channel_title': search_result['snippet']['channelTitle'],
                'publish_time': search_result['snippet']['publishTime'],
                'description': search_result['snippet']['description']
            }
            results.append(video_data)
            
        return results

    except Exception as e:
        print(f"There is an error with the API: {e}")
        return []

if __name__ == "__main__":
    termo_busca = "Hello World"
    
    print(f"Usando chave segura do .env...")
    print(f"Buscando por: {termo_busca}...")
    
    dados = search_video(termo_busca)
    
    if dados:
        df = pd.DataFrame(dados)
        print("\n--- Results ---")
        print(df[['video_id', 'title', 'channel_title']])
        
    else:
        print("No data found")