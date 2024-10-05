#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:54:19 2024

@author: sergio
"""

#função com while

def get_formatted_name(first_name,last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nPlaese tell me your name? ")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")