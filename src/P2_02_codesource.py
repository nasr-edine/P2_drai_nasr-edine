from bs4 import BeautifulSoup

import csv
import P2_06_codesource

from urllib.parse import urlparse

from urllib.parse import urljoin
import os

from P2_03_codesource import reach_next_page
from P2_04_codesource import extract_detailled_product

web_url = 'http://books.toscrape.com'


def create_csv_file(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'product_page_url',
            'universal_ product_code',
            'title',
            'price_including_tax',
            'price_excluding_tax',
            'number_available',
            'product_description',
            'category',
            'review_rating',
            'image_url'
        ])


def extract_books_url(category_page):
    urls = []
    parsed = urlparse(category_page)
    category_name = parsed.path.split('/', 4)[4]
    category_name = category_name.split('/', 1)[0]
    print(category_name)
    filename = category_name + '.csv'
    csv_path = os.path.join('../csv', filename)
    create_csv_file(csv_path)
    all_pages = reach_next_page(category_page)

    slice_object = slice(9, None, 1)

    for page in all_pages:
        html_requests = P2_06_codesource.s.get(page).text

        soup = BeautifulSoup(html_requests, 'lxml')

        for h in soup.find_all('h3'):
            a = h.find('a')
            string = a.attrs['href']
            absolute_path = 'catalogue/' + string[slice_object]
            absolute_path = urljoin(web_url,   absolute_path)
            urls.append(absolute_path)
    for url in urls:
        extract_detailled_product(url, category_name)
    return 0
