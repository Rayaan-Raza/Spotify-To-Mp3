# Spotify-to-MP3-Downloader

## Description

**Spotify-to-YouTube-MP3-Downloader** is a Python script that fetches tracks from a Spotify playlist, searches for them on YouTube, and downloads them as MP3 files. This tool allows users to easily convert their favorite Spotify tracks into MP3 format using YouTube as the source.

## Features

- Fetch tracks from a specified Spotify playlist
- Search for tracks on YouTube
- Download YouTube videos as MP3 files
- Convert downloaded audio files to MP3 format
- Simple and easy-to-use interface

## Usage

1. Set up your Spotify API credentials:
    - Create a `.env` file in the root directory.
    - Add your Spotify client ID and client secret to the `.env` file:
        ```
        CLIENT_ID=your_spotify_client_id
        CLIENT_SECRET=your_spotify_client_secret
        ```

3. Enter the Spotify playlist ID when prompted.

4. The script will fetch the tracks, search for them on YouTube, and download them as MP3 files.

## Example

Here's an example of the script in action:

```bash
$ python downloader.py
Playlist Track Strings:
1. Track Name 1 by Artist 1
2. Track Name 2 by Artist 2
...

Searching for 'Track Name 1 by Artist 1'
Found video: https://www.youtube.com/watch?v=example1
Downloaded and converted to MP3: downloads/Track Name 1.mp3

Searching for 'Track Name 2 by Artist 2'
Found video: https://www.youtube.com/watch?v=example2
Downloaded and converted to MP3: downloads/Track Name 2.mp3
...
