#Importando todas as funções de um módulo

from car import *

car = make_car('subaru', 'outback', 
           color='blue',
           tow_package=True)
print(car)