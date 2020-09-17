from math import factorial

cadena=str(factorial(100))
suma=0

for letter in cadena:
	suma = suma+int(letter)

print(suma)

	