import sys
import time
import json
import tweepy
import datetime


reload(sys)
sys.setdefaultencoding('utf-8')

auth = tweepy.OAuthHandler(str(sys.argv[3]),str(sys.argv[4]))
api = tweepy.API(auth,wait_on_rate_limit=True)

folder = str(sys.argv[2])
fin = open(sys.argv[1], "rt")

linebuffer = list()
for line in fin:
	uid = int(line.replace("\n",""))
	try:
		with open(folder+"/"+str(uid)+".json", "wt") as fout:
			for tweet in tweepy.Cursor(api.user_timeline, id=uid).items():
				fout.write(json.dumps(tweet._json) + "\n")
	except tweepy.TweepError as e:
		print e
fin.close()






