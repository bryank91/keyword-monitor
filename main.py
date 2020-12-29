#!/usr/bin/python3
import os
import argparse
import sys
from dotenv import load_dotenv

from Monitors import Monitors
from Discord import Discord

if sys.argv[1] == '-h' or len(sys.argv) < 2:
    print('./runner.py <method> <url> <keyword> <output-file> <type> <env>')
    sys.exit()

method = sys.argv[1]
siteUrl = sys.argv[2]
keyword = sys.argv[3]
filename = sys.argv[4]
bsType = sys.argv[5]

env = "DEV_WEBHOOK_URL"
if len(sys.argv) > 6:
    env = sys.argv[6]

load_dotenv()
webhook_url = os.getenv(env)

if method == 'proxyReader':
    m = Monitors()
    suc = m.query(keyword,siteUrl,bsType,filename)
    if suc:
        Discord.message(siteUrl,webhook_url, "Proxied site has changed")
else:
    print('Unable to determine method that has been specified. Please try again..')
    sys.exit()
