#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 00:33:20 2024

@author: sergio
"""

#Importando função do módulo explicitamente
from pizza import make_pizza

#Usando função do módulo
#Quando importamos o módulo e explicitamos a função, podemos chamar a função diretamente
#Sem usar: nome_modulo.nome_função()
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')