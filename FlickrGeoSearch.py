#!/usr/bin/env python

import sys
import flickrapi
from lxml import etree
import time

api_key = u'key'
api_secret = u'secret'

import re

def cleanhtml(raw_html):
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  return cleantext


def main():

	reload(sys)
	sys.setdefaultencoding('utf-8')
	
	bbox = "29.23,-11.76,40.5,-1" #tanzania "21,59.8,28,68" #finland
			
	flickr = flickrapi.FlickrAPI(api_key, api_secret)
	ts = 1514851200

	with open("photos.dat", "wt") as photosfile:

		with open("comments.dat", "wt") as commentsfile:

			while ts > 1325376000 :

				page = 1
				done = False
		
				while not done:

					searched = False
					while not searched:
						try:
							result = flickr.photos.search(per_page=250, page=page, bbox=bbox, max_upload_date=ts-1, min_upload_date=ts-24*60*60)
							print str(len(result[0])+250*(page-1)) +" / " + result[0].get("total") + "  " + str(ts)
							searched=True
						except:
							print "search error"
							time.sleep(1)
					write = True
					if len(result[0]) < 250 :
						write = True
						done = True
					else :
						if page > 1:
							if result[0][0].get("id") == prevresult[0][0].get("id"):
								done = True
								write = False
					if write :
						for photo in result[0]:
							photoid = photo.get("id")
							owner = photo.get("owner")
							try:
								comments = flickr.photos.comments.getList(photo_id = photoid)[0]
								originalurl = ""
								info = flickr.photos.getInfo(photo_id = photoid)
								tsn = int(info[0].get("dateuploaded"))
			
								if len(comments) > 0 :
									sizes = flickr.photos.getSizes(photo_id = photoid)
									sizesdic = dict()
									for child in sizes.iter() :
										if child.tag == "size":
											sizesdic[child.get("label")] = child.get("url")
									if sizesdic.get("Original",-1) != -1:
										originalurl =  sizesdic.get("Original")
									else:
										if sizesdic.get("Large",-1) != -1:
											originalurl =  sizesdic.get("Large")
										else:
											if sizesdic.get("Medium",-1) != -1:
												originalurl =  sizesdic.get("Medium")
											else:
												if sizesdic.get("Small",-1) != -1:
													originalurl =  sizesdic.get("Small")


									i = 0	
									for child in comments.iter():
										if child.tag == 'comment':
											text = cleanhtml(child.text.replace("\t", " ").replace("\n"," ").replace("\r", " "))
											commentid = comments[i].get("id")
											author = comments[i].get("author")
											date = comments[i].get("datecreate")
											i = i+1
											commentsfile.write(commentid + "\t" + photoid + "\t" + author + "\t" + date + "\t\"" + text + "\"\n")
								photosfile.write(photoid + "\t" + owner + "\t" + originalurl+ "\t" + str(len(comments)) + "\t" + str(tsn) +"\n")												

							except:
								print "missing photo " + photoid
					prevresult = result
					page = page + 1
				ts = ts-24*60*60

if __name__ == '__main__':
	main()
 
 
