#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 04:51:15 2024

@author: sergio
"""

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if (number % 2) == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")