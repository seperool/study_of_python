alien_0 = {'color':'green',
           'points':5,
           'x_position':0,
           'y_position':25,
           'speed':'slow'}

print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

#Move o alienigena para a direita
#Determina a distância que o alienigena deve se deslocar de acordo com sua
#velocidade atual

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#Nova posição do alienigena
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: "+
      str(alien_0['x_position']))