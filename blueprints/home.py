from flask import Blueprint, redirect, request, url_for, session, render_template
import spotipy
from services.spotify_oauth import sp_oauth, get_spotify_object

home_bp = Blueprint('home', __name__) 

@home_bp.route('/home')
def home():
    token_info = session.get('token_info', None) #recupero token sissione (salvato prima)
    if not token_info:
        return redirect(url_for('login'))
    sp = spotipy.Spotify(auth=token_info['access_token']) #usiamo il token per ottenere i dati del profilo
    user_info = sp.current_user()
    playlists = sp.current_user_playlists() #sempre tramite il token sp preso prima
    playlists_info = playlists['items']
    print(user_info) #capiamo la struttura di user_info per usarle nel frontend
    return render_template('home.html', user_info=user_info, playlists=playlists_info) #passo le info utente all'home.html

sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private", #permessi x informazioni dell'utente
    show_dialog=True #forziamo la richiesta di inserire new credenziali
)


@home_bp.route('/playlist/<playlist_id>')
def playlist_details(playlist_id):
    token_info = session.get('token_info', None)
    if not token_info:
        return redirect(url_for('login'))

    sp = spotipy.Spotify(auth=token_info['access_token'])
    brani = sp.playlist_items(playlist_id)
    brani_specifici = brani['items']
    return render_template('brani.html',brani = brani_specifici)


