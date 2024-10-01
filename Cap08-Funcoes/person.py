#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:08:07 2024

@author: sergio
"""

#Função
#Retornando um dicionário

def build_person(first_name,last_name,age=''):
    """Devolve um dicionário com informações sobre uma pessoa."""
    person = {'first':first_name,'last':last_name}
    if age: #Se age não vazio, então True, logo adiciona ao dicionário
        person['age']=age
    return person

musician = build_person('jimi', 'hendrix',age=27)
print(musician)