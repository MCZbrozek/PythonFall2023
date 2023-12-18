# ZbrozekFinal
# Programmer: Mike Zbrozek
# Email: MZbrozek1@cnm.edu
# Purpose: Metronone GUI - read in song list from dictionary to count time for songs I like. 
#Files associated with this assignment - metronome.py, spotify.py
# Spotify.py uses Spotipy library to call various spotify api endpoints, grabs a playlist, gets track ID from the playlist, queries the audio analysis endpoint for tempo and time_signature data.
# and writes to txt file. 
# !!!! I am NOT including my spotify credentials, you will not be able to run this file without API credentials !!!!


# Spotipy https://spotipy.readthedocs.io/en/2.22.1/
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

import os.path
import ast

scope = "playlist-read-private"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))

# https://open.spotify.com/playlist/0jPbco4Xo568ZlbA7dAk55?si=655bbd388c744518&pt=c1658323b0b6dec2ad528060c2bc8a64
def get_id_from_playlist():
    track_id_list = []
    track_data = {}
    playlist = sp.playlist(playlist_id="0jPbco4Xo568ZlbA7dAk55")
    for index, item in enumerate(playlist['tracks']['items']):
        track = item['track']
        album = item['track']['album']['name']
        # artist = item['track']['artists']['name']
        id = item['track']['id']
        track_data ={'track':track['name'], 'track_id':id, 'album':album, 'artist':track['artists'][0]['name']}
        track_id_list.append(track_data)
        # print(index, track['artists'][0]['name']," id = ", id, " - ", track['name'], "album = ", album,)
    return track_id_list

def get_track_data(track_id_list):
    for count, value in enumerate(track_id_list):
        tId = value['track_id']
        audio_data = sp.audio_analysis(track_id=tId)
        for i in audio_data:
           track_data = audio_data['track']
        for j in track_data:
              tempo = track_data['tempo']
              time_signature = track_data['time_signature']
        value['tempo'] = tempo
        value['time_signature'] = time_signature
        # for idx, item in enumerate(audio_data['track']):
        #     # "The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration." - Spotify API Docs
        #     tempo = item['tempo']
        #     # "An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4"." - Spotify API Docs
        #     
    return track_id_list
    

track_id_list = get_id_from_playlist()
track_id_list = get_track_data(track_id_list)
for item in track_id_list:
    print(f"list of track ids = {item}")

def format(track_id_list):
    '''format the track data that I need.'''
    formatted_list = []
    for item in track_id_list:
            formatted_dict = {}
            formatted_dict['artist'] = item['artist']
            formatted_dict['song'] = item['track'] 
            formatted_dict['tempo'] = item['tempo']
            formatted_dict['time_signature'] = f"{item['time_signature']}/4"
            formatted_list.append(formatted_dict)
    return formatted_list


fileLocation = "metronome_songs.txt"
def writeFile(fileLocation, track_id_list):
    '''Check to see if fileLocation exists, if not, then write a new file.'''
    formattedList = format(track_id_list)
    print(formattedList)
    if not os.path.isfile(fileLocation):
        file = open("metronome_songs.txt", "w")
        for i in formattedList:
            file.write(f'{i}\n')
        file.close()

writeFile(fileLocation,track_id_list)

# Test function where initially pulled first batch of data. Refined with the method above. 
# fiftyPlayed = sp.current_user_recently_played()
# for idx, item in enumerate(fiftyPlayed['items']):
#     track = item['track']
#     id = item['track']['id']
#     played_at = item['played_at']
#     print(idx, track['artists'][0]['name']," id = ", {id}, " - ", track['name'], played_at)

# topArtists = sp.current_user_top_artists()
# print(topArtists)


