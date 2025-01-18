# Metal Music Analyzer 🤘

A Python application that uses the Last.fm API to analyze metal music bands, their albums, and track popularity.

# IMPORTANT
### To include a metal band (or any band or artist) in analysis they have to be written in the bands.txt file.

## Features

- Fetches information about metal bands, albums, and tracks.
- Analyzes the most frequently played tracks(todo), where the band places on a ranking based on listeners and shows top 5 bands.
- Visualizes four bands that surround the band searched based on listeners using graphs.

## Setup Instructions

### Step 1: Get Your API Key

1. Go to [Last.fm API page](https://www.last.fm/api) and sign up for an account (if you don't already have one).
2. Create a new API application and get your **API Key**.

### Step 2: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/nicoxeye/Metal-Music-Analyzer.git
```

Create a `.env` file in the root of the project and add your key as follows:

API_KEY=your-api-key-here
