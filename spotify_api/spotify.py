import requests
import json

# API endpoint for searching tracks
SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'

# Your Spotify access token
ACCESS_TOKEN = 'your_access_token_here'

# Search query parameters
query = 'track:love on the brain artist:Rihanna'
search_type = 'track'
limit = 10

# Set up the request headers
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

# Set up the request parameters
params = {
    'q': query,
    'type': search_type,
    'limit': limit
}

# Send the API request
response = requests.get(SEARCH_ENDPOINT, headers=headers, params=params)

# Parse the response JSON
data = response.json()

# Process and extract the desired information
if 'tracks' in data:
    tracks = data['tracks']['items']
    for track in tracks:
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        album_name = track['album']['name']
        print(f'Track: {track_name} | Artist: {artist_name} | Album: {album_name}')
else:
    print('No tracks found.')
