#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:24:35 2024

@author: sergio
"""

#1)
car = 'subaru'
print("Is car == 'subaru'? I predict 'True'.")
print(car == 'subaru')

#2)
print("\nIs car == 'audi'? I predict 'False'.")
print(car == 'audi')

#3
num = 21
print("\nIs num < 70? I predict 'True'.")
print(num < 70)

#4
num2 = 45
print("\nIs num == num2? I predict 'False'.")
print(num == num2)

#5
print("\nIs num > 20 and num2 == 45? I predict 'True'.")
print((num > 20) and (45 == num2))

#6
print("\nIs num < 20 or num2 == 45? I predict 'True'.")
print((num < 20) or (45 == num2))

#7
print("\nIs num < 20 or num2 != 45? I predict 'False'.")
print((num < 20) or (45 != num2))

#8
print("\nIs num >= 20 and car == 'audi'? I predict 'False'.")
print((num >= 20) and (car == 'audi'))

#9
print("\nIs num != 'audi'? I predict 'True'.")
print(num != 'audi')

#10
print("\nIs num == 'audi'? I predict 'False'.")
print(num == 'audi')
