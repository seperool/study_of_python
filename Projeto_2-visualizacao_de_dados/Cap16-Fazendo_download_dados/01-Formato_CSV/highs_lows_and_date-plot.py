#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 21 10:52:10 2025

@author: sergio
"""

# Importa o módulo csv para trabalhar com arquivos CSV.
import csv
# Importa a classe datetime do módulo datetime para trabalhar com datas.
from datetime import datetime
# Importa funções do matplotlib para plotagem.
from matplotlib import pyplot as plt

#Obtém as datas e as temperaturas máximas do arquivo

# Define o nome do arquivo CSV a ser lido.
filename = 'sitka_weather_2014.csv'
# Abre o arquivo CSV.
with open(filename) as f:
    # Cria um objeto para ler o arquivo CSV.
    reader = csv.reader(f)
    # Lê a primeira linha, contendo os cabeçalhos.
    header_row = next(reader)

    # Lista para armazenar as temperaturas máximas.
    dates, highs = [], []
    # Loop pelas linhas restantes do arquivo.
    for row in reader:
        # Converte a string da primeira coluna para um objeto datetime (data).
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        # Adiciona a data à lista de datas.
        dates.append(current_date)
        
        # Converte o valor da segunda coluna para inteiro (temperatura máxima).
        high = int(row[1])
        # Adiciona a temperatura máxima à lista.
        highs.append(high)

# Cria a figura para o gráfico.
fig = plt.figure(dpi=128,figsize=(10,6))
# Plota as temperaturas máximas em vermelho.
plt.plot(dates, highs, c='red')

# Define o título do gráfico e os rótulos dos eixos.
plt.title("Daily high temperatures - 2014", fontsize=24)
# Define o rótulo do eixo x.
plt.xlabel("",fontsize=16)
# Formata as datas no eixo x para melhor visualização.
fig.autofmt_xdate()
# Define o rótulo do eixo y.
plt.ylabel("Temperature (F)",fontsize=16)
# Define o tamanho dos rótulos dos eixos.
plt.tick_params(axis='both',which='major',labelsize=16)

# Exibe o gráfico.
plt.show()