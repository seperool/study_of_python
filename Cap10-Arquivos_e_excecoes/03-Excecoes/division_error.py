#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:20:49 2024

@author: sergio
"""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try: #Tentar fazer
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError: #Error
        print("You can't divide by 0!")
    else: #Sucesso
        print(answer)