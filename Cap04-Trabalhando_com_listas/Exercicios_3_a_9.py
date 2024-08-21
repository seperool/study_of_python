#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:14:57 2024

@author: sergio
"""

#3)

counts = []
for count in range(1,21):
    counts.append(count)
print(counts)


#4)
counts = [] 
for count in range(1,1000001):
    counts.append(count)
print(counts)

#5)
min(counts)
max(counts)
sum(counts)

#6)
imps = []
for imp in range(1,20,2):
    imps.append(imp)
print(imps)

#7)
mults_3=[]
for mult in range(3,31,3):
    mults_3.append(mult)
print(mults_3)

#8)
cubos=[]
for cubo in range(1,11):
    cubos.append(cubo**3)
print(cubos)

#9)
cubos = [cubo**3 for cubo in range(1,11)]
print(cubos)