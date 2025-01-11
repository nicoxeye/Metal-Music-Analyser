from src.api_requests import get_band_info
from dotenv import load_dotenv
import os
from src.gui import start_gui

def main():
    # FOR TESTING AND QUICK REVIEWS
    load_dotenv()
    api_key = os.getenv('API_KEY')

    if not api_key:
        print("Error: API key not found. Please set your API key in the .env file.")
        exit(1)

    #artist_name = input("Enter the name of the band: ")
    with open('src/bands.txt', 'r') as file:
        bands = [line.strip() for line in file]

        for artist_name in bands:
            band_info = get_band_info(artist_name, api_key)
            #print(band_info)
            #if band_info:
                #print(band_info['artist']['name'] + " - " + band_info['artist']['tags']['tag'][0]['name'])

if __name__ == "__main__":
    start_gui()
    #main()