t=(23,45,23,45,34,67,23)
b=[]
for i in t:
	if t.count(i)>1:
		if i not in b:
			b.append(i)
print(b)
		
