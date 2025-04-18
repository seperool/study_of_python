#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 20:12:35 2024

@author: sergio
"""

def count_words(filename):
    """Conta o número aproximado de palavras em um arquivo."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass #Falhando silenciosamente
    else:
        #Conta o número aproximado de palavras no arquivo
        words = contents.split() # Cria uma lista com as palavras do texto
        num_words = len(words) # Conta o número de palavras
        print(f"The file {filename} has about {num_words} words.")
    
filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)