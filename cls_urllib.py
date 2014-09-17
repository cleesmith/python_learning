import urllib.request
# GET:
# x = urllib.request.urlopen('http://www.google.com')
# print(x.read())

import urllib.parse
# POST:
#url = 'http://pythonprogramming.net'
#values = {'s':'basic', 'submit':'search'}
#data = urllib.parse.urlencode(values)
#data = data.encode('utf-8')
#req = urllib.request.Request(url,data)
#resp = urllib.request.urlopen(req)
#resp_data = resp.read()
#print(resp_data)

# 403 forbidden:
#try:
#  x = urllib.request.urlopen('https://www.google.com/search?q=test')
#  print(x.read())
#except Exception as e:
#  print(str(e))

# avoid 403 by using headers:
try:
  url = 'https://www.google.com/search?q=test'
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request(url, headers = headers)
  resp = urllib.request.urlopen(req)
  respData = resp.read()
  saveFile = open('withHeaders.txt','w')
  saveFile.write(str(respData))
  saveFile.close()
except Exception as e:
  print(str(e))
                                                
