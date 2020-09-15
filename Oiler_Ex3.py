from math import sqrt
'''
The prime factor of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number
600851475143
'''
N=600851475143
Div_N=[]

for t in range(5000000):
	t=t+1
	if N%t==0:
		Div_N.append(t)

print(Div_N)

Div1=[]
Div2=[]

for t in range(2000000):
	t=t+1
	if Div_N[-1]%t==0:
		Div1.append(t)

for t in range(1000000):
	t=t+1
	if Div_N[-2]%t==0:
		Div2.append(t)

print(Div1)
print(Div2)
print(sqrt(6857))
Div3=[]
for t in range(6857):
	t=t+1
	if Div2[-2]%t==0:
		Div3.append(t)
print(Div3)

#Respuesta: 6857
