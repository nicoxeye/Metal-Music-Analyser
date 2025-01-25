import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Toplevel

def visualize_band_popularity(searched_band, df, window):
    df_sorted = df.sort_values(by='listeners', ascending=False).reset_index(drop=True)
    
    band_index = df_sorted[df_sorted['band'] == searched_band].index[0]
    
    start_index = max(0, band_index - 2)
    end_index = min(len(df_sorted), band_index + 3)  
    surrounding_bands = df_sorted.iloc[start_index:end_index]
    
    band_names = surrounding_bands['band'].tolist()
    band_listeners = surrounding_bands['listeners'].tolist()

    figure, ax = plt.subplots(figsize=(8, 6))
    ax.bar(band_names, band_listeners, color=['black' if band != searched_band else 'aqua' for band in band_names])
    
    ax.set_title(f"Bands who have similar popularity to {searched_band}")
    ax.set_xlabel("Band")
    ax.set_ylabel("Listeners")

    pwindow = Toplevel(window)
    pwindow.title(f"Popularity Comparison - {searched_band}")
    pwindow.configure(background="black")
    pwindow.geometry("800x600")

    canvas = FigureCanvasTkAgg(figure, master=pwindow)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


def visualize_top_tracks(band_name, track_df, window):
    sorted_df = track_df.sort_values(by='playcount', ascending=False).reset_index(drop=True)

    track_names = sorted_df['track_name'].tolist()
    track_playcounts = sorted_df['playcount'].tolist()

    figure, ax = plt.subplots(figsize=(8, 6))

    ax.bar(track_names, track_playcounts, color="black")

    ax.set_title(f"{band_name}'s Top Tracks", fontsize=16)
    ax.set_xlabel("Track Name", fontsize=16)
    ax.set_ylabel("Playcount", fontsize=16)

    pwindow = Toplevel(window)
    pwindow.title(f"Top Tracks - {band_name}")
    pwindow.geometry("800x600")

    canvas = FigureCanvasTkAgg(figure, master=pwindow)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

