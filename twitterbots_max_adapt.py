#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:00:01 2018

@author: maxpe
"""

import sys
import botometer

mashape_key = ""
twitter_app_auth = {
	'consumer_key': '',
	'consumer_secret': ''
}

bom = botometer.Botometer(wait_on_ratelimit=True, mashape_key=mashape_key, **twitter_app_auth)

# provide file that contains one twitter userid per line
finname = "/home/mpellert/bots/ensample.old"

# name of file to write output to
foutname = "/home/mpellert/bots/ensample.old_checked"


print("all set")

i = 1
with open(finname, "rt") as fin:
	with open(foutname, "wt",1) as fout:
		fout.write("id\tuniversalScore\tenglishScore\n")
		for line in fin: 
			userid = line.strip()
			try:
				result = bom.check_account(userid)
#				print(str(i) +"\t" + str(userid) + "\t" + str(result['scores']['universal']) + "\t" + str(result['scores']['english']))
#				i = i+1
				fout.write(str(userid) + "\t" + str(result['scores']['universal']) + "\t" + str(result['scores']['english']) + "\n")
			except Exception as e:
				fout.write(str(userid) + "\t" + "Error: " + str(e) + "\t" + "Error: " + str(e) + "\n")
