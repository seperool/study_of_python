#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:08:15 2025

@author: sergio
"""

import unittest  # Importa biblioteca de testes
from name_function import get_formatted_name  # Importa função

class NameTestCase(unittest.TestCase):  # Cria classe de teste
  """Testes para 'name_function.py'"""  # Docstring da classe de teste

  def test_first_last_name(self):  # Define um método de teste
    """Nomes como 'janis joplin' funcionam?"""  # Docstring do método de teste
    formatted_name = get_formatted_name('janis', 'joplin')  # Chama função para formatar nome
    self.assertEqual(formatted_name, 'Janis Joplin')  # Verifica se o nome formatado está correto

unittest.main()  # Executa os testes