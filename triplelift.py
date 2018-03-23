import requests
import pandas as pd
import re
from requests import Request, Session
import time
import csv

#global variables
success = 0
fails = 0
blanks = 0
excepts = 0
failures_url = []
failures_id = []
exceptions_url = []
exceptions_id = []

#clean the data for use
def clean(num_urls):
	for i in num_urls:
	
		#add counter to track progress in terminal
		print(i[0])

		#get url
		url0 = str(i[1])

		#check if url exists
		if url0 != '[]' and url0 != 'nan' or None :

			#remove json config
			url1 = url0.replace("\\", "")
			url2 = url1.replace('"', "")
			url3 = url2[1:-1]

			#check if more than one url
			if ',' in url3:
				mylist = url3.split(',')
				for item in mylist:
					req_url(item, i)
			else:
				req_url(url3, i)

		else:
			#blank cell, add to counter
			global blanks
			blanks += 1


#request the json pixel url
def req_url(url3, i):
	try:
		status = requests.get(url3, timeout=1)
		#print(status)
		if status.ok:
			global success
			success += 1
		else:
			global fails
			fails += 1	

			failures_id.append(tactics['tactic_id'][i[0]])
			failures_url.append('"' + url3 + "'")

	except:
		global excepts

		excepts += 1
		exceptions_id.append(tactics['tactic_id'][i[0]])
		exceptions_url.append('"' + url3 + "'")




#write the results to a csv file
def results(success, failures_id, failures_url, exceptions_id, exceptions_url):
	f = open("success1.csv","w+")
	f.write('%d' % success)

	with open('failures1.csv', 'w') as f:
	       writer = csv.writer(f, delimiter='\t')
	       writer.writerow(['Tactic_ID', 'JSON_URL'])
	       writer.writerows(zip(failures_id,failures_url))

	with open('exceptions1.csv', 'w') as f:
	       writer = csv.writer(f, delimiter='\t')
	       writer.writerow(['Tactic_ID', 'JSON_URL'])
	       writer.writerows(zip(exceptions_id,exceptions_url))

if __name__ == '__main__':
	
	#get current time
	timenow = time.time()
	tactics = pd.read_csv("tactic.csv")

	#get numbered json urls
	num_urls = enumerate(tactics['impression_pixel_json'][:50])
	clean(num_urls)
	results(success, failures_id, failures_url, exceptions_id, exceptions_url)

	#print results
	print('Successes: ' + str(success))
	print('Exceptions: ' + str(excepts))
	print('Fails: ' + str(fails))
	print('Blanks: ' + str(blanks))
	endtime = time.time()

	#get ending time, print difference to get total run time
	seconds = (timenow - endtime)
	print(seconds)

	#quit()







