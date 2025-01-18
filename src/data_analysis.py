import pandas
from .api_requests import get_band_popularity

def load_bands_from_file(filename="bands.txt"):
    with open(filename, "r") as f:
        bands = f.readlines()
    bands = [band.strip() for band in bands]
    return bands

def analyse_bands_popularity(bands):
    band_data = []
    
    for band in bands:
        listeners, playcount = get_band_popularity(band)
        if listeners is not None and playcount is not None:
            band_data.append({
                'band': band,
                'listeners': listeners,
                'playcount': playcount
            })

    df = pandas.DataFrame(band_data)
    return df

def compare_bands(searched_band, df):
    band_data = df[df['band'] == searched_band].iloc[0]

    band_info = f"{searched_band} - Listeners: {band_data['listeners']}, Playcount: {band_data['playcount']}"

    df_sorted = df.sort_values(by='listeners', ascending = False).reset_index(drop=True)
    #print(df_sorted)

    band_rank = df_sorted[df_sorted['band'] == searched_band].index[0] + 1
    
    rank_info = f"{searched_band} is ranked {band_rank} out of {len(df_sorted)} bands based on listeners."

    return band_info, rank_info, df_sorted[['band', 'listeners']].head(5).to_string(index=False)

