from bs4 import BeautifulSoup
import requests

from urllib.parse import urljoin
from extract_urls_category import extract_books_url
import os
import time
import concurrent.futures


def function2(category_url, a):
    i = 0
    categories_name = []
    # for item in categories_url:

    # print(a[i].text.strip())
    categories_name.append(a[i].text.strip())
    extract_books_url(category_url, a[i].text.strip())
    i += 1


def function():
    start_time = time.time()
    # home_url = 'http://books.toscrape.com/index.html'
    home_url = 'http://books.toscrape.com/index.html'

    session = requests.Session()
    # adapter = requests.adapters.HTTPAdapter(
    #     pool_connections=1000,
    #     pool_maxsize=1000)
    # session.mount('http://', adapter)
    # session = 0
    # make a get request
    # s.get(home_url)
    # html_page = s.get(home_url)
    # html_page = requests.get(home_url)
    html_page = session.get(home_url)

    soup = BeautifulSoup(html_page.text, 'lxml')

    ul = soup.find('ul', class_='nav nav-list')
    ul2 = ul.find('ul')

    a = ul2.find_all('a')

    current_directory = '../'
    csv_dir = "csv"

    path = os.path.join(current_directory, csv_dir)
    if not os.path.exists(path):
        os.mkdir(path)

    web_url = 'http://books.toscrape.com'
    categories_url = []

    for item in a:

        absolute_path = urljoin(web_url, item.attrs['href'])

        categories_url.append(absolute_path)
    i = 0
    # list = []
    categories_name = []

    for item in categories_url:

        # print(a[i].text.strip())
        categories_name.append(a[i].text.strip())
        extract_books_url(item, a[i].text.strip(), session)
        end_time = time.time()

        print(end_time - start_time)
        i += 1

    end_time = time.time()
    print(end_time - start_time)
    return categories_url, categories_name


function()
