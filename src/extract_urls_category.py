from bs4 import BeautifulSoup
import requests

import csv
from urllib.parse import urljoin
import os


from reach_next_page import reach_next_page


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


def extract_books_url(category_page, category):

    current_directory = '../'
    csv_dir = 'csv'
    path_csv = os.path.join(current_directory, csv_dir)
    filename = category + '.csv'
    path = os.path.join(path_csv, filename)
    create_csv_file(path)
    all_pages = reach_next_page(category_page)

    for page in all_pages:
        html_requests = requests.get(page).text
        soup = BeautifulSoup(html_requests, 'lxml')

        web_url = 'http://books.toscrape.com'
        urls = []

        slice_object = slice(9, None, 1)

        for h in soup.find_all('h3'):
            a = h.find('a')
            string = a.attrs['href']
            absolute_path = 'catalogue/' + string[slice_object]

            absolute_path = urljoin(web_url,   absolute_path)

            urls.append(absolute_path)

    return urls
