#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Split file in l parts and run this script in parallel on them (in the end cat them together again)
#split -n l/x <file> -a 1 <prefix>

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
import sys
   
if __name__ == "__main__":

     analyzer = SentimentIntensityAnalyzer()

     with open(sys.argv[1], "rb") as a:

        tweets=a.readlines()
        [print(json.dumps(analyzer.polarity_scores(tweet.decode("utf-8").rstrip("\n")))) for tweet in tweets]