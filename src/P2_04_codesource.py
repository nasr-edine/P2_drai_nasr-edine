from bs4 import BeautifulSoup
import re
import csv
from urllib.parse import urljoin
from P2_05_codesource import dowload_image
import os
import P2_06_codesource


def extract_detailled_product(product_page_url, category_file):
    html_requests = P2_06_codesource.s.get(product_page_url).text
    soup = BeautifulSoup(html_requests, 'lxml')

    title = soup.find('h1').text

    product_information = soup.findAll("table", class_='table-striped')
    article = soup.find("article", class_='product_page')
    product_description = article.find("h2").find_next('p').text
    ul = soup.find("ul", class_="breadcrumb")
    li = ul.find_all("li")
    category = li[-2].text.strip()

    product_gallery = article.find("div", class_="carousel")

    base = 'http://books.toscrape.com'
    image_url = product_gallery.find("img", )['src']
    image_url = urljoin(base, image_url)
    dowload_image(image_url)

    td_list = []

    for td in product_information[0].findAll('td'):
        td_list.append(td.text)

    universal_product_code = td_list[0]

    numbers = re.findall('[0-9]+.?[0-9]+', td_list[2])

    price_including_tax = u'\u00A3'+numbers[0]

    numbers = re.findall('[0-9]+.?[0-9]+', td_list[3])
    price_excluding_tax = u'\u00A3'+numbers[0]

    numbers = re.findall('[0-9]+', td_list[5])
    number_available = numbers[0]

    review_rating = td_list[-1]

    print(category_file + '.csv')
    current_directory = '../'
    csv_dir = 'csv'
    path_csv = os.path.join(current_directory, csv_dir)
    filename = category_file + '.csv'
    path = os.path.join(path_csv, filename)
    with open(path, 'a+', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([
            product_page_url,
            universal_product_code,
            title,
            price_including_tax,
            price_excluding_tax,
            number_available,
            product_description,
            category,
            review_rating,
            image_url
        ])
    return
