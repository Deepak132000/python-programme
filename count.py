l=[1,5,3,5,6,(),5,43]
count=0
for i in l:
	if type(i)!=tuple:
		count+=1
	else:
		break
print(count)
