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

favorite_places = {
    'sergio': ['nilopolis','nova friburgo'],
    'maria': ['bangu'],
    'marcelo': ['araruama','saquarema','rio das ostras'],
    'eduardo':['nova iguaçu','rio das ostras']
    }
for name, places in favorite_places.items():
    if len(places) != 1:
        print("\nOs lugares favoritos de " + name.title() + " são:")
        for place in places:
            print(place.title())
    else:
        print("\nO lugar favorito de " + name.title() + " é " + places[0].title())

#10)

number_faverite = {'mario':[42,56],
                   'ricardo':[54,38],
                   'sergio':[29,48],
                   'marcela':[96,100],
                   'rafaela':[12,1,79]
                   }
for nome, numeros in number_faverite.items():
    print("\nOs números favoritos de " + nome.title() + " são:")
    for numero in numeros:
        print(numero)

#11)

cities = {
    'nova friburgo':{'country':'brasil',
                     'population':203328,
                     'id':'nf'},
    'nilopolis':{'country':'brasil',
                 'population':16000,
                 'id':'n'},
    'nova iguaçu':{'country':'brasil',
                   'population':843046,
                   'id':'ni'}
    }

for cidade, infos in cities.items():
    print("\nA cidade de " + cidade.title() + " tem:")
    for curiosidade, info in infos.items():
        print(curiosidade.title() + ": " + str(info))