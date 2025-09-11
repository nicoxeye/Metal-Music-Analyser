# Metal Music Analyser

A Python application that uses the Last.fm API to analyse metal music bands; their tracks, albums, and popularity amongst other bands.

It can also be used as an overall artist analyser, since it works just fine with any artist given.

## PREVIEW OF THE APP

<p align="center">
  <img src="https://github.com/user-attachments/assets/f6cccf3a-ede8-46d2-8a99-a2a7cc28eaaf" width="1000" />
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/c54997f7-1141-436a-8ef4-b3d16800d158" width="1000" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/d02f7093-96eb-46a4-a048-b75946c91422" width="300" />
  <img src="https://github.com/user-attachments/assets/fd86c558-cb22-4277-b61d-66663c7ba448" width="350" />
  <img src="https://github.com/user-attachments/assets/5990c58a-52e8-4a08-8302-fb5906b6d882" width="350" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/1c850283-8db8-461b-a76a-92c0fafe96bb" width="300" />
  <img src="https://github.com/user-attachments/assets/79b81466-a766-4f73-9520-b301545e0afc" width="300" />
</p>


## Before Usage
> [!IMPORTANT]
> To include a metal band (or any band or artist) in analysis they have to be written in the bands.txt file.

## Features

- Fetches information about metal bands, albums, tracks, their biography, their genre and similar artists from LastFM API.
- Analyses most frequently played tracks, top albums, where the band places on a ranking based on listeners and playcount amongst bands in bands.txt.
- Visualizes the band's top five tracks.
- Visualizes four bands that surround the band searched based on their popularity using graphs.

## Setup Instructions

### Step 1: Get Your API Key

1. Go to [Last.fm API page](https://www.last.fm/api) and sign up for an account (if you don't already have one).
2. Create a new API application and get your **API Key**.

### Step 2: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/nicoxeye/Metal-Music-Analyser.git
```

Create a `.env` file in the root of the project and add your key as follows:

API_KEY=your-api-key-here

> [!CAUTION]
> Never commit your API keys on GitHub.

### Step 3: Install needed packages

In your terminal:
```bash
pip install requirements.txt
```

Then run main.py and have fun :D
