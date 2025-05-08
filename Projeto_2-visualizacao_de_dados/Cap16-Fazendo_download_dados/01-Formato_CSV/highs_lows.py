#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  8 02:07:07 2025

@author: sergio
"""

# Importa o módulo para trabalhar com arquivos CSV.
import csv

# Define o nome do arquivo.
filename = 'sitka_weather_07-2014.csv'
# Abre o arquivo CSV.
with open(filename) as f:
    # Cria um objeto para ler o CSV.
    reader = csv.reader(f)
    # Lê a linha de cabeçalho.
    header_row = next(reader)
    # Imprime o cabeçalho.
    print(header_row)