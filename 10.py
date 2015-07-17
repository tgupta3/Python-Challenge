a = [1,11,21,1211]
c=[]
temp=[]
for i in range(3,33) :
		digit_str=str(a[i])
		c=list(digit_str)
		par_digit=1
		par_num=[]
		temp=[]
		cont_loop=0
		for i in range(len(c)-1) :
			if( c[i]==c[i+1]) :
				par_digit+=1
				cont_loop+=1
				par_num=int((str(par_digit))+c[i])
				if(cont_loop>1):
					temp[-1]=par_num
				else :
					temp.append(par_num)		

					
				#print par_num
			elif(i>0 and c[i]==c[i-1]) :
				par_digit=1
				cont_loop=0
				i+=1
			else :
				par_digit=1
				cont_loop=0
				par_num=int((str(par_digit))+c[i])
				temp.append(par_num)
				
				
		if(c[i]!=c[i-1] and cont_loop==0):
			par_digit=1
			par_num=int((str(par_digit))+c[i])
			temp.append(par_num)
		
				
		num = int(''.join(map(str,temp)))	
		a.append(num)	
				
print len(str(a[30]))

# solution provided 

import re
def describe(s):
    return "".join([str(len(m.group(0))) + m.group(1)
                    for m in re.finditer(r"(\d)\1*", s)])
s = "1"
for dummy in range(30):
    s = describe(s)
print len(s)  # prints 5808			
			
		
				
				
				

		
		
