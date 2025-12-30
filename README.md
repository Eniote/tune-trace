# Tune-trace: A Metadata Integration for Youtube & Spotify
This project aims to cross-reference and unify music track metadata from **YouTube** and **Spotify**.

While both platforms host similar content, their metadata schemas and available attributes differ significantly. The primary goal is to perform **Entity Resolution**—identifying that "Track A" on YouTube is the same as "Track B" on Spotify—to create a unified, enriched dataset.

The secondary objective is to perform an **Algorithmic Audit** on YouTube's recommendation engine: *Does YouTube recommend tracks that are sonically similar according to Spotify's acoustic metrics?*


## Problem Statement & Hypothesis
YouTube and Spotify operate as data silos. By integrating them, we aim to:
1.  Utilize graph analysis to find relationships between songs that aren't obvious when looking at a single platform isolatedly.
2.  Explore the pipeline of collecting (ETL), cleaning, and analyzing heterogeneous data sources.
3.  Answer the question: If a Track A recommends Track B on youtube, how similar are ther acoustic features (valance, tempo, energy) in Spotify's metrics?
4.  Visualize everythin in buitlfie graphics ^-^

## Tools
### Data colleciton
- `spotipy`: For accessing the Spotify Web API (Track features & metadata).
- ``google-api-python-client``: For accessing the YouTube Data API (Video search & recommendations).
### Data Engineering & Analysis
- `pandas`: For data manipulation, cleaning, and structuring the datasets.
- `networkx`: For modeling the recommendation data as a directed graph (Nodes = Songs, Edges = Recommendations).
- `scipy` / `numpy`: For calculating vector distances (similarity metrics).

### Visualization
- `matplotlib` / `seaborn`: For plotting statistical findings and graph topology.

## ToDos
- [ ] Define data models for "Track" and "Artist" to normalize API responses
- [ ] Implament authentication and basic fetching scripts for both APIs
- [ ] Specific scripst to handle string maching (fuzzy logic) for artist names and titles
- [ ] Plan and execute a strategy to analyze the "sonic distance" between seed songs and recommended songs

%%
# Instruções de Configuração

## On VSCode
- Start a python env: `python -m venv .venv`
- Allouw Command execuiton on the terminal `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
   - ps.: This will lower the safity of windows but i think it's necessery for my enviroment at lesast 
- Restart the terminal
- Download the libreries `pip install -r requirements.txt`
- Create a file name .env and add the API Keys on it
```python
YOUTUBE_API_KEY=your_key_here
SPOTIFY_CLIENT_ID=your_id_here
SPOTIFY_CLIENT_SECRET=your_secret_here
```
%%