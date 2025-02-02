#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:08:15 2025

@author: sergio
"""

import unittest  # Importa a biblioteca unittest para testes

from name_function import get_formatted_name  # Importa a função que será testada

class NameTestCase(unittest.TestCase):  # Define uma classe para os casos de teste, herdando de unittest.TestCase
    """Testes para 'name_function.py'"""  # Docstring da classe, descrevendo o propósito dos testes

    def test_first_last_name(self):  # Define um método de teste para nomes com primeiro e último nome
        """Nomes como 'janis joplin' funcionam?"""  # Docstring do método, explicando o caso de teste específico
        formatted_name = get_formatted_name('janis', 'joplin')  # Chama a função com um nome de exemplo
        self.assertEqual(formatted_name, 'Janis Joplin')  # Verifica se o resultado formatado é o esperado

    def test_first_last_middle_name(self):  # Define um método de teste para nomes com primeiro, do meio e último nome
        """Nomes como 'Wolfgang Amadeus Mozart' funcionam?"""  # Docstring do método, explicando o caso de teste
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')  # Chama a função com um nome de exemplo
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')  # Verifica se o resultado formatado é o esperado

unittest.main()  # Executa os testes definidos na classe