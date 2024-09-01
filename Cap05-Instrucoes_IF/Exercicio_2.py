#Testando condicionais.
#1)
car_1 = 'audi'
car_2 = 'maserati'
print("A expressão testada é car_1 == car_2, o resultado esperado é 'False'")
print(car_1 == car_2)
print("\nA expressão testada é car_1 != car_2, o resultado esperado é 'True'")
print(car_1 != car_2)

#2)
car_3 = 'AUDI'
print("\nA expressão testada é car_1 == car_3, o resultado esperado é 'True'")
print(car_1 == car_3.lower())

#3)
year2 = 2019
year1 = 1981
year3 = 2022
print("\nA expressão testada é year1 == year3, o resultado esperado é 'False'")
print(year1 == year3)
print("\nA expressão testada é year1 != year2, o resultado esperado é 'True'")
print(year1 != year2)
print("\nA expressão testada é year3 > year2, o resultado esperado é 'True'")
print(year3 > year2)
print("\nA expressão testada é year2 < year3, o resultado esperado é 'True'")
print(year2 < year3)
print("\nA expressão testada é year1 >= year3, o resultado esperado é 'False'")
print(year1 >= year3)
print("\nA expressão testada é year2 <= year1, o resultado esperado é 'False'")
print(year2 <= year1)

#4)
print("\nAs expressões testadas são (year1 == year3) or (year3 > year1), o resultado esperado é 'True'")
print((year1 == year3) or (year3 > year1))
print("\nA expressão testada é (year1 == year3) and (year3 > year1), o resultado esperado é 'False'")
print((year1 == year3) and (year3 > year1))

#5)
cars = ['audi','maserati','ford']
print("\nVerificando se 'audi' esta contido na lista cars, resultado esperado 'True'")
print('audi' in cars)

#6)
print("\nVerificando se 'ferrari' não esta contido na lista cars, resultado esperado 'True'")
print('ferrari' not in cars)