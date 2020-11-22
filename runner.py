#!/usr/bin/python3
import os
import argparse
import sys
from discordBot import sampleMessage, message
from pageMonitor import finder, differences
from dotenv import load_dotenv

# Future implementation will use ArgumentParser
# parser = argparse.ArgumentParser(
#     description='Monitors data on each run. This should be used with as a cronjob')

# parser.add_argument(
#     'difference', help='Checks any difference by storing the last read source in the directory and comparing at time of run')

if sys.argv[1] == '-h' or len(sys.argv) < 2:
    print('./runner.py <method> <url> <keyword> <discord-key> <output-file>')
    sys.exit()

load_dotenv()
webhook_url = os.getenv("DEV_WEBHOOK_URL")

method = sys.argv[1]
url = sys.argv[2]
key_out = sys.argv[3]
output = sys.argv[4]

discord_key = "undefined"
if len(sys.argv) > 4:
    discord_key = sys.argv[4]

# switch statement does not exist in python?
if method == 'finder':
    res = finder(key_out, url)
    if res:
        message(discord_key, webhook_url, "Found keyword {}".format(key_out))
elif method == 'difference':
    res = differences(url, key_out, output)
    if res:
        message(discord_key, webhook_url, "Targeted website has changed")
else:
    print('Unable to determine method that has been specified. Please try again..')
    sys.exit()
