#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 13:37:29 2025

@author: sergio
"""

# Importa o módulo csv para trabalhar com arquivos CSV.
import csv
# Importa a classe datetime do módulo datetime para trabalhar com datas.
from datetime import datetime
# Importa funções do matplotlib para plotagem.
from matplotlib import pyplot as plt

#Obtém as datas e as temperaturas máximas do arquivo

# Death Valley csv

# Define o nome do arquivo CSV a ser lido.
filename = 'Dados_csv/death_valley_2014.csv'
# Abre o arquivo CSV.
with open(filename) as f:
    # Cria um objeto para ler o arquivo CSV.
    reader = csv.reader(f)
    # Lê a primeira linha, contendo os cabeçalhos.
    header_row = next(reader)

    # Lista para armazenar a temperatura média e as datas.
    dates_dv, means_dv = [], []
    # Loop pelas linhas restantes do arquivo.
    for row in reader:
        try:
            # Converte a string da primeira coluna para um objeto datetime (data).
            current_date_dv = datetime.strptime(row[0], "%Y-%m-%d")
            # Converte o valor da terceira coluna para inteiro (temperatura máxima).
            mean_dv = int(row[2])
            
        except ValueError:
            print(current_date_dv, 'missing data')
        
        else:
            # Adiciona a data à lista de datas.
            dates_dv.append(current_date_dv)
            # Adiciona a temperatura media à lista.
            means_dv.append(mean_dv)

# Sitka csv

# Define o nome do arquivo CSV a ser lido.
filename = 'Dados_csv/sitka_weather_2014.csv'
# Abre o arquivo CSV.
with open(filename) as f:
    # Cria um objeto para ler o arquivo CSV.
    reader = csv.reader(f)
    # Lê a primeira linha, contendo os cabeçalhos.
    header_row = next(reader)

    # Lista para armazenar as temperaturas máximas, mínimas e as datas.
    dates_s, means_s = [], []
    # Loop pelas linhas restantes do arquivo.
    for row in reader:
        try:
            # Converte a string da primeira coluna para um objeto datetime (data).
            current_date_s = datetime.strptime(row[0], "%Y-%m-%d")
            # Converte o valor da terceira coluna para inteiro (temperatura média).
            mean_s = int(row[2])
            
        except ValueError:
            print(current_date_s, 'missing data')
        
        else:
            # Adiciona a data à lista de datas.
            dates_s.append(current_date_s)
            # Adiciona a temperatura média à lista.
            means_s.append(mean_s)

# Cria a figura para o gráfico.
fig = plt.figure(dpi=128,figsize=(10,6))

# Death Valley

# Plota as temperaturas médias em vermelho escuro.
plt.plot(dates_dv, means_dv, c='red', alpha=1, label='Death Valley (média')

# Stika

# Plota as temperaturas médias em azul escuro.
plt.plot(dates_s, means_s, c='blue', alpha=1, label='Stika (média)')

# Gráfico

plt.legend()

# Define o título do gráfico e os rótulos dos eixos.
plt.title("Daily mean temperatures - 2014\ncomparison between \nDeath Valley \nSitka", fontsize=20)
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