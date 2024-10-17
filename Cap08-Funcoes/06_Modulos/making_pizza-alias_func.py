#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:27:04 2024

@author: sergio
"""

#Importando função do módulo explicitamente
#Dando um alias que substitui o nome da função
from pizza import make_pizza as mp

#Usando função do módulo
#Quando importamos o módulo e explicitamos a função, podemos chamar a função diretamente
#Sem explicitar: nome_modulo.nome_função()
mp(16, 'pepperoni')
mp(12, 'mushrooms','green peppers','extra cheese')