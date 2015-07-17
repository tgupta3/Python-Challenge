import urllib2
import cv2.cv as cv
import cv2
from StringIO import StringIO

#html=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()
#savedFile = open("oxygen.png", 'wb')
#savedFile.write(html)
#savedFile.close()
html1=cv2.imread('oxygen.png')

#cv2.namedWindow('html')
html2=html1[43:52,0:629]
print html2[0,:]
t=[]
for i in range(0,629,7):
		t.append((html2[0,:])[i][0])
		

k=[]
for i in t :
		k.append(chr(i))
print "".join(k)
#output from last step is smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

g=[105, 110, 116, 101, 103, 114, 105, 116, 121]
ans=[]
for i in g :
		print chr(i)
#cv2.imshow('html',html2)
#cv2.waitKey(0)
#cv2.destroyWindow('html')	


