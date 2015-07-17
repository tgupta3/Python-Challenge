import collections
import re
guts=list(open("ocr.txt").read())
results=collections.Counter(guts) #to get count of each character
print results 
print re.findall(r'[a-z]',"".join(guts)) #find chaaracters a-z in order in guts string
