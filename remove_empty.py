l=[(),(),('',),('a','b'),('a','b','c'),('d')]
ls=[]
for i in l:
	if len(i)!=0:
		ls.append(i)
print(ls)
