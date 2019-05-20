from bs4 import BeautifulSoup
import requests

# Custom imports
import songsGetter
import lyricsGetter


if __name__ == '__main__':
    artist = input('Artist or band: ')
    slug = 'https://www.last.fm/search/albums?q=%s' % artist.lower().replace(' ', '+')
    page = requests.get(slug)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Gets the artist albums
    print('>>> Getting albums')
    albums_raw = soup.find_all('h4', class_='album-result-heading')
    print('>>> ', len(albums_raw), ' Albums found')
    albums = []
    for album in albums_raw:
        albums.append(' '.join(album.get_text().split()))

    print(albums)
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

