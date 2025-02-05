#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:14:46 2025

@author: sergio
"""

from city_functions import get_city_country  # Importa a função de formatação

print("Enter 'q' at any time to quit.")  # Mensagem de instrução para sair do loop

while True:  # Loop principal do programa
    city = input("\nPlase give me a city: ")  # Solicita ao usuário o nome de uma cidade
    if city == 'q':  # Verifica se o usuário digitou 'q' para sair
        break  # Sai do loop se o usuário digitar 'q'

    country = input("\nPlase give me a country: ")  # Solicita ao usuário o nome de um país
    if country == 'q':  # Verifica se o usuário digitou 'q' para sair
        break  # Sai do loop se o usuário digitar 'q'
    
    population = input("\nPlase give me the number of population: ")  # Solicita ao usuário o nome de um país
    if country == 'q':  # Verifica se o usuário digitou 'q' para sair
        break  # Sai do loop se o usuário digitar 'q'
    
    formatted_address = get_city_country(city, country, population)  # Chama a função para formatar cidade e país
    print("\tNeatly formatted city and country : " + formatted_address)  # Imprime a cidade e o país formatados