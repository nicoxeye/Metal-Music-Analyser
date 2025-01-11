from .api_requests import get_band_info1, get_track_info, get_band_info
import tkinter as tk
from tkinter import messagebox, PhotoImage, Label
import os
from dotenv import load_dotenv #delete

def start_gui():
    def search_band():
        band_name = entry.get()

        if not band_name:
            messagebox.showwarning("Input Error", "Please enter a band name.")
            return
        
        band_info1 = get_band_info1(band_name)
        track_info = get_track_info(band_name)

        #DELETE THIS
        load_dotenv()
        api_key = os.getenv('API_KEY')
        band_info = get_band_info(band_name, api_key)
        
        if band_info1 and track_info:
            band_label.config(text=f"Band: {band_info1['artist']['name']}")
            listeners_label.config(text=f"Listeners: {band_info1['artist']['stats']['listeners']}")
            playcount_label.config(text=f"Playcount: {band_info1['artist']['stats']['playcount']}")
            genre_label.config(text=f"Genre: {band_info['artist']['tags']['tag'][0]['name']}")
        else:
            messagebox.showerror("Error", "Failed to retrieve data.")

    window = tk.Tk()

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "images", "bg.png")

    bg = PhotoImage(file=image_path)
  
    label1 = Label(window, image = bg) 
    label1.place(x = 0, y = 0) 

    w = bg.width()
    h = bg.height()
  
    window.geometry(f"{w}x{h}")
    window.title("Metal Music Analyzer")

    info_label = tk.Label(window, text="See Info About A Band")
    info_label.grid(row=0, column=0, pady=5, padx=25)
    info_label.place(x=w/2, y=10, anchor="center")

    entry = tk.Entry(window)
    entry.grid(row=1, column=0)
    entry.place(x=w/2, y=30, anchor="center")

    search_button = tk.Button(window, text="Search", command=search_band)
    search_button.grid(row=2, column=0, pady=5, padx=5)
    search_button.place(x=w/2, y=60, anchor="center")

    band_label = tk.Label(window, text="Band: ")
    band_label.place(x=50, y=100, anchor="w")

    listeners_label = tk.Label(window, text="Listeners: ")
    listeners_label.place(x=50, y=150, anchor="w")

    playcount_label = tk.Label(window, text="Playcount: ")
    playcount_label.place(x=250, y=100, anchor="w")

    genre_label = tk.Label(window, text="Genre: ")
    genre_label.place(x=250, y=150, anchor="w")

    window.mainloop()
