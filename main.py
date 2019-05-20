from bs4 import BeautifulSoup
import requests

# Custom imports
import songsGetter
import lyricsGetter
import albumsGetter


if __name__ == '__main__':
    artist = input('Artist or band: ')
    albums = albumsGetter.get_album(artist)

    # Gets the album song titles
    print('>>> Getting tracks')
    songs_raw = []
    for album in albums:
        songs_raw.append(songsGetter.get_songs(artist, album))

    #Gets the song lyrics
    print('>>> Getting lyrics')
    lyricsArray = []
    for album in songs_raw:
        for track in album:
            lyrics = lyricsGetter.get_lyrics(artist, track)
            lyricsArray.append(lyrics)

    print(lyricsArray)

    with open('output.txt', 'w') as f:
        for item in lyricsArray:
            f.write("%s\n" % item)

