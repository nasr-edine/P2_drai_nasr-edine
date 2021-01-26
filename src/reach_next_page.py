from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import re

def get_current_page(soup):
    current_page = soup.find('li', class_='current')
    if not current_page:
        # print('there are 1 page only in this category')
        return
    # print(current_page.text.strip())
    current_page  = current_page.text.strip()
    number = [int(s) for s in current_page.split() if s.isdigit()]
    
    # print('current page: ' + str(number[0]))
    # print('last page   : '    +str(number[-1]))
    return number


def reach_next_page(url_page):
    # url_page = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    # url_page = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    # url_page = 'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html'
    

    response = requests.get(url_page).text
    # print(response)
    soup = BeautifulSoup(response, 'lxml')
    list = []
    number = get_current_page(soup)
    if not number:
        list.append(url_page)
        # print('there are only 1 page')
        return list
    current_page = number[0]
    last_page = number[-1]

    # print('current page: ' + str(current_page))
    # print('last page   : '    +str(last_page))
    

    # TODO remove fiename from url
    # .rsplit('/', 1)[0]
    urls = []
    urls.append(url_page)
    url_page = url_page.rsplit('/', 1)[0] + '/'
    # print(url_page)
    url_page = urljoin(url_page, 'page-0.html')

   



    # print(url_page)
    # all_pages = []
    # # TODO add all pages in a list
    
    while current_page < last_page:
        current_page += 1
        org_string = "page-0.html"
        pattern = r'[0-9]'
        # Match all digits in the string and replace them by empty string
        mod_string = re.sub(pattern, str(current_page), org_string)
        # print(mod_string)
        url_page = urljoin(url_page, mod_string)
        # print(url_page)
        urls.append(url_page)
    
    return(urls)


# reach_next_page()