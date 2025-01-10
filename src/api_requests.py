import requests

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
    
    