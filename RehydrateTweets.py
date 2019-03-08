#!/usr/bin/python
import sys
import time
import json
import tweepy
import os
from tweepy.parsers import JSONParser


with open(str(sys.argv[3]), "rt") as credfile:
        par1 = credfile.readline().replace("\n","")
        par2 = credfile.readline().replace("\n","")
        par3 = credfile.readline().replace("\n","")
        par4 = credfile.readline().replace("\n","")

auth = tweepy.OAuthHandler(par1, par2)
auth.set_access_token(par3, par4)

finname = sys.argv[1]
foutname = sys.argv[2]


# Construct the API instance
api = tweepy.API(auth, wait_on_rate_limit=True)


with open(finname, "rt") as fin:
        with open(foutname, "wt") as fout:
                linebuffer = list()
                for line in fin:
                        index = line.replace("\n","").replace("\r","")
                        linebuffer.append(index)
                        if len(linebuffer)==100:
                                statuses = None
                                try:
                                        statuses = api.statuses_lookup(linebuffer,tweet_mode='extended')
                                except tweepy.TweepError as e:
                                        print(e)
                                        statuses = None
                                if statuses != None:
                                        for status in statuses:
                                                fout.write(json.dumps(status._json) + "\n")
                                del linebuffer
                                linebuffer = list()

                if len(linebuffer) > 0:
                        statuses = None

                        try:
                                statuses = api.statuses_lookup(linebuffer,tweet_mode='extended')
                        except tweepy.TweepError:
                                statuses = None
                        if statuses != None:
                                for status in statuses:
                                        fout.write(json.dumps(status._json) + "\n")
 
