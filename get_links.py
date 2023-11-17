import requests
from bs4 import BeautifulSoup


def get_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True) if a.text.strip()]
        return links
    except Exception as e:
        print(e)
        return []
