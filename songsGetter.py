from bs4 import BeautifulSoup
import requests


def get_songs(artist, album):
    # artist = 'Amaral'
    # album = 'Pájaros en la cabeza'
    slug = 'https://www.last.fm/music/%s/%s' % (artist, album)
    page = requests.get(slug)
    soup = BeautifulSoup(page.text, 'html.parser')

    albums_raw = soup.find_all('span', class_='chartlist-ellipsis-wrap')
    albums = []
    for album in albums_raw:
        albums.append(' '.join(album.get_text().split()))


    print(albums)
    return albums