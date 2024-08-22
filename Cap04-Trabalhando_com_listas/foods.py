#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:30:16 2024

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
