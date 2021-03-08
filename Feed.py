#!/usr/bin/python3
import os
import argparse
import sys
from dotenv import load_dotenv

from Monitors import Monitors
from Discord import Discord
from Feeds import Feeds

if sys.argv[1] == '-h' or len(sys.argv) < 2:
    print('./Feed.py url webhook_url')
    sys.exit()

env = "FEED_WEBHOOK_URL"  # semi permenant
bsTypeId = None

url = sys.argv[1]

# absorbs multiple keywords
keywordArr = []
if len(sys.argv) > 2:
    keywordArr = sys.argv[2].split(',')

load_dotenv()
webhook_url = os.getenv(env)

f = Feeds()
data = f._generateData(url)
res = f._separateData(data)
f.logToDiscord(webhook_url, res, keywordArr)
# Discord.message(siteUrl, webhook_url, "Proxied site has changed")
