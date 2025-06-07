#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 15:42:28 2025

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
filename = 'San_Francisco_2014.csv'
# Abre o arquivo CSV.
with open(filename) as f:
    # Cria um objeto para ler o arquivo CSV.
    reader = csv.reader(f)
    # Lê a primeira linha, contendo os cabeçalhos.
    header_row = next(reader)

    # Lista para armazenar as temperaturas máximas, mínimas e as datas.
    dates, highs, lows = [], [], []
    # Loop pelas linhas restantes do arquivo.
    for row in reader:
        try:
            # Converte a string da primeira coluna para um objeto datetime (data).
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            # Converte o valor da segunda coluna para inteiro (temperatura máxima).
            high = int(row[1])
            # Converte o valor da quarta coluna para inteiro (temperatura mínima).
            low = int(row[3])
            
        except ValueError:
            print(current_date, 'missing data')
        
        else:
            # Adiciona a data à lista de datas.
            dates.append(current_date)
            # Adiciona a temperatura máxima à lista.
            highs.append(high)
            # Adiciona a temperatura mínima à lista.
            lows.append(low)

# Cria a figura para o gráfico.
fig = plt.figure(dpi=128,figsize=(10,6))
# Plota as temperaturas máximas em vermelho.
plt.plot(dates, highs, c='red', alpha=0.5)
# Plota as temperaturas mínimas em azul.
plt.plot(dates, lows, c='blue', alpha=0.5)
# Sombreando a área entre os gráficos
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Define o título do gráfico e os rótulos dos eixos.
plt.title("Daily high and low temperatures - 2014\nSan Francisco, CA", fontsize=20)
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