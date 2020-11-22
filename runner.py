#!/usr/bin/python3

from discordBot import sampleMessage
from pageMonitor import finder
import os
from dotenv import load_dotenv

load_dotenv()
webhook_url = os.getenv("WEBHOOK_URL")

found_bigw = finder(
    "749", 'https://www.bigw.com.au/entertainment/video-games-consoles/ps5/c/6412118/')

if found_bigw:
    sampleMessage('bigw', webhook_url)
else:
    sampleMessage('not_found', webhook_url)
