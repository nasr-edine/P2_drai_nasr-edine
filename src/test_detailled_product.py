import unittest
# import requests
from extract_book_page import extract_detailled_product


class Test_detailled_product(unittest.TestCase):
    def test_detailled_product(self):
        url = 'http://books.toscrape.com/catalogue/' \
              'a-light-in-the-attic_1000/index.html'
        detailled_product = extract_detailled_product(url)
        print(detailled_product)
