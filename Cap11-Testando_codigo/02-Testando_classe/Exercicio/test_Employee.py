#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:08:11 2025

@author: sergio
"""

import unittest  # Importa a biblioteca de testes unitários

from Employee import Employee  # Importa a classe Employee do arquivo Employee.py

class testEmployee(unittest.TestCase):  # Define a classe de teste que herda de unittest.TestCase
    def setUp(self):  # Configura o ambiente de teste antes de cada método de teste
        self.name = 'joão'  # Define o nome do funcionário
        self.sobrenome = 'ninguem'  # Define o sobrenome do funcionário
        self.salario = 5000  # Define o salário do funcionário
        self.novo_funcionario = Employee(self.name, self.sobrenome, self.salario)  # Cria um objeto Employee para teste

    def test_give_default_raise(self):  # Define um método de teste para o aumento de salário padrão
        self.novo_funcionario.give_raise()  # Chama o método give_raise() sem argumento
        self.assertEqual(10000, self.novo_funcionario.salario)  # Verifica se o salário foi aumentado corretamente

    def test_give_custom_raise(self):  # Define um método de teste para o aumento de salário personalizado
        self.novo_funcionario.give_raise(2000)  # Chama o método give_raise() com um argumento de 2000
        self.assertEqual(7000, self.novo_funcionario.salario)  # Verifica se o salário foi aumentado corretamente

unittest.main()  # Executa os testes