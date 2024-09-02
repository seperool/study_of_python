#3)
alien_color = 'green'
if alien_color == 'green':
    print("The player gained 5 points!")
if alien_color == 'yellow':
    print("The player gained 10 points!")

#4)
##Versão 1
alien_color = 'green'
if alien_color == 'green':
    print("The player gained 5 points!")
if alien_color != 'green':
    print("The player gained 10 points!")

##Versão 2
alien_color = 'green'
if alien_color == 'green':
    print("The player gained 5 points!")
else:
    print("The player gained 10 points!")

#5)
alien_color = 'green'
if alien_color == 'green':
    print("Green alien. The player gained 5 points!")
elif alien_color == 'yellow':
    print("Yellow alien. The player gained 10 points!")
elif alien_color == 'red':
    print("Red alien. The player gained 15 points!")

#6)
age = 12
if age < 2:
    print("Você é um bebe!")
elif age < 4:
    print("Você é uma criança!")
elif age < 13:
    print("Você é um(a) garoto(a)!")
elif age < 20:
    print("Você é um(a) adolecente!")
elif age < 65:
    print("Você é um adulto!")
else:
    print("Você é um idoso(a)!")

#7)
favorite_fruits = ['banana','maçã','pêra']
if 'banana' in favorite_fruits:
    print("Você realmente gosta de bananas!")
if 'maçã' in favorite_fruits:
    print("Você realmente gosta de maçãs!")
if 'pêra' in favorite_fruits:
    print("Você realmente gosta de pêras!")
if 'uva' in favorite_fruits:
    print("Você realmente gosta de uvas!")
if 'guarana' in favorite_fruits:
    print("Você realmente gosta de guaranas!")