import unittest
import numpy
#from triplelift import req_url
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

class TestMethods(unittest.TestCase):

    #def test_upper(self):
    #    self.assertEqual('foo'.upper(), 'FOO')

    def test_req_url(self):
        url0 = req_url("https://www.google.com/", 1)
        #print(url)
        url1 = req_url("httsdp://google.com/", 1)
        url2 = req_url("https://voken.eyereturn.com/pix?1132530", 1)
        self.assertTrue(url0, 1)
        #self.assertFalse(url1, 1)
        
        #self.assertTrue(url0, 99)
        #self.assertTrue(url1, 99)
        assert url1 != 1
        assert url1 == 99
        assert url2 == -1
        assert url2 != 1

    def test_clean(self):

        url0 = clean([[1,'[]']])
        url1 = clean([[1,'nan']])
        url2 = clean([[1,'']])
        url3 = clean([[1, 'hello']])
        url4 = clean([[1, 'hello, world']])
        #print(url0)
        #url1 = 
        #url2 = 
        #self.assertTrue(url0, 1)
        #self.assertFalse(url1, 1)
        
        #self.assertTrue(url0, 99)
        #self.assertTrue(url1, 99)
        assert url0 == 2
        assert url1 == 2
        assert url2 == 2
        assert url3 == 1
        assert url4 == 0


#clean the data for use
def clean(num_urls):
    for i in num_urls:
    
        #add counter to track progress in terminal
        print(i[0])

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
                    return 0
                    req_url(item, i)
            else:
                return 1
                req_url(url3, i)

        else:
            #blank cell, add to counter
            return 2
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
            return 1
        else:
            global fails
            fails += 1  
            return -1

            failures_id.append(tactics['tactic_id'][i[0]])
            failures_url.append('"' + url3 + "'")

    except:
        global excepts
        return 99

        excepts += 1
        exceptions_id.append(tactics['tactic_id'][i[0]])
        exceptions_url.append('"' + url3 + "'")




if __name__ == '__main__':
    unittest.main()