import os
import time
import P2_06_codesource
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from P2_02_codesource import extract_books_url
# import concurrent.futures
# from concurrent.futures import ProcessPoolExecutor, as_completed

base_url = 'http://books.toscrape.com'
home_url = 'http://books.toscrape.com/index.html'


if __name__ == '__main__':
    start_time = time.time()

    P2_06_codesource.initialize()

    html_page = P2_06_codesource.s.get(home_url)

    soup = BeautifulSoup(html_page.text, 'lxml')
    ul = soup.find('ul', class_='nav nav-list')
    ul2 = ul.find('ul')

    P2_06_codesource.a = ul2.find_all('a')

    current_directory = '../'
    csv_dir = "csv"
    path = os.path.join(current_directory, csv_dir)
    if not os.path.exists(path):
        os.mkdir(path)

    for item in P2_06_codesource.a:
        absolute_path = urljoin(base_url, item.attrs['href'])
        extract_books_url(absolute_path)
    end_time = time.time()
    print(end_time - start_time)

    # function = concurrent.futures.ProcessPoolExecutor(max_workers=4)
    # for item in categories_url:
    #     function.submit(extract_books_url, item)

    # with ProcessPoolExecutor(max_workers=10) as executor:
    #     start_time = time.time()
    #     futures = [ executor.submit(extract_books_url, url)
    #       for url in categories_url]
