import requests
import pandas as pd
import re
from requests import Request, Session
import time
import csv
import asyncio
import concurrent.futures

#global variables
success = 0
fails = 0
blanks = 0
excepts = 0
failures_url = []
failures_id = []
exceptions_url = []
exceptions_id = []
newlist = []

#clean the data for use
def clean(num_urls):
	for i in num_urls:

		#add counter to track progress in terminal
		#print(i[0])

		#get url
		url0 = str(i[1])

		#check if url exists
		if url0 != '[]' and url0 != 'nan' and url0 is not '' :

			#remove json config
			url1 = url0.replace("\\", "")
			url2 = url1.replace('"', "")
			url3 = url2[1:-1]

			#check if more than one url
			if ',' in url3:
				mylist = url3.split(',')
				for item in mylist:
					newlist.append([item, i[0]])
					#req_url(item, i)
			else:
				newlist.append([url3, i[0]])
				#req_url(url3, i)

		else:
			#blank cell, add to counter
			global blanks
			blanks += 1

def load_url(url):
    return requests.head(url, timeout=2)


#request the json pixel url asynchronously
async def req_url():


	with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
			future_to_url = {executor.submit(load_url, url[0]): url for url in     newlist}
			for future in concurrent.futures.as_completed(future_to_url):
				url = future_to_url[future]
				try:
					data = future.result()
				except Exception as exc:
					global excepts
					excepts += 1
				else:
					#print(data)
					if data.ok:
						global success
						success += 1
					else:
						global fails
						fails += 1
						x = url[1]
						print('Tactic_ID: ' + str(tactics['tactic_id'][x]))
						print('URL: ' + str(url[0]))


#write the results to a csv file
#def results(success, failures_id, failures_url, exceptions_id, exceptions_url):
#	f = open("success2.csv","w+")
#	f.write('%d' % success)
#
#	with open('failures2.csv', 'w') as f:
#	       writer = csv.writer(f, delimiter='\t')
#	       writer.writerow(['Tactic_ID', 'JSON_URL'])
#	       writer.writerows(zip(failures_id,failures_url))
#
#	with open('exceptions2.csv', 'w') as f:
#	       writer = csv.writer(f, delimiter='\t')
#	       writer.writerow(['Tactic_ID', 'JSON_URL'])
#	       writer.writerows(zip(exceptions_id,exceptions_url))

if __name__ == '__main__':

	#get current time
	timenow = time.time()
	tactics = pd.read_csv("tactic.csv")

	#get numbered json urls
	num_urls = enumerate(tactics['impression_pixel_json'][:2500])
	clean(num_urls)
	#print(newlist)

	loop = asyncio.get_event_loop()
	loop.run_until_complete(req_url())
	#results(success, failures_id, failures_url, exceptions_id, exceptions_url)

	#print results
	print('Successes: ' + str(success))
	print('Exceptions: ' + str(excepts))
	print('Fails: ' + str(fails))
	print('Blanks: ' + str(blanks))
	endtime = time.time()

	failures = zip(failures_id,failures_url)
	print(failures)


	#get ending time, print difference to get total run time
	seconds = (timenow - endtime)
	print(seconds)









