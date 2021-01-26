from bs4 import BeautifulSoup
import requests
import csv
from urllib.parse import urljoin
from extract_urls_category import extract_books_url
import os


def function():

    # filename = 'csv_file.csv'
    # create_csv_file(filename)                    
    home_url = 'http://books.toscrape.com/index.html'
    html_page = requests.get(home_url)
    # print(html_page.status_code)
    # print(html_page.text)
    soup = BeautifulSoup(html_page.text, 'lxml')
    # print(soup)
    ul = soup.find('ul', class_='nav nav-list')
    ul2 = ul.find('ul')
    # print(ul2)
    # li = ul2.find_all('li')
    a = ul2.find_all('a')
    # print(a)

    # create  a csv folder
    current_directory = '../'
    csv_dir = "csv"

    path = os.path.join(current_directory, csv_dir)
    if not os.path.exists(path):
        os.mkdir(path)
    # TODO relative url --> absolute url
    web_url = 'http://books.toscrape.com'
    list = []

    for item in a:
        # print(item.attrs['href'])
        absolute_path = urljoin(web_url, item.attrs['href'])
        # print(absolute_path)
        list.append(absolute_path)
    i = 0
    for item in list:
        # print(item)
        print(a[i].text.strip())
        extract_books_url(item, a[i].text.strip())
        i += 1
    # a.attrs['href']
    # print(li)
    # for item in li:
    #     print(item.text.strip())
    #     list.append(item.text.strip()
    # for url in

function()
