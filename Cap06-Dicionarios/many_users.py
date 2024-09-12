#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:25:20 2024

@author: sergio
"""
#Dicionário de dicionários
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'},
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'}
    }

#Extrair informações de um dicionário de dicionários
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\nFull name: " + full_name.title())
    print("\nLocation: " + location.title())