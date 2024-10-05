#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:04:46 2024

@author: sergio
"""

#Função e default
def describe_city(cidade,pais='brasil'):
    print(cidade.title() + " esta localizada no " + pais.title() + ".")

describe_city("macaé")
describe_city("nilopolis")
describe_city("meca")