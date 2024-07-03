from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from youtubesearchpython import VideosSearch
from pytube import YouTube
from pydub import AudioSegment
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = result.json()
    return json_result["access_token"]

def auth_get_headers(token):
    return {"Authorization": f"Bearer {token}"}

def get_playlist_tracks(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = auth_get_headers(token)
    tracks = []
    while url:
        result = get(url, headers=headers)
        result_json = result.json()
        tracks.extend(result_json["items"])
        url = result_json.get("next")
    return tracks

def display_playlist_tracks(tracks):
    if not tracks:
        print("No tracks found in the playlist")
        return

    track_strings = []
    for idx, item in enumerate(tracks):
        track = item['track']
        track_string = f"{track['name']} by {', '.join([artist['name'] for artist in track['artists']])}"
        track_strings.append(track_string)

    return track_strings

playlist_id = "playlist_id"
token = get_token()
tracks = get_playlist_tracks(token, playlist_id)
track_strings = display_playlist_tracks(tracks)

def search_youtube(query, limit=1):
    videos_search = VideosSearch(query, limit=limit)
    results = videos_search.result()
    if results['result']:
        return results['result'][0]['link']
    else:
        return None

def download_youtube_mp3(video_url, output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        downloaded_file = stream.download(output_path)
        base, ext = os.path.splitext(downloaded_file)
        mp3_file = base + '.mp3'
        AudioSegment.from_file(downloaded_file).export(mp3_file, format='mp3')
        os.remove(downloaded_file)
        print(f"Downloaded and converted to MP3: {mp3_file}")
        return mp3_file
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def download_songs_as_mp3(song_names):
    for song_name in song_names:
        print(f"Searching for '{song_name}'")
        video_url = search_youtube(song_name)
        if video_url:
            print(f"Found video: {video_url}")
            download_youtube_mp3(video_url)
        else:
            print(f"Could not find '{song_name}' on YouTube.")

print("Playlist Track Strings:")
for i, track_string in enumerate(track_strings):
    print(f"{i + 1}. {track_string}")

    download_songs_as_mp3(track_strings)

