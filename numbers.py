for value in range(1,11): # range(), gera uma serie de numeros, mas para antes do ultimo, no caso o 11
	print (value)

numbers = list(range(1,11)) #list(), cria uma lista
print (numbers)

event_numbers = list(range(2,20,3)) #range(numero incial, numero final, espaço entre numeros)
print (event_numbers)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print ("\nValores quadros:")
print (squares)

fsquares = []
for value in range(1,11):  #forma consisa da mesma formula
	fsquares.append(value**2)
print (fsquares)


squares = [value**2 for value in range(1,11)] #forma em "list comprehensions"
print (squares)

digits = [1,2,3,4,5,6,7,8,9,0]
m=min(digits)
ma=max(digits)
soma=sum(digits)
print ('\n\nLista numerica:')
print (digits)
print ('\nValor minimo da lista:'+ str(m))
print ('\nValor maximo da lista:'+ str(ma))
print ('\nValor da soma dos valores da lista:'+ str(soma))

soma_mao = 0
for valor in digits:
	soma_mao = valor + soma_mao
print ('Confirmando o valor da soma (na mão):'+str(soma))
