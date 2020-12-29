from ConnectionManager import ConnectionManager
from pageMonitor import multiReader
from bs4 import BeautifulSoup
import re
import os.path
import sys

# azKeyword = sys.argv[1]

class Monitors:
    def __init__(self):
        self.placeholder = "0"
        self.placeholdersite = "http://icanhazzip.com/"

    @classmethod
    def _proxify(self, site):
        cm = ConnectionManager()
        cm._get_connection()
        response = cm.request(site).read()
        return response

    @classmethod
    def _bsExtract(self, keyword, response, bsType, fileReader):
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
            for extract in soup.find_all('span'):
                if re.search(keyword, str(extract), re.IGNORECASE):
                    data += str(extract) + '\n'
        elif bsType == 'button':
            for extract in soup.find_all('button'):
                if re.search(keyword, str(extract), re.IGNORECASE):
                    data += str(extract) + '\n'
        else:
            print("Unable to determine type passed. Please retry (eg. text)")
            return 0

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
            file.write(data) # TODO: pokemon catcher
            return 0

    @classmethod
    def query(self, keyword, site, bsType, filename):
        res = self._proxify(site)
        success = self._bsExtract(keyword,res, bsType, filename)
        if success:
            print("Sucessfully extracted data")
            return 1
        else:
            print("Encountered error when extracting data")
            return 0

# testProxy(azKeyword,"sample")

# Assigns a new identity
# cm.new_identity()