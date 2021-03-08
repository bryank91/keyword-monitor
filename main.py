#!/usr/bin/python3
import os
import argparse
import sys
from dotenv import load_dotenv

from Element.Monitors import Monitors
from Discord.Discord import Discord
from Proxy.ConnectionManager import ConnectionManager

if sys.argv[1] == '-h' or len(sys.argv) < 2:
    print('./Runner.py <method> <url> <keyword> <output-file> <type> <id> <env>')
    sys.exit()

env = "DEV_WEBHOOK_URL"
bsTypeId = None

method = sys.argv[1]
siteUrl = sys.argv[2]
keyword = sys.argv[3]
filename = sys.argv[4]
bsType = sys.argv[5]

if len(sys.argv) > 6:
    bsTypeId = sys.argv[6]

if len(sys.argv) > 7:
    env = sys.argv[7]

load_dotenv()
webhook_url = os.getenv(env)

if method == 'proxyReader':
    m = Monitors()
    suc = m.query(keyword, siteUrl, bsType, filename, bsTypeId, True)
    if suc:
        Discord.message(siteUrl, webhook_url, "Proxied site has changed")
elif method == 'reader':
    m = Monitors()
    suc = m.query(keyword, siteUrl, bsType, filename, bsTypeId)
    if suc:
        Discord.message(siteUrl, webhook_url, "Site trigger")

else:
    print('Unable to determine method that has been specified. Please try again..')
    sys.exit()
