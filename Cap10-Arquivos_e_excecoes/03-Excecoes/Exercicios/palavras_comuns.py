#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:56:16 2024

@author: sergio
"""

#Definição da função
def count_words (filename,word):
    """Conta quantas vezes aparece determinada palavra no texto."""
    try:
        with open(filename) as f_obj: #Abre arquivo
            contents = f_obj.read() #Salva conteudo do arquivo na variável contents
    except FileNotFoundError: #Tratamento de erro
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        #Conta o número aproximado de palavras no arquivo
        num_words = contents.lower().count(word) #Conta o número de palavras 'the'
        print(f"The file {filename} has about {num_words} words '{word}'.")

#Parâmetros
filename = "siddhartha.txt"
word = 'the'

#Chamada da função
count_words(filename,word)