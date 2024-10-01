#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:02:08 2024

@author: sergio
"""

#Retornando valores de uma função
#Return
#Argumento opcional

def get_formatted_name(first_name,last_name,middle_name=''): #add parâmetro opcional
    """Devolve um nome completo formatado de modo elegante."""
    if middle_name: #middle_name vazio é false (else), e com algo é true (if)
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title() #Retorna valor da função

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker','lee')
print(musician)
