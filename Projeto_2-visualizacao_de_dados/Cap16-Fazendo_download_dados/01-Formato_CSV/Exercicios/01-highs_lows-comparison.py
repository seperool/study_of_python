#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 15:20:35 2025

@author: sergio
"""

# Importa o módulo csv para trabalhar com arquivos CSV.
import csv
# Importa a classe datetime do módulo datetime para trabalhar com datas.
from datetime import datetime
# Importa funções do matplotlib para plotagem.
from matplotlib import pyplot as plt

#Obtém as datas e as temperaturas máximas do arquivo

# San Francisco csv

# Define o nome do arquivo CSV a ser lido.
filename = 'Dados_csv/san_francisco_2014.csv'
# Abre o arquivo CSV.
with open(filename) as f:
    # Cria um objeto para ler o arquivo CSV.
    reader = csv.reader(f)
    # Lê a primeira linha, contendo os cabeçalhos.
    header_row = next(reader)

    # Lista para armazenar as temperaturas máximas, mínimas e as datas.
    dates_sf, highs_sf, lows_sf = [], [], []
    # Loop pelas linhas restantes do arquivo.
    for row in reader:
        try:
            # Converte a string da primeira coluna para um objeto datetime (data).
            current_date_sf = datetime.strptime(row[0], "%Y-%m-%d")
            # Converte o valor da segunda coluna para inteiro (temperatura máxima).
            high_sf = int(row[1])
            # Converte o valor da quarta coluna para inteiro (temperatura mínima).
            low_sf = int(row[3])
            
        except ValueError:
            print(current_date_sf, 'missing data')
        
        else:
            # Adiciona a data à lista de datas.
            dates_sf.append(current_date_sf)
            # Adiciona a temperatura máxima à lista.
            highs_sf.append(high_sf)
            # Adiciona a temperatura mínima à lista.
            lows_sf.append(low_sf)

# Death Valley csv

# Define o nome do arquivo CSV a ser lido.
filename = 'Dados_csv/death_valley_2014.csv'
# Abre o arquivo CSV.
with open(filename) as f:
    # Cria um objeto para ler o arquivo CSV.
    reader = csv.reader(f)
    # Lê a primeira linha, contendo os cabeçalhos.
    header_row = next(reader)

    # Lista para armazenar as temperaturas máximas, mínimas e as datas.
    dates_dv, highs_dv, lows_dv = [], [], []
    # Loop pelas linhas restantes do arquivo.
    for row in reader:
        try:
            # Converte a string da primeira coluna para um objeto datetime (data).
            current_date_dv = datetime.strptime(row[0], "%Y-%m-%d")
            # Converte o valor da segunda coluna para inteiro (temperatura máxima).
            high_dv = int(row[1])
            # Converte o valor da quarta coluna para inteiro (temperatura mínima).
            low_dv = int(row[3])
            
        except ValueError:
            print(current_date_dv, 'missing data')
        
        else:
            # Adiciona a data à lista de datas.
            dates_dv.append(current_date_dv)
            # Adiciona a temperatura máxima à lista.
            highs_dv.append(high_dv)
            # Adiciona a temperatura mínima à lista.
            lows_dv.append(low_dv)

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
    dates_s, highs_s, lows_s = [], [], []
    # Loop pelas linhas restantes do arquivo.
    for row in reader:
        try:
            # Converte a string da primeira coluna para um objeto datetime (data).
            current_date_s = datetime.strptime(row[0], "%Y-%m-%d")
            # Converte o valor da segunda coluna para inteiro (temperatura máxima).
            high_s = int(row[1])
            # Converte o valor da quarta coluna para inteiro (temperatura mínima).
            low_s = int(row[3])
            
        except ValueError:
            print(current_date_s, 'missing data')
        
        else:
            # Adiciona a data à lista de datas.
            dates_s.append(current_date_s)
            # Adiciona a temperatura máxima à lista.
            highs_s.append(high_s)
            # Adiciona a temperatura mínima à lista.
            lows_s.append(low_s)

# Cria a figura para o gráfico.
fig = plt.figure(dpi=128,figsize=(10,6))

# San Francisco

# Plota as temperaturas máximas em vermelho escuro.
plt.plot(dates_sf, highs_sf, c='red', alpha=1, label='San Francisco (máx)')
# Plota as temperaturas mínimas em vermelho claro.
plt.plot(dates_sf, lows_sf, c='red', alpha=0.5, label='San Francisco (mín)')

# Death Valley

# Plota as temperaturas máximas em azul escuro.
plt.plot(dates_dv, highs_dv, c='blue', alpha=1, label='Death Valley (máx)')
# Plota as temperaturas mínimas em azul claro.
plt.plot(dates_dv, lows_dv, c='blue', alpha=0.5, label='Death Valley (mín)')

# Stika

# Plota as temperaturas máximas em amarelo escuro.
plt.plot(dates_s, highs_s, c='yellow', alpha=1, label='Stika (máx)')
# Plota as temperaturas mínimas em amarelo claro.
plt.plot(dates_s, lows_s, c='yellow', alpha=0.5, label='Stika (mín)')

# Gráfico

plt.legend()

# Define o título do gráfico e os rótulos dos eixos.
plt.title("Daily high and low temperatures - 2014\ncomparison between \nSan Francisco \nDeath Valley \nSitka", fontsize=20)
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