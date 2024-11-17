#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 03:34:27 2024

@author: sergio
"""

#Bibliotecas padrão do Python

#Importando biblioteca-padrão collections a função OrderedDict
#OrderedDict = é um dicionário que mantém a ordem dos pares chave-valor
from collections import OrderedDict

#Instância
glossario = OrderedDict()

#Armazenando chaves-valores
glossario['print'] = "Imprime na tela uma mensagem."
glossario['dicionários'] = "Os Dicionários permitem conectar informações relacionadas."
glossario['lista'] = "Uma lista é uma coleção de itens em uma ordem em particular."
glossario['del'] = "Quando não houver mais necessidade de uma informação armazenada em um dicionário, podemos usar a instrução del para remover totalmente um par chave-valor."
glossario['tuplas'] = "Tuplas são listas em que os itens não são criadas para mudar (listas imutáveis)."

#Percorrendo o dicionário OrderedDict
for key, value in glossario.items():
    print("\n" + key + ":")
    print(value)