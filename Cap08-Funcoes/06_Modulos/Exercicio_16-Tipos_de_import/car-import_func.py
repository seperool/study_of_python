#Importando função do módulo

from car import make_car

car = make_car('subaru', 'outback', 
           color='blue',
           tow_package=True)
print(car)