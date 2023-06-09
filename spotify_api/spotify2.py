import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = <YOUR CLIENT ID>

secret = <YOUR CLIENT SECRET>

 

ccm = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = ccm)

os.environ["SPOTIPY_CLIENT_ID"] = cid
os.environ["SPOTIPY_CLIENT_SECRET"] = secret
os.environ["SPOTIPY_REDIRECT_URI"] = "https://localhost:8080"

scope = 'user-library-read'
username = <YOUR USERNAME HERE>

 

token = spotipy.util.prompt_for_user_token(username, scope)

if token:
spotipy_obj = spotipy.Spotify(auth=token)
saved_tracks_resp = spotipy_obj.current_user_saved_tracks(limit=50)
else:
print('Couldn\'t get token for that username')
