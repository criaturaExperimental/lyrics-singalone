from bs4 import BeautifulSoup
import requests
from unidecode import unidecode
import os

def adapt_song(title):
    return unidecode(title).replace(' ', '-').lower()


def get_lyrics(artist, song):
    # artist = 'Amaral'
    # song = 'Días de verano'
    titleAdapted = adapt_song(song)
    slug = 'https://genius.com/%s-%s-lyrics' % (artist, titleAdapted)
    page = requests.get(slug)
    soup = BeautifulSoup(page.text, 'html.parser')

    lyrics_raw = soup.p.get_text().replace('...', '')
    print(lyrics_raw)
    return lyrics_raw

if __name__ == '__main__':
    lyrics = get_lyrics('Amaral', 'Días de verano')
    song = 'dias de verano'

    directory = os.path.abspath('./data/test/')
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = os.path.join(directory, song)
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(lyrics)