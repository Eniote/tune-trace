# Tune-trace: A Metadata Integration for Youtube & Spotify
This project aims to cross-reference and unify music track metadata from **YouTube** and **Spotify**.

While both platforms host similar content, their metadata schemas and available attributes differ significantly. The primary goal is to perform **Entity Resolution**—identifying that "Track A" on YouTube is the same as "Track B" on Spotify—to create a unified, enriched dataset.

The secondery objective is to analyze the behavior of the recommendetions on youtube:  Does Youtube recommend tracks that are similar as per the Spotify metrics?


## Problem Statement & Hypothesis
YouTube and Spotify operate as data silos. By integrating them, we aim to:
1.  Utilize graph analysis to find relationships between songs that aren't obvious when looking at a single platform isolatedly.
2.  Explore the pipeline of collecting (ETL), cleaning, and analyzing heterogeneous data sources.
3.  Eansor the question: If a Track A recommends Track B on youtube, how similar are ther acoustic features (valance, tempo, energy) in Spotify's metrics?
4.  Visualize everythin in buitlfie graphics ^-^

## Tools
### Data colleciton
- `spotipy` for colecting Spotify's data
- `[youtube's Python API librery here]` for colecting Youtube's data
### Data Engeneerign
- `pandas` the number 1 python lybrery for structuring data and math stuff

## ToDos
- [ ] Define data models for "Track" and "Artist" to normalize API responses
- [ ] Implament authentication and basic fetching scripts for both APIs
- [ ] Specific scripst to handle string maching (fuzzy logic) for artist names and titles
- [ ] Plan and execute a strategy to analize the distance between seed songs and recommended songs based on audio features

