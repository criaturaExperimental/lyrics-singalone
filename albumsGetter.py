from bs4 import BeautifulSoup
import requests

def get_album(artist):
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
    return albums


if __name__ == '__main__':
    get_album('Amaral')