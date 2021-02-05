import requests


def initialize():
    global s
    s = requests.session()
    global a
    a = []
