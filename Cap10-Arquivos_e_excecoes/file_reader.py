#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:18:18 2024

@author: sergio
"""

#Abre arquivo, lê o conteudo e salva numa variável
#with fecha o arquivo depois de usa-lo
#open() abre o arquivo
#'as' salva o conteudo do arquivo no objeto file_object
path_text = 'text_files/pi_digits.txt' #path relativo do arquivo, caminho
with open(path_text) as file_object:
    
    #Lê o conteúdo do arquivo, salva como string
    contents = file_object.read()
    
    #Elimina o caracter em branco do final
    contents = contents.rstrip()
    
    #Confere  tipo da variável, resultado esperado string
    print(type(contents))
    
    #Printa o conteúdo da variável = conteúdo do arquivo
    print(contents)