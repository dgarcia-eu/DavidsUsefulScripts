#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:55:35 2018

@author: maxpe + dgarcia
"""

import sys
import os
import time
import json
import tweepy
import datetime
from tweepy.parsers import JSONParser

auth = tweepy.OAuthHandler(...", "...")
auth.set_access_token("...",  "...")

foutname = "ColombiaStream"

def timeStamped(fname, fmt='{fname}_%Y-%m-%d-%H-%M-%S'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

#os.chdir("/home/mpellert/bots/")

GEOBOX_COLOMBIA = [-79.09,-4.24,-66.8,12.55]
#long lat long lat

while True:

    with open(timeStamped(foutname), "wt",1) as fout:

        class MyStreamListener(tweepy.StreamListener):

            def on_status(self, status):
                print(status.user.id)
                fout.write(str(status._json) + "\n")

            def on_error(self, status_code):
                return False

            def on_disconnect(self, notice):
                return False

            def on_timeout(self):
                return False
        try:
            api = tweepy.API(auth,wait_on_rate_limit=True)
            myStreamListener = MyStreamListener()
            myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener, timeout=60)
            myStream.filter(locations=GEOBOX_COLOMBIA)
            myStream.sample()

        except Exception as e:
            print(e)
            time.sleep(60)  
