import urllib2
response=urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
str='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='


for i in range(0,400):
	html=response.read()
	html1=html.rsplit(None,1)[1]
	print html1
	url1=str+html1
	response=urllib2.urlopen(url1)


	

