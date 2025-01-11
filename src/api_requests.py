import requests
from dotenv import load_dotenv
import os

def get_band_info(artist_name, api_key):
    url = "http://ws.audioscrobbler.com/2.0/" #endpoint API Last.fm
    params = {
        "method": "artist.getinfo",
        "artist": artist_name,
        "api_key": api_key,
        "format": "json"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch data; status code {response.status_code}")
        return None
    
load_dotenv()
api_key = os.getenv('API_KEY')

def get_band_info1(band_name):
    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={band_name}&api_key={api_key}&format=json"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def get_album_info(band_name):
    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist={band_name}&api_key={api_key}&format=json"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def get_track_info(band_name):
    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={band_name}&api_key={api_key}&format=json"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None
