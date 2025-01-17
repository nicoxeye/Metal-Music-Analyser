from .api_requests import get_band_info, get_top_album_image, get_top_album_name, get_similar_artists
import tkinter as tk
from tkinter import messagebox, PhotoImage, Label, Toplevel
import os
import requests
from PIL import Image, ImageTk
import io

def start_gui():
    def search_band():
        band_name = entry.get()

        if not band_name:
            messagebox.showwarning("Input Error", "Please enter a band name.")
            return
        
        band_info1 = get_band_info(band_name)
        album_image_url = get_top_album_image(band_name)
        album_name = get_top_album_name(band_name)
        similar_artists = get_similar_artists(band_name)


        if band_info1 and album_image_url and album_name:
            listeners_label.config(text=f"{band_info1['artist']['stats']['listeners']}")
            playcount_label.config(text=f"{band_info1['artist']['stats']['playcount']}")
            genre_label.config(text=f"{band_info1['artist']['tags']['tag'][0]['name']}")
            top_album_name_label.config(text=f"{album_name}")

            if similar_artists and 'similarartists' in similar_artists:
                artists = similar_artists['similarartists']['artist']
                similar1.config(text=f"{artists[0]['name']}")
                similar2.config(text=f"{artists[1]['name']}")
                similar3.config(text=f"{artists[2]['name']}")

            if album_image_url:
                try:
                    response = requests.get(album_image_url)
                    response.raise_for_status()
                    image_data = response.content
                    image = Image.open(io.BytesIO(image_data))
                    image = image.resize((205, 205))

                    photo = ImageTk.PhotoImage(image)
                
                    album_canvas.create_image(0, 0, anchor='nw', image=photo)
                    album_canvas.image = photo  #type: ignore
                except Exception:
                    album_canvas.create_text(100, 100, text="No image available", font="Calibri, 12")
            else:
                album_canvas.create_text(100, 100, text="No image available", font="Calibri, 12")
            
    def analyze():
        newWindow = Toplevel(window)

        newWindow.title("Analyzing Metal Bands")

        newWindow.geometry("400x200")

        Label(newWindow, 
          text ="This is a new window").pack()
        

    window = tk.Tk()

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "images", "bg2.png")

    bg = PhotoImage(file=image_path)
  
    label1 = Label(window, image = bg) 
    label1.place(x = 0, y = 0) 

    window_width = 1200
    window_height = 800
    window.geometry(f"{window_width}x{window_height}")
    window.resizable(False, False)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)

    window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    window.title("Metal Music Analyzer")

    entry = tk.Entry(window, font=("MS Gothic", 24))
    entry.place(x=65, y=235, anchor="w", width=400, height=50)

    search_button = tk.Button(window, text="Search", command=search_band)
    search_button.place(x=420, y=235, anchor="center")

    listeners_label = tk.Label(window, font=("MS Gothic", 24), bg="black", fg="white")
    listeners_label.place(x=220, y=320, anchor="w")

    playcount_label = tk.Label(window, font=("MS Gothic", 24), bg="black", fg="white")
    playcount_label.place(x=250, y=410, anchor="w")

    genre_label = tk.Label(window, font=("MS Gothic", 24), bg="black", fg="white")
    genre_label.place(x=180, y=500, anchor="w")

    album_canvas = tk.Canvas(window, width=200, height=200)
    album_canvas.place(x=860, y=280, anchor="center")

    top_album_name_label = tk.Label(window, font=("MS Gothic", 24), bg="black", fg="white")
    top_album_name_label.place(x=860, y=420, anchor="center")

    analyze_button = tk.Button(window, text="Analyze Bands", anchor="center", command=analyze)
    analyze_button.place(x=785, y=715, anchor="w")

    visualize_button = tk.Button(window, text="View Top Albums", anchor="center")
    visualize_button.place(x=785, y=475, anchor="w")

    similar1 = tk.Label(window, font=("MS Gothic", 20), bg="black", fg="white")
    similar1.place(x=75, y=625)

    similar2 = tk.Label(window, font=("MS Gothic", 20), bg="black", fg="white")
    similar2.place(x=75, y=675)

    similar3 = tk.Label(window, font=("MS Gothic", 20), bg="black", fg="white")
    similar3.place(x=75, y=725)

    window.mainloop()
