#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 02:03:46 2024

@author: sergio
"""

#While continue
#A instrução 'continue' volta o laço para o início

current_number = 0
while current_number < 10:
    current_number += 1
    if (current_number % 2) == 0: #Se for par
        continue
    print(current_number)