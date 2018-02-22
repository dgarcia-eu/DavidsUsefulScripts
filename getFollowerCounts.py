import sys
import time
import json
import tweepy
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

auth = tweepy.OAuthHandler(str(sys.argv[2]),str(sys.argv[3]))
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

fin = open(sys.argv[1], "rt")
querylist = list()
allusersdata = list()

for line in fin:
	querylist.append(line.replace("\n",""))
	if len(querylist) == 100:
		try:
			usersdata = api.lookup_users(screen_names=querylist)				
		except tweepy.TweepError as e:
			print e
		allusersdata.extend(usersdata)
		querylist = list()

if len(querylist) > 0:
	try:
		usersdata = api.lookup_users(screen_names=querylist)				
	except tweepy.TweepError as e:
		print e
	allusersdata.extend(usersdata)

for ud in allusersdata:
	print ud.screen_name + "\t" + str(ud.followers_count)
