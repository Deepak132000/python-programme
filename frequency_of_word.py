a=input()
k=''
for i in a:
	b=a.count(i)
	if i not in k:
		k+=i
		print(i,':',b)

