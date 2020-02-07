t=()
while 1:
	item =input('enter the item')
	t= t+(item,)
	c=input('do you want another item')
	if c.lower()=='n':
		break
print(t)
	
