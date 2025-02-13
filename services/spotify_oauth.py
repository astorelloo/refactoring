import spotipy
from spotipy.oauth2 import SpotifyOAuth

#le tue credenziali le trovi nella dashboard di prima
SPOTIFY_CLIENT_ID = "a0a2db3b4cb5471f9d5b2ba16544f32d"
SPOTIFY_CLIENT_SECRET = "c6f8c960594d41638d56aadd2668ce4c"
SPOTIFY_REDIRECT_URI = "https://5000-astorelloo-refactoring-01hod411ni7.ws-eu117.gitpod.io/callback" #DA AGGIUNGERE

sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private",
    show_dialog=True 
)


def get_spotify_object(token_info):
    return spotipy.Spotify( auth=token_info['access_token'])