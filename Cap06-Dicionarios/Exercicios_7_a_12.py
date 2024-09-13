#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 19:00:45 2024

@author: sergio
"""

#7)
marcelo = {'first_name':'marcelo','last_name':'oliveira','city':'rio de janeiro'}
thiago = {'first_name':'thiago','last_name':'valente','city':'saquarema'}
tania = {'first_name':'tania','last_name':'pereira','city':'trindade'}
people = [marcelo,thiago,tania]

for person in people:
    print('\nPrimeiro nome: ' + person['first_name'].title())
    print('Sobrenome: ' + person['last_name'].title())
    print('Cidade natal: ' + person['city'].title())

#8)

arthur = {'tipo':'cachorro','dono':'sergio'}
fifi = {'tipo':'tartaruga','dono':'alexandre'}
zabayone = {'tipo':'tartaruga','dono':'martha'}
paquita = {'tipo':'cachorro','dono':'sergio'}
mufasa = {'tipo':'gato','dono':'alexandre'}
pets = [arthur,fifi,zabayone,paquita,mufasa]

for pet in pets:
    print('\nEsse pet é um(a) ' + pet['tipo'] + 
          " e seu dono é " + pet['dono'].title())

#9)



#10)
#11)
#12)