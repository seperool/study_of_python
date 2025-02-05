#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:10:15 2025

@author: sergio
"""

def get_city_country(city, country, population=''):
    """Retorna uma string formatada com o nome da cidade, país e população (opcional).

    Args:
        city: O nome da cidade (string).
        country: O nome do país (string).
        population: A população da cidade (inteiro ou string, opcional).

    Returns:
        Uma string formatada contendo "Cidade, País" ou "Cidade, País - população X",
        com a capitalização correta.
    """
    
    if population:  # Verifica se o argumento population foi fornecido
        address = city + ", " + country + " - população " + str(population)  # Concatena cidade, país e população
    else:  # Se population não foi fornecido
        address = city + ", " + country + "."  # Concatena cidade e país
    return address.title()  # Capitaliza a string resultante (primeira letra de cada palavra)