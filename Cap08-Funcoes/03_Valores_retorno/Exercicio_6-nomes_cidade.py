#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:30:50 2024

@author: sergio
"""

#Função retornando valor

def city_country(city,country):
    full_name = city + ", " + country
    return full_name.title()

local = city_country("madri","espanha")
print(local)
local = city_country("moscow","russia")
print(local)
local = city_country("santiago","chile")
print(local)
