import pickle
import urllib2
response=urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
html=response.read()
data_string=pickle.dumps(html)
data=pickle.loads(html)
print data
for item in data:
	print "".join(i[0] * i[1] for i in item)
