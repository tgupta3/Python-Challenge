import string 
str=list(raw_input("Enter the string: "))
str1="".join(str)

for co,i in enumerate(str):
	if i=='y' :
		str[co]='a'
	elif i=='z' :
		str[co]='b'
	elif i==' ' or i=='.' :
		str[co]=i
	else :
		str[co]=chr(ord(i)+2)  #ord return ascii value, chr converts it back to text */
	
print("".join(str))
	
	#alternative way

intab='abcdefghijklmnopqrstuvwxyz'
outtab='cdefghijklmnopqrstuvwxyzab'
transtab=string.maketrans(intab,outtab) # geneartes a table to map a->c, b->d
print str1.translate(transtab)    #translates the table into string
		


