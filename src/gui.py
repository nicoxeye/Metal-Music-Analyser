from .api_requests import get_band_info, get_top_album_image, get_top_album_name, get_similar_artists, get_band_biography
from .data_analysis import analyse_bands_popularity, load_bands_from_file, compare_bands
from .plot_visualisation import visualize_band_popularity
import tkinter as tk
import customtkinter as Ctk
from tkinter import messagebox, PhotoImage, Label
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

    def biography():
        band_name = entry.get()

        content = get_band_biography(band_name)

        newWindow = Ctk.CTkToplevel(window)

        newWindow.configure(background="black")
        newWindow.title(f"{band_name} Biography")
        newWindow.geometry("600x800")

        label1 = Ctk.CTkLabel(newWindow, text="BIOGRAPHY", font=("MS PGothic", 20), fg_color="transparent")
        label1.pack(pady=(10, 5))

        textbox = Ctk.CTkTextbox(newWindow, height=800, corner_radius=50, scrollbar_button_color="white", width=600, font=("MS PGothic", 22), fg_color="#20262B")

        textbox.insert("0.0", content) 
        textbox.configure(state="disabled")  # read-only
        textbox.pack()
    

    def analyze():
        band_name = entry.get()
        newWindow = Ctk.CTkToplevel(window)

        newWindow.title("Analysing Metal Bands")

        newWindow.geometry("600x800")

        bands = load_bands_from_file("bands.txt")
        df = analyse_bands_popularity(bands)
                
        band_info, rank_info, rank_info_playcount, top_bands_info = compare_bands(band_name, df)

        label = Ctk.CTkLabel(newWindow, text=f"{band_name}", font=("MS PGothic", 28))
        label.pack(fill="both", padx=10, pady=10)

        band_label = Ctk.CTkLabel(newWindow, text="Band Info", font=("MS PGothic", 22))
        band_label.pack(fill="both", padx=10, pady=10)

        rank_label_listeners = Ctk.CTkLabel(newWindow, text="Rank Info Based On Listeners", font=("MS PGothic", 22))
        rank_label_listeners.pack(fill="both", padx=10, pady=10)

        rank_info_playcount_label = Ctk.CTkLabel(newWindow, text="Rank Info Based On Playcount", font=("MS PGothic", 22))
        rank_info_playcount_label.pack(fill="both", padx=10, pady=10)


        band_label.configure(text=band_info)
        rank_label_listeners.configure(text=rank_info)
        rank_info_playcount_label.configure(text=rank_info_playcount)

        textbox = Ctk.CTkTextbox(newWindow, height=800, corner_radius=50, scrollbar_button_color="white", width=600, font=("MS PGothic", 20), fg_color="#20262B")

        textbox.insert("1.0", "\n" + top_bands_info)
        textbox.insert("1.0", "RANKING BY LISTENERS\n")
        textbox.configure(state="disabled")  # read-only
        textbox.pack()


    def visualize_popularity():
        band_name = entry.get()
        bands = load_bands_from_file("bands.txt")

        df = analyse_bands_popularity(bands)

        visualize_band_popularity(band_name, df, window)

    window = Ctk.CTk()
    Ctk.set_default_color_theme("dark-blue")

    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "images", "bg.png")
    
    bg = PhotoImage(file=image_path)
    
    label1 = Label(window, image = bg) 
    label1.place(x = 0, y = 0, anchor="nw") 
    label1.configure(padx=0, pady=0)

    window_width = 1200
    window_height = 800
    window.geometry(f"{window_width}x{window_height}")
    window.resizable(False, False)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)

    window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    window.title("Metal Music Analyser")

    entry = tk.Entry(window, font=("MS PGothic", 24))
    entry.place(x=65, y=235, anchor="w", width=400, height=50)

    search_button = tk.Button(window, text="find", command=search_band, font=("MS PGothic", 12), bg="#20262B", fg="white")
    search_button.place(x=430, y=235, anchor="center")

    listeners_label = tk.Label(window, font=("MS PGothic", 24), bg="#20262B", fg="white")
    listeners_label.place(x=220, y=315, anchor="w")

    playcount_label = tk.Label(window, font=("MS PGothic", 24), bg="#20262B", fg="white")
    playcount_label.place(x=250, y=405, anchor="w")

    genre_label = tk.Label(window, font=("MS PGothic", 24), bg="#20262B", fg="white")
    genre_label.place(x=180, y=495, anchor="w")

    album_canvas = tk.Canvas(window, width=200, height=200)
    album_canvas.place(x=860, y=280, anchor="center")

    top_album_name_label = tk.Label(window, font=("MS PGothic", 24), bg="#20262B", fg="white")
    top_album_name_label.place(x=860, y=405, anchor="center")



    top_albums_button = tk.Button(window, text="Top Albums", anchor="center", bg="black", fg="white", font=("MS PGothic", 22), width=20)
    top_albums_button.place(x=700, y=495, anchor="w")

    top_tracks_button = tk.Button(window, text="Top Tracks", anchor="center", bg="black", fg="white", font=("MS PGothic", 22), width=20)
    top_tracks_button.place(x=700, y=560, anchor="w")

    biography_button = tk.Button(window, text="Biography", anchor="center", command=biography, bg="black", fg="white", font=("MS PGothic", 22), width=20)
    biography_button.place(x=700, y=625, anchor="w")

    visualize_button = tk.Button(window, text="Popularity Comparison", anchor="center", command=visualize_popularity, bg="black", fg="white", font=("MS PGothic", 22), width=20)
    visualize_button.place(x=700, y=690, anchor="w")

    analyze_button = tk.Button(window, text="Ranking", anchor="center", command=analyze, bg="black", fg="white", font=("MS PGothic", 22), width=20)
    analyze_button.place(x=700, y=755, anchor="w")



    similar1 = tk.Label(window, font=("MS PGothic", 20), bg="#20262B", fg="white")
    similar1.place(x=75, y=625)

    similar2 = tk.Label(window, font=("MS PGothic", 20), bg="#20262B", fg="white")
    similar2.place(x=75, y=675)

    similar3 = tk.Label(window, font=("MS PGothic", 20), bg="#20262B", fg="white")
    similar3.place(x=75, y=725)

    window.mainloop()
