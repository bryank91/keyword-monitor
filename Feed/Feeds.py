#!/usr/bin/python3
from pageMonitor import multiReader
from Monitors import Monitors
from bs4 import BeautifulSoup
from lxml import etree
import os.path
from Discord import Discord


class Feeds:

    @classmethod
    def _generateData(self, link):
        m = Monitors()
        response = m.getRequest(link)
        return response

    @classmethod
    def _logId(self, id, site):
        file = open(site, "w")
        file.write(id)

    @classmethod
    def _checkId(self, site):
        if os.path.isfile(site) == True:
            r = open(site, "r")
            res = r.read()
            return int(res)
        else:
            file = open(site, "w")
            file.write('0')  # initialise new document
            return 0

    @classmethod
    def _separateData(self, data):
        soup = BeautifulSoup(data, "xml")
        result = []

        for item in soup.find_all('item'):
            title = item.select("title")[0].text

            # we need to keep track of the link id (assuming this is the id of the item)
            link = item.select("link")[0].text
            id = link.split('/')[-1]

            description = item.select("description")[0]
            description = description.select("p")

            # TODO:
            # https://stackoverflow.com/questions/2872512/python-truncate-a-long-string
            # truncateDescription = (description[:75] + '..') if len(description) > 75 else description

            res = {'title': title,
                   'id': id,
                   'link': link,
                   'description': description
                   }

            result.append(res)

        return result

    @classmethod
    def logToDiscord(self, webhook_url, arr, keywordArr=[]):

        # sort the list according to the smallest to biggest
        sortedArr = sorted(arr, key=lambda x: (x['id']))
        highestId = ""

        for item in sortedArr:
            # list already sorted so will not need to check
            highestId = item['id']

            # In certain occurences, this will break, so lets reset this
            highestIdComparitor = 0
            try:
                highestIdComparitor = self._checkId('oz')
            except:
                print("It is failing in highestIdComparitor. Defaulting to 0...")
                highestIdComparitor = 0

            if (int(highestId) > self._checkId('oz')):
                message = f'''{item['title']} - {item['link']}'''
                Discord.send(webhook_url, message)

                # verify if it matches certain keywords
                if len(keywordArr) > 0:
                    for keyword in keywordArr:
                        if keyword in item['title'].lower():
                            Discord.send(webhook_url,"Keyword: " + keyword + " trigger @everyone") 
                 

        self._logId(highestId,'oz')
