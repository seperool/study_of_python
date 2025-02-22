#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:50:47 2025

@author: sergio
"""

class Employee():
    def __init__(self, name, sobrenome, salario):
        self.name = name  # Inicializa o nome do funcionário
        self.sobrenome = sobrenome  # Inicializa o sobrenome do funcionário
        self.salario = salario  # Inicializa o salário do funcionário

    def give_raise(self, new_salario=5000):
        self.salario = self.salario + new_salario  # Aumenta o salário pelo valor fornecido ou padrão
        print(self.salario)  # Imprime o novo salário

    def show_salario(self):
        print(self.salario)  # Imprime o salário atual do funcionário