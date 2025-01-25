# Metal Music Analyser

A Python application that uses the Last.fm API to analyse metal music bands; their tracks, albums, and popularity amongst other bands.

It can also be used as an overall artist analyser, since it works just fine with any artist given.

## Before Usage
> [!IMPORTANT]
> To include a metal band (or any band or artist) in analysis they have to be written in the bands.txt file.

## Features

- Fetches information about metal bands, albums, tracks, their biography, their genre and similar artists from LastFM API.
- Analyses most frequently played tracks, top albums, where the band places on a ranking based on listeners and playcount among bands in bands.txt.
- Visualizes the band's top five tracks.
- Visualizes four bands that surround the band searched based on their popularity using graphs.

## Setup Instructions

> [!IMPORTANT]
> Without these steps, this app will not work.

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
