#!/usr/bin/python
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

finname = sys.argv[1]
foutname = sys.argv[2]

with open(foutname, "wt") as out_file: 
	with open(finname, "rt") as data_file: 
        for tweetline in data_file:
            data = json.loads(tweetline)
            tweetid = str(data["id"])
            out_file.write(tweetid + '\n')
