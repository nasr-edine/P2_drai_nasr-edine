from bs4 import BeautifulSoup
import requests
import re
import csv
from urllib.parse import urljoin
from save_image import dowload_image
import os

def extract_detailled_product(product_page_url, category_file):
    html_requests = requests.get(product_page_url).text
    # product_page_url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

    soup = BeautifulSoup(html_requests, 'lxml')
    # print(soup)
    title = soup.find('h1').text

    product_information = soup.findAll("table", class_= 'table-striped')
    article = soup.find("article", class_='product_page')
    product_description = article.find("h2").find_next('p').text
    ul = soup.find("ul", class_="breadcrumb")
    li = ul.find_all("li")
    category = li[-2].text.strip()

    product_gallery = article.find("div", class_="carousel")
    # print(product_gallery)
    
    # TODO fix url image to absolute
    base = 'http://books.toscrape.com'
    image_url = product_gallery.find("img", )['src']
    image_url = urljoin(base, image_url)
    dowload_image(image_url)
    # print(image_url)
    
    # print(url_image)
    td_list = []
    # print(td_list)
    for td in product_information[0].findAll('td'):
        td_list.append(td.text)
    # print(td_list)


    #print("product_page_url:".ljust(25), product_page_url)
    universal_product_code = td_list[0]
    #print("universal_product_code:".ljust(25), td_list[0])
    #print("title:".ljust(25), title)
    numbers = re.findall('[0-9]+.?[0-9]+', td_list[2])

    price_including_tax = u'\u00A3'+numbers[0]
    #print("price_including_tax:".ljust(25), price_including_tax)
    numbers = re.findall('[0-9]+.?[0-9]+', td_list[3])
    price_excluding_tax = u'\u00A3'+numbers[0]
    #print("price_excluding_tax:".ljust(25), price_excluding_tax)

    numbers = re.findall('[0-9]+', td_list[5])
    number_available = numbers[0]
    #print("number_available:".ljust(25),number_available)

    #print("product_description:".ljust(25), product_description)
    #print("category:".ljust(25), category)

    # print("category:".ljust(25), td_list[1])
    review_rating = td_list[-1]
    #print("review_rating:".ljust(25), review_rating)
    #print("image_url:".ljust(25), image_url)

    thisdict = {
                'product_page_url':product_page_url,
                'universal_product_code':universal_product_code,
                'title':title,
                'price_including_tax':price_including_tax,
                'price_excluding_tax':price_excluding_tax,
                'number_available':number_available,
                'product_description':product_description,
                'category':category,
                'review_rating':review_rating,
                'image_url':image_url
    }
    # print(thisdict)
    # for key in thisdict:
        # print(key, ' : ', thisdict[key])
    print(category_file + '.csv')
    current_directory = '../'
    csv_dir = 'csv'
    path_csv = os.path.join(current_directory, csv_dir)
    filename = category_file + '.csv'
    path = os.path.join(path_csv, filename)
    with open(path, 'a+', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow([   
        #                     'product_page_url',
        #                     'universal_ product_code',
        #                     'title',
        #                     'price_including_tax',
        #                     'price_excluding_tax',
        #                     'number_available',
        #                     'product_description',
        #                     'category',
        #                     'review_rating',
        #                     'image_url'
        #                 ])
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
    return thisdict

# extract_detailled_product('http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')