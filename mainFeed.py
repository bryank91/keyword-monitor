#!/usr/bin/python3
import os
import argparse
import sys
from dotenv import load_dotenv

from Monitors import Monitors
from Discord import Discord
from Feeds import Feeds

if sys.argv[1] == '-h' or len(sys.argv) < 2:
    print('./mainFeed.py url webhook_url')
    sys.exit()

env = "FEED_WEBHOOK_URL"
bsTypeId = None

url = sys.argv[1]

if len(sys.argv) > 2:
    env = sys.argv[2] # sets the webhook url

load_dotenv()
webhook_url = os.getenv(env)

f = Feeds()
data = f._generateData(url)
res = f._separateData(data)
f.logToDiscord(webhook_url,res)
# Discord.message(siteUrl, webhook_url, "Proxied site has changed")