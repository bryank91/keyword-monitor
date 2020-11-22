#!/usr/bin/python3

import requests
from discord import Webhook, RequestsWebhookAdapter


def sampleMessage(loc, webhook_url):
    webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter())
    try:
        webhook.send("New update from {}".format(loc))
    except:
        print("Something went wrong when trying to send messages")
