#!/usr/bin/python3
import os
import argparse
import sys
from discordBot import sampleMessage, message
from pageMonitor import finder, differences, differencesMultiple, differencesPage, differencesMultipleId, multiReader, multiReaderMultiFile
from dotenv import load_dotenv

# Future implementation will use ArgumentParser
# parser = argparse.ArgumentParser(
#     description='Monitors data on each run. This should be used with as a cronjob')

# parser.add_argument(
#     'difference', help='Checks any difference by storing the last read source in the directory and comparing at time of run')

if sys.argv[1] == '-h' or len(sys.argv) < 2:
    print('./runner.py <method> <url> <keyword> <discord-key> <output-file> <env>')
    sys.exit()

method = sys.argv[1]
url = sys.argv[2]
key_out = sys.argv[3]
discord_key = sys.argv[4]
output = sys.argv[5]

env = "DEV_WEBHOOK_URL"
if len(sys.argv) > 6:
    env = sys.argv[6]

load_dotenv()
webhook_url = os.getenv(env)

# switch statement does not exist in python?
if method == 'finder':
    res = finder(key_out, url)
    if res:
        message(discord_key, webhook_url, "Found keyword {}".format(key_out))
elif method == 'difference':
    res = differences(url, key_out, output)
    if res:
        message(discord_key, webhook_url, "Targeted website has changed")
elif method == 'differenceMultiple':
    res = differencesMultiple(url, key_out, output)
    if res:
        message(discord_key, webhook_url, "Targeted website has changed")
elif method == 'differenceMultipleId':
    res = differencesMultipleId(url, key_out, output)
    if res:
        message(discord_key, webhook_url, "Targeted website has changed")
elif method == 'differencePage':
    res = differencesPage(url, output)
    if res:
        message(discord_key, webhook_url, "Targeted website has changed")
elif method == 'multiReader':
    res = multiReader(url, key_out, output)
    if res:
        message(discord_key, webhook_url, "Targeted website has changed")
elif method == 'multiReader2':
    res = multiReaderMultiFile(url, key_out, output)
    if res:
        message(discord_key, webhook_url, "Targeted website has changed")
else:
    print('Unable to determine method that has been specified. Please try again..')
    sys.exit()
