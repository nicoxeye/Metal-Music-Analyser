from src.api_requests import get_band_info
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    api_key = os.getenv('API_KEY')

    if not api_key:
        print("Error: API key not found. Please set your API key in the .env file.")
        exit(1)

    artist_name = input("Enter the name of the band: ")
    band_info = get_band_info(artist_name, api_key)

    if band_info:
        print(band_info)

if __name__ == "__main__":
    main()