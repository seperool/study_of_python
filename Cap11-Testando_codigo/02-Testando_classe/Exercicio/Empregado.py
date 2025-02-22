#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:02:21 2025

@author: sergio
"""

from Employee import Employee # Importa a classe Employee do arquivo Employee.py

novo_empregado = Employee("Marcelo",'Nogueira',2000) # Cria um novo objeto Employee

print(type(novo_empregado.show_salario())) # Imprime o tipo do valor retornado por show_salario()
novo_empregado.give_raise(200) # Aumenta o salário em 200
novo_empregado.give_raise() # Aumenta o salário pelo valor padrão