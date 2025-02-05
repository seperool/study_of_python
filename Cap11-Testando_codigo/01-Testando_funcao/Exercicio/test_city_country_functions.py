#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:20:31 2025

@author: sergio
"""

import unittest  # Importa o módulo unittest para a criação de testes

from city_functions import get_city_country  # Importa a função que será testada

class City_and_Country_TestCase(unittest.TestCase):  # Define uma classe de teste que herda de unittest.TestCase
    """Testes para a função get_city_country."""

    def test_city_and_country(self):  # Define um método de teste
        """Testa a formatação de cidade e país sem população."""
        formatted_address = get_city_country("santiago", "chile")  # Chama a função com dados de exemplo
        self.assertEqual(formatted_address, "Santiago, Chile.")  # Verifica se o resultado é o esperado
    
    def test_city_country_and_population(self):  # Define um método de teste
        """Testa a formatação de cidade, país e população."""
        formatted_address = get_city_country("santiago", "chile", 500000)  # Chama a função com dados de exemplo, incluindo a população
        self.assertEqual(formatted_address, "Santiago, Chile - População 500000")  # Verifica se o resultado é o esperado, incluindo a população

unittest.main()  # Executa os testes