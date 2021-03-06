from ConnectionManager import ConnectionManager
from pageMonitor import multiReader
from bs4 import BeautifulSoup
import re
import os.path
import sys
import requests

# azKeyword = sys.argv[1]


class Monitors:
    def __init__(self):
        self.placeholder = "0"
        self.placeholdersite = "http://icanhazzip.com/"

    @classmethod
    def getRequest(self, site):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
        response = requests.get(site, headers=headers, timeout=5)
        return response.text

    @classmethod
    def _proxify(self, site):
        cm = ConnectionManager()
        cm._get_connection()
        response = cm.request(site).read()
        return response

    @classmethod
    def _bsExtract(self, keyword, response, bsType, fileReader, id=None):
        soup = BeautifulSoup(response, "lxml")
        data = ""

        if bsType == 'text':
            for extract in soup.find_all(text=re.compile(keyword+'*')):
                data += str(extract) + '\n'
        elif bsType == 'a':
            for extract in soup.find_all('a'):
                if re.search(keyword, str(extract), re.IGNORECASE):
                    data += str(extract) + '\n'
        elif bsType == 'ahref':
            for extract in soup.find_all('href'):
                if re.search(keyword, str(extract), re.IGNORECASE):
                    data += str(extract) + '\n'
        elif bsType == 'span':
            if id != None:
                for extract in soup.find_all('span', id=id):
                    if re.search(keyword, str(extract), re.IGNORECASE):
                        data += str(extract) + '\n'
            else:
                for extract in soup.find_all('span'):
                    if re.search(keyword, str(extract), re.IGNORECASE):
                        data += str(extract) + '\n'
        elif bsType == 'button':
            for extract in soup.find_all('button'):
                if re.search(keyword, str(extract), re.IGNORECASE):
                    data += str(extract) + '\n'
        else:
            print("Using customised tag")
            for extract in soup.find_all(bsType):
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
            file.write(data)  # TODO: pokemon catcher
            return 0

    @classmethod
    def query(self, keyword, site, bsType, filename, bsTypeId, enableProxy= False):
        res = ""
        if enableProxy == True:
            res = self._proxify(site)
        else:
            res = self.getRequest(site)

        success = self._bsExtract(keyword, res, bsType, filename, bsTypeId)
        if success:
            print("Found change in: " + site)
            return 1
        else:
            print("No change in: " + site)
            return 0

# testProxy(azKeyword,"sample")

# Assigns a new identity
# cm.new_identity()
