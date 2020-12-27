from ConnectionManager import ConnectionManager
from pageMonitor import multiReader
from bs4 import BeautifulSoup
import re
import os.path
import sys

azKeyword = sys.argv[1]

def testProxy(keyword, fileReader):
    cm = ConnectionManager()
    cm._get_connection()
    response = cm.request("https://www.amazon.com.au/s?k=ps5&ref=nb_sb_noss").read() # TODO: hardcoded
    # response = cm.request("http://icanhazip.com/").read() # TODO: change
    soup = BeautifulSoup(response, "lxml")
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
    for extract in soup.find_all('button'):
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

testProxy(azKeyword,"sample")

# Assigns a new identity
# cm.new_identity()