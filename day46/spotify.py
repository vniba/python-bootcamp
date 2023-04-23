import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv
import os
from billbord import songs
import pprint

load_dotenv()
redirect_url = "https://example.com/callback/"
scope = "playlist-modify-private"
auth_manager = SpotifyOAuth(
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRECT"),
    client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
    scope=scope,
    redirect_uri=redirect_url,
)

sp = spotipy.Spotify(auth_manager=auth_manager)


results = [
    sp.search(q=f"track:{title} year:{songs['date'][:4]}", type="track")
    for title in songs["title"]
]

track_id = []
for result in results:
    if result["tracks"]["items"]:
        track_id.append(result["tracks"]["items"][0]["id"])
    else:
        continue

print(track_id)


user_id = sp.current_user()["id"]
playlist_name = f"billboard hot 100 {songs['date']}"
playlist_desc = "billboard hot 100 songs omg"
playlist = sp.user_playlist_create(
    user_id, name=playlist_name, public=False, description=playlist_desc
)
print(f"Created playlist '{playlist['name']}' with ID '{playlist['id']}'")
playlist_id = playlist["id"]

if playlist_id and track_id:
    out = sp.playlist_add_items(playlist_id=playlist_id, items=track_id)
    print(out)
