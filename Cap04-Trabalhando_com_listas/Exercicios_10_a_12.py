#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:52:09 2024

@author: sergio
"""
my_foods = ["pizza","falafel","carrot cake"]
friend_foods = my_foods[:] #Copia uma fatia (inteira) de lista para outra variável.
old_friend_foods = my_foods #Ambas variáveis apontam pra mesma lista.

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite food are:")
print(my_foods)

print("\nMy friend's favorite food are:")
print(friend_foods)

print("\nMy old friend's favorite food are:")
print(old_friend_foods)

#10)
print("Os três primeiros itens da lista são:")
print(my_foods[:3])

print("Os três itens do meio da lista são:")
print(my_foods[1:4])

print("Os três últimos itens da lista são:")
print(my_foods[-3:])

#11)
pizzas = ["peperoni","calabresa","frango com catupiri"]
friend_pizzas = pizzas[:]

pizzas.append("carne seca com catupiri")
friend_pizzas.append("mussarela")

print("Minhas pizzas favoritas são:")
for pz in pizzas:
    print(pz.title())
print("As pizzas favoritas dos meus amigos são:")
for fpz in friend_pizzas:
    print(fpz.title())

#12)

print("Os três primeiros itens da lista são:")
for food in my_foods[:3]:
    print(food)

print("Os três itens do meio da lista são:")
for food in my_foods[1:4]:
    print(food)

print("Os três últimos itens da lista são:")
for food in my_foods[-3:]:
    print(food)