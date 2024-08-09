#criando dicionario chamado alien_0 e adicionando chaves-valor
alien_0={'points': 5}
alien_0['x_position']=0
alien_0['y_position']=25
alien_0['color']='green'
alien_0['speed']='medium'
print ('alien 0 is:'+ str(alien_0))
print ('\n\n\nthe alien 0 color is: '+str(alien_0['color']))
print ('the alien 0 ponts is: '+str(alien_0['points']))
print ('the alien 0 speed is: '+str(alien_0['speed']))
print ('the alien 0 position in "x" is: '+str(alien_0['x_position']))
print ('the alien 0 position in "y" is: '+str(alien_0['y_position']))

alien_0['speed']='fast'	#alterando uma chave valor
del alien_0['points']	#apagando uma chave-valor
print ('\n\n\nthe new alien 0 is:'+ str(alien_0)+'\n\n\n')

#uma lista de dicionarios
aliens =[]
for alien_num in range(0,30):
	new_alien = {'color': 'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
for alien in aliens[0:5]:
	print (alien)
print ('\n\nNumero total de aliens = '+str(len(aliens)))
