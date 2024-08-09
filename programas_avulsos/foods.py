my_foods=['pizza','falafel','carrot cake']
friend_foods = my_foods[:] #copia da lista, porem listas diferentes
my_foods.append('cannoli')
friend_foods.append('ice cream')

print ('My favorite foods are:')
print (my_foods)

print ("\nMy friend's favorite foods are:")
print (friend_foods)

itens=0
for n in range(0,len(my_foods)):
	if my_foods[n] == friend_foods[n]:
		itens=itens+1

if itens == len(my_foods):
	print ('\nListas iquais')
else:
	print ('\nListas diferentes')

girlfriend_food = my_foods #as duas variaveis apontam para a mesma lista
my_foods.append('cannoli')
girlfriend_food.append('ice cream')

print ('\n\n\n\nMy favorite foods are:')
print (my_foods)

print ('\nMy girlfriend favorite foods are:')
print (girlfriend_food)

itens2 = 0
for n in range(0,len(my_foods)):
	if my_foods[n] == girlfriend_food[n]:
		itens2 = itens2+1

if itens2 == len(my_foods):
	print ('\nListas iquais')
else:
	print ('\nListas diferentes')
