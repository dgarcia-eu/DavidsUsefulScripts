import sys
import time
import json
import tweepy
import datetime

auth = tweepy.OAuthHandler(str(sys.argv[3]),str(sys.argv[4]))
api = tweepy.API(auth,wait_on_rate_limit=True)

folder = str(sys.argv[2])
fin = open(sys.argv[1], "rt")

linebuffer = list()
for line in fin:
	uid = int(line.replace("\n",""))
	try:
		with open(folder+"/"+str(uid)+"_friends.txt", "wt") as fout:
			for friend in tweepy.Cursor(api.friends_ids, id=uid).items():
				fout.write(str(friend) + "\n")
	except tweepy.TweepError as e:
		print(e)
fin.close()






