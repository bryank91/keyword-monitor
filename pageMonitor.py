#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import time
import sys
import pickle
from urllib.request import Request, urlopen
import os.path
import re


def finder(keyword, url):
    # inject headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
    response = requests.get(url, headers=headers, timeout=5)
    soup = BeautifulSoup(response.text, "lxml")

    # result of finder
    extract = soup.find(p=keyword)

    if extract == -1 or extract == None:
        return 0
    else:
        return 1


def foreverFinder(keyword, url):
    while True:
        # inject headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "lxml")

        # result of finder
        extract = soup.find(text=keyword)

        if extract == -1 or extract == None:
            time.sleep(10)
            continue
        else:
            time.sleep(10)


def differences(url, keyword, fileReader):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
    response = requests.get(url, headers=headers, timeout=5)
    soup = BeautifulSoup(response.text, "lxml")
    data = str(soup.find(text=re.compile(keyword+'*')))

    # append comparitor so is included in gitignore
    fileReader = fileReader + "_comparitor"
    comparitor = ""

    # determine if file exist
    if os.path.isfile(fileReader) == True:
        # required for reading. there might be a more optimum step to do this
        r = open(fileReader, "r")
        comparitor = r.read()
    else:  # this is the first run, no need to alert
        file = open(fileReader, "w")
        file.write(data)
        comparitor = data
        return 0

    try:
        file = open(fileReader, "w")

        if data != comparitor:
            file.write(data)
            return 1
        else:
            file.write(data)
            return 0
    except:
        file.write(data)
        return 0


def differencesPage(url, fileReader):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
    response = requests.get(url, headers=headers, timeout=5)
    soup = BeautifulSoup(response.text, "lxml")
    data = str(soup)

    # append comparitor so is included in gitignore
    fileReader = fileReader + "_comparitor"
    comparitor = ""

    # determine if file exist
    if os.path.isfile(fileReader) == True:
        # required for reading. there might be a more optimum step to do this
        r = open(fileReader, "r")
        comparitor = r.read()
    else:  # this is the first run, no need to alert
        file = open(fileReader, "w")
        file.write(data)
        comparitor = data
        return 0

    try:
        file = open(fileReader, "w")

        if data != comparitor:
            file.write(data)
            return 1
        else:
            file.write(data)
            return 0
    except:
        file.write(data)
        return 0


def differencesMultiple(url, keyword, fileReader):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
    response = requests.get(url, headers=headers, timeout=5)
    soup = BeautifulSoup(response.text, "lxml")

    data = ""
    for extract in soup.find_all(text=re.compile(keyword+'*')):
        data += str(extract)

    # append comparitor so is included in gitignore
    fileReader = fileReader + "_comparitor"
    comparitor = ""

    # determine if file exist
    if os.path.isfile(fileReader) == True:
        # required for reading. there might be a more optimum step to do this
        r = open(fileReader, "r")
        comparitor = r.read()
    else:  # this is the first run, no need to alert
        file = open(fileReader, "w")
        file.write(data)
        comparitor = data
        return 0

    try:
        file = open(fileReader, "w")

        if data != comparitor:
            file.write(data)
            return 1
        else:
            file.write(data)
            return 0
    except:
        file.write(data)
        return 0


def differencesMultipleId(url, keyword, fileReader):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
    response = requests.get(url, headers=headers, timeout=5)
    soup = BeautifulSoup(response.text, "lxml")

    data = ""
    for extract in soup.find_all(id=re.compile(keyword+'*')):
        data += str(extract)

    # append comparitor so is included in gitignore
    fileReader = fileReader + "_comparitor"
    comparitor = ""

    # determine if file exist
    if os.path.isfile(fileReader) == True:
        # required for reading. there might be a more optimum step to do this
        r = open(fileReader, "r")
        comparitor = r.read()
    else:  # this is the first run, no need to alert
        file = open(fileReader, "w")
        file.write(data)
        comparitor = data
        return 0

    try:
        file = open(fileReader, "w")

        if data != comparitor:
            file.write(data)
            return 1
        else:
            file.write(data)
            return 0
    except:
        file.write(data)
        return 0


def multiReader(url, keyword, fileReader):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
    response = requests.get(url, headers=headers, timeout=5)
    soup = BeautifulSoup(response.text, "lxml")
    data = ""

    for extract in soup.find_all(text=re.compile(keyword+'*')):
        data += str(extract) + '\n'
    for extract in soup.find_all('a'):
        if re.search(keyword, str(extract), re.IGNORECASE):
            data += str(extract) + '\n'
    for extract in soup.find_all('href'):
        if re.search(keyword, str(extract), re.IGNORECASE):
            data += str(extract) + '\n'
    for extract in soup.find_all('span'):
        if re.search(keyword, str(extract), re.IGNORECASE):
            data += str(extract) + '\n'

    # append comparitor so is included in gitignore
    fileReader = fileReader + "_comparitor"
    comparitor = ""

    # determine if file exist
    if os.path.isfile(fileReader) == True:
        # required for reading. there might be a more optimum step to do this
        r = open(fileReader, "r")
        comparitor = r.read()
    else:  # this is the first run, no need to alert
        file = open(fileReader, "w")
        file.write(data)
        comparitor = data
        return 0

    try:
        file = open(fileReader, "w")

        if data != comparitor:
            file.write(data)
            return 1
        else:
            file.write(data)
            return 0
    except:
        file.write(data)
        return 0
