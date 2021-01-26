from bs4 import BeautifulSoup
import requests
import re
import csv
from urllib.parse import urljoin
import os
from extract_book_page import extract_detailled_product

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
    # category_page = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    # category_page = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    # category_page = 'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html'

    current_directory = '../'
    csv_dir = 'csv'
    path_csv = os.path.join(current_directory, csv_dir)
    filename = category + '.csv'
    path = os.path.join(path_csv, filename)
    create_csv_file(path)
    all_pages = reach_next_page(category_page)
    # print(all_pages)
    i = 0
    for page in all_pages:
        html_requests = requests.get(page).text
        soup = BeautifulSoup(html_requests, 'lxml')

        web_url = 'http://books.toscrape.com'
        urls = []

        slice_object = slice(9, None, 1)

        # loop for extract url
        for h in soup.find_all('h3'):
            a = h.find('a')
            string = a.attrs['href']
            absolute_path = 'catalogue/' + string[slice_object]
            
            #TODO integrate get_next_pages here
            absolute_path = urljoin(web_url,   absolute_path)
            # print(absolute_path)
            # reach_next_page(absolute_path)

            urls.append(absolute_path)

        # record information for 1 book in a dictionnary
        dic = {}
        # print('page:'+ str(i))
        for url in urls:
            dic = extract_detailled_product(url, category)
        i += 1
        # print(dic)
    return urls
    

