#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import time


def finder(keyword, url):
    # inject headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    # Full website source code
    # print(str(soup))

    # result of finder
    extract = soup.find(text=keyword)

    if extract == -1 or extract == None:
        print("Unable to find keyword")
        return 0
    else:
        print("Found keyword")
        return 1


def foreverFinder(keyword, url):
    while True:
        # inject headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        # result of finder
        extract = soup.find(text=keyword)

        if extract == -1 or extract == None:
            time.sleep(10)
            continue
        else:
            print("Found something different")
            time.sleep(10)
