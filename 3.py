import re
str=open("3.txt").read()
str1='aABCaDEFgdsg'
print re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',str) #brackets for grouping
