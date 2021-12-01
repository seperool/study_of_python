bicycles=['trek','cannondale','redline','specialized']
print (bicycles)
print (bicycles[0].title()) #acessando primeiro elemento da lista, lista começa no indice "0"
print (bicycles[-1].title())  #acessando ultimo elemento da lista de fora rápida
message = "My first bicycle was a " + bicycles[0].title()+"." #concatenando mensagem com o uso de lista
print (message)
bicycles.append('ducati') #adicionando elemento no final da lista
print (bicycles)
bicycles.insert(2,'honda') #adicionando elemento da posição qualquer (2)
print (bicycles)
del bicycles[2] #deleta elemento da posição qualquer (2)
print (bicycles)
popped_bicycles = bicycles.pop(-1) #.pop() remove valor e deixar armazenar numa variavel o valor removido
print (bicycles)
message = 'Value remove was ' + popped_bicycles+"."
print (message)
too_expensive = 'specialized'
bicycles.remove(too_expensive) #remove elemento da lista pelo valor.
message = 'Too expensive for me ' + too_expensive.title()+"."
print (message)
print (bicycles)
bicycles.sort() #organiza a lista em ordem alfabetica
message='\n\n\nLista em ordem alfabetica:'
print(message)
print(bicycles)
bicycles.sort(reverse=True) #organiza a lista em ordem alfabetica inversa
message='\nLista em ordem alfabetica reversa:'
print(message)
print(bicycles)

cars=['toyota','subaru','bmw','audi']
message = '\n\n\n\nNova lista "cars":'
print (message)
print (cars)
message = '\nLista em ordem alfabetica:'
print (message)
print (sorted(cars)) #altera a organização de forma temporaria, organiza em ordem alfabetica
message = '\nLista em ordem alfabetica reversa:'
print (message)
print (sorted(cars,reverse=True)) #altera a organização de forma temporaria, organiza em ordem alfabetica reversa
message = '\nLista ordem original:'
print (message)
print (cars)
message = '\nLista invertida:'
print (message)
cars.reverse()
print (cars) #inverte a ordem dos elementos da lista de forma permanente

size_list = len (cars) #devolve o tamanho da lista
message = '\n\n\nNumero de elementos da lista (tamanho) "cars" é: ' + str(size_list)+ "."
print (message)
