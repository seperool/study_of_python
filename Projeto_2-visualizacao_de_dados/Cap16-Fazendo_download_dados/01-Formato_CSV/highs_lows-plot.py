#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 14 18:08:29 2025

@author: sergio
"""

# Importa o módulo csv para trabalhar com arquivos CSV.
import csv
# Importa funções do matplotlib para plotagem.
from matplotlib import pyplot as plt

# Define o nome do arquivo CSV a ser lido.
filename = 'sitka_weather_07-2014.csv'
# Abre o arquivo CSV.
with open(filename) as f:
    # Cria um objeto para ler o arquivo CSV.
    reader = csv.reader(f)
    # Lê a primeira linha, contendo os cabeçalhos.
    header_row = next(reader)

    # Lista para armazenar as temperaturas máximas.
    highs = []
    # Loop pelas linhas restantes do arquivo.
    for row in reader:
        # Converte o valor da segunda coluna para inteiro (temperatura máxima).
        high = int(row[1])
        # Adiciona a temperatura máxima à lista.
        highs.append(high)

    # Imprime a lista de temperaturas máximas.
    print(highs)

# Cria a figura para o gráfico.
fig = plt.figure(dpi=128,figsize=(10,6))
# Plota as temperaturas máximas em vermelho.
plt.plot(highs, c='red')

# Define o título do gráfico e os rótulos dos eixos.
plt.title("Daily high temperatures, July 2014", fontsize=24)
# Define o rótulo do eixo x.
plt.xlabel("",fontsize=16)
# Define o rótulo do eixo y.
plt.ylabel("Temperature (F)",fontsize=16)
# Define o tamanho dos rótulos dos eixos.
plt.tick_params(axis='both',which='major',labelsize=16)

# Exibe o gráfico.
plt.show()