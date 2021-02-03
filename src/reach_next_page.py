from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import re


def get_current_page(soup):
    current_page = soup.find('li', class_='current')
    if not current_page:

        return

    current_page = current_page.text.strip()
    number = [int(s) for s in current_page.split() if s.isdigit()]

    return number


def reach_next_page(url_page, session):
    # response = requests.get(url_page).text
    response = session.get(url_page).text

    soup = BeautifulSoup(response, 'lxml')
    list = []
    number = get_current_page(soup)
    if not number:
        list.append(url_page)

        return list
    current_page = number[0]
    last_page = number[-1]

    urls = []
    urls.append(url_page)
    url_page = url_page.rsplit('/', 1)[0] + '/'

    url_page = urljoin(url_page, 'page-0.html')

    while current_page < last_page:
        current_page += 1
        org_string = "page-0.html"
        pattern = r'[0-9]'

        mod_string = re.sub(pattern, str(current_page), org_string)

        url_page = urljoin(url_page, mod_string)

        urls.append(url_page)
    return(urls)
