#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 21:24:26 2024

@author: sergio
"""

try:
    print(5/0)
except ZeroDivisionError:
    print("You can´t divide by zero!")