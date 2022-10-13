import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from bs4 import BeautifulSoup
import requests

cid ='user_id'
secret ='9dadb8714a3b4fc587f33684ea9d0029'
uri_info='spotify:album:5BLwx5IlfoWOrjJJ3i7gbK'

client_credentials_manager = SpotifyClientCredentials(client_id='user_id',client_secret='user_id')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
def get_album_tracks(uri_info):
    uri = []
    track = []
    one = sp.album_tracks(uri_info, limit=50, offset=0, market='US')
    df1 = pd.DataFrame(one)
    
    for i, x in df1['items'].items():
        uri.append(x['uri'])
        track.append(x['name'])
    df2 = pd.DataFrame({
    'uri':uri,
    'track':track,
    })
    return df2

def audio_info(df):
    danceability = []
    energy = []
    key = []
    loudness = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []
    tempo = []
    for i in df['uri']:
        for x in sp.audio_features(tracks=[i]):
            danceability.append(x['danceability'])
            energy.append(x['energy'])
            key.append(x['key'])
            loudness.append(x['loudness'])
            speechiness.append(x['speechiness'])
            acousticness.append(x['acousticness'])
            instrumentalness.append(x['instrumentalness'])
            liveness.append(x['liveness'])
            valence.append(x['valence'])
            tempo.append(x['tempo'])
            
    df2 = pd.DataFrame({
    'danceability':danceability,
    'energy':energy,
    'key':key,
    'loudness':loudness,
    'speechiness':speechiness,
    'acousticness':acousticness,
    'instrumentalness':instrumentalness,
    'liveness':liveness,
    'valence':valence,
    'tempo':tempo})
    
    return df2

# df3=get_album_tracks("spotify:album:3T4tUhGYeRNVUGevb0wThu")
#function to scrape lyrics from genius

def merge_frames(df1, df2):
    df3 = df1.merge(df2, left_index= True, right_index= True)
    return df3
def scrape_lyrics(artistname, songname):
    artistname2 = str(artistname.replace(' ','-')) if ' ' in artistname else str(artistname)
    songname2 = str(songname.replace(' ','-')) if ' ' in songname else str(songname)
    page = requests.get('https://genius.com/'+ artistname2 + '-' + songname2 + '-' + 'lyrics')
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics1 = html.find("div", class_="lyrics")
    lyrics2 = html.find("div", class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
    if lyrics1:
        lyrics = lyrics1.get_text()
    elif lyrics2:
        lyrics = lyrics2.get_text()
    elif lyrics1 == lyrics2 == None:
        lyrics = None
    return lyrics

#function to attach lyrics onto data frame
#artist_name should be inserted as a string
def lyrics_onto_frame(df1, artist_name):
    for i,x in enumerate(df1['track']):
        test = scrape_lyrics(artist_name, x)
        df1.loc[i, 'lyrics'] = test
    return df1


df3= get_album_tracks('spotify:album:5BLwx5IlfoWOrjJJ3i7gbK')
df4=audio_info(df3)

df1 = merge_frames(df3, df4)
lyrics_onto_frame(df1, 'jubin nautiyal')
print(df1)
df1.to_csv("file.csv")
