#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:46:33 2024

@author: sergio
"""

#Bibliotecas padrão do Python

#Importando biblioteca-padrão collections a função OrderedDict
#OrderedDict = é um dicionário que mantém a ordem dos pares chave-valor
from collections import OrderedDict

#Instância
favorite_languages = OrderedDict()

#Pares chave-valor
favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'

#Mantem a ordem de entrada
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")