f = open('test.csv')
f1 = open('test1.csv','w')
for i in f :
	j = i.strip().split(',')
	
	if '/' in j[-1] :
		a = j[-1].split('/')
		a = sorted(a)
		j[-1] = '/'.join(a)
	k = ','.join(j)
	f1.write(k+"\n")