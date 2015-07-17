import zipfile
file=zipfile.ZipFile('channel.zip')
inti='90052'
suf='.txt'
zpp=['90052']
t=[]
print len(file.namelist())
#print file.namelist()[1]
for i in range(909) :
		data=file.read(inti+suf)
		com=file.getinfo(inti+suf).comment
		t.append(com)
		inti=data.rsplit(None,1)[1]
		zpp.append(inti)
print ''.join(t)
