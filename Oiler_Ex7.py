#calcular el primo numero 1001
from math import sqrt, floor
primo=3
indice=2
#Saber si un número es primo
def is_prime(num):
	rnum=floor(sqrt(num))
	counter=0
	t=0
	while counter==0 and t<=rnum:
		t=t+1
		if num%t==0:
			if t==1:
				s=0
			else:
				counter=counter+1
				return False
	

	if counter==0:
		return True


nimpar=primo

while indice!=10001:
	nimpar=nimpar+2
	if is_prime(nimpar)==False:
		x=0
	else:
		primo=nimpar
		indice=indice+1
print('numero ',primo,' ','indice ',indice)


	


		








