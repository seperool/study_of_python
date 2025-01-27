#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:56:26 2025

@author: sergio
"""

from name_function import get_formatted_name  # Importa função

print("Enter 'q' at any time to quit.")  # Mensagem para sair
while True:  # Loop principal
    first = input("\nPlase give me a first name: ")  # Pede primeiro nome
    if first == 'q':  # Sai se digitar 'q'
        break
    last = input("\nPlase give me a last name: ")  # Pede último nome
    if last == 'q':  # Sai se digitar 'q'
        break
    
    formatted_name = get_formatted_name(first, last)  # Formata o nome
    print("\tNeatly formatted name : " + formatted_name + ".")  
    # Imprime nome formatado