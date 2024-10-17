#Importando um módulo 
#e dando um alias ao módulo

import car as c

car = c.make_car('subaru', 'outback', 
           color='blue',
           tow_package=True)
print(car)