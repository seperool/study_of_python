#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 19 11:21:13 2025

@author: sergio
"""

# Importa a classe datetime do módulo datetime
from datetime import datetime

# Converte a string '2014-7-1' para um objeto datetime usando o formato '%Y-%m-%d'
first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
# Imprime o objeto datetime
print(first_date)