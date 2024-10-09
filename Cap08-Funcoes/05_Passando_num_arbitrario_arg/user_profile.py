#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:52:27 2024

@author: sergio
"""

#Argumentos arbitrários e nomeados (dicionário)

def build_profile(first,last,**user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre o usuário."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items(): #percorre o dicionário parâmetro
        profile[key] = value #Add keys e value do parâmetro no dicionário criado da função
    return profile #Retorna o dicionário criado

user_profile = build_profile('albert', 'einstein', 
                             location = 'princeton',
                             field = 'physics')
print(user_profile)