#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 14:01:42 2025

@author: sergio
"""

# Importa o módulo json para trabalhar com dados JSON.
import json

# Define o nome do arquivo JSON a ser lido.
filename = 'population_data.json'
# Abre o arquivo em modo de leitura ('as f') e carrega seu conteúdo JSON.
with open(filename) as f:
    pop_data = json.load(f)
    
# Itera sobre cada dicionário de dados de população na lista.
for pop_dict in pop_data:
    # Verifica se o ano no dicionário é '2010'.
    if pop_dict['Year'] == '2010':
        # Obtém o nome do país.
        country_name = pop_dict['Country Name']
        
        # Obtém o valor da população.
        population = int(float(pop_dict['Value']))
        #O Python não consegue converter de string com float para int.
        #É necessário converter primeiro de string para float,
        #e por fim, converter float para int. 
        
        # Imprime o nome do país e sua população.
        print(country_name + ': ' + str(population))