import sys
import botometer

mashape_key = "mashape key"
twitter_app_auth = {
	'consumer_key': 'consumer key',
	'consumer_secret': 'consumer secret',
	'access_token': 'access token',
	'access_token_secret': 'access token secret',
}

bom = botometer.Botometer(wait_on_ratelimit=True, mashape_key=mashape_key, **twitter_app_auth)


finname = sys.argv[1]
foutname = sys.argv[2]


print "all set"

i = 1
with open(finname, "rt") as fin:
	with open(foutname, "wt") as fout:
		fout.write("id\tuniversalScore\tenglishScore\n")
		for line in fin: 
			userid = line.strip()
			try:
				result = bom.check_account(userid)
				print str(i) +"\t" + str(userid) + "\t" + str(result['scores']['universal']) + "\t" + str(result['scores']['english'])
				i = i+1
				fout.write(str(userid) + "\t" + str(result['scores']['universal']) + "\t" + str(result['scores']['english']) + "\n")
			except Exception as e:
				fout.write(str(userid) + "\tNA\tNA\n")
	
		
