#Importando função do módulo 
#e dando um alias a função

from car import make_car as mk

car = mk('subaru', 'outback', 
           color='blue',
           tow_package=True)
print(car)