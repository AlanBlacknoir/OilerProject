#Find the largerst palindrome made from the product of two 3-digit
#numebers.
def is_pal(string):

	largo=len(string)
	c1_string=[]
	c2_string=[]
	for t in range(largo):
		c1_string.append(string[-(t+1)])
		c2_string.append(string[t])

	if c1_string==c2_string:

		return True

	else:
		return False

Fpal=[]
n1,n2=999,999
while n1>=100:
	
	while n2>=100:
		prod=str(n1*n2)
		
		Espal=is_pal(prod)
		
		n2=n2-1
		if Espal==True:	
			Fpal.append(n1*(n2+1))

	n1=n1-1
	
	n2=n1
Fpal.sort()
print('maxpalis: ',Fpal[-1])
	


	
				



