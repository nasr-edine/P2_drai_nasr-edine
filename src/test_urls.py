import unittest
import requests
from extract_urls_category import extract_books_url

class Test_urls(unittest.TestCase):
    def test_urls(self):
        # urls = extract_books_url('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
        urls = extract_books_url('http://books.toscrape.com/catalogue/category/books/mystery_3/index.html')

        for url in urls:
            # print(url)
            r = requests.get(url)
            self.assertEqual(r.status_code, 200)
        print('Urls are OK')


