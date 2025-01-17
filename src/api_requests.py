import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def get_band_info(band_name):
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

def get_similar_artists(band_name):
    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist={band_name}&api_key={api_key}&format=json"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def get_top_album_image(band_name):
    params = {
        'method': 'artist.getTopAlbums',
        'artist': band_name,
        'api_key': api_key,
        'format': 'json',
        'limit': 1 
    }
    response = requests.get("http://ws.audioscrobbler.com/2.0/", params=params)
    
    if response.status_code == 200:
        data = response.json()
        if 'topalbums' in data and data['topalbums']['album']:
            album = data['topalbums']['album'][0]
            images = album['image']
            for img in images:
                if img['size'] == 'large':
                    return img['#text']
    return None

def get_top_album_name(band_name):
    album_info = get_album_info(band_name)
    if album_info and 'topalbums' in album_info and 'album' in album_info['topalbums']:
        first_album = album_info['topalbums']['album'][0]
        return first_album['name']
    return "No albums found"