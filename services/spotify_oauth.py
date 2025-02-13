SPOTIFY_CLIENT_ID = "a0a2db3b4cb5471f9d5b2ba16544f32d"
SPOTIFY_CLIENT_SECRET = "c6f8c960594d41638d56aadd2668ce4c"
SPOTIFY_REDIRECT_URI = "https://5000-astorelloo-spotifyflask-rxeeownq96n.ws-eu117.gitpod.io/callback" #DA AGGIUNGERE
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private" #permessi x informazioni dell'utente
)
def get_spotify_object(token_info):
    return spotipy.Spotify( auth=token_info['access_token'])