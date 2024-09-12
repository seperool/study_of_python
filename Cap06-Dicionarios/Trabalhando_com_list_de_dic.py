#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:04:43 2024

@author: sergio
"""

#Criando uma lista vazia para armazenar aliens
aliens = []

#Criando 30 aliens verdes
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#Mostrando os 5 primeiros aleins
for alien in aliens[:5]:
    print(alien)
print("...")

#Mostrando quantos alienígenas foram criados
print("O número total de alienígenas é " +
      str(len(aliens)) + ".")

#Mudando a cor dos 3 primeiros aliens de verde para amarelo
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

#Mostrando os 5 primeiros aliens
for alien in aliens[:5]:
    print(alien)

#Mudando a cor dos 10 primeiros aliens de verde para amarelo e amarelo para vermelho
for alien in aliens[:10]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

#Mostrandos os 15 primeiros aliens
print("\nOs 15 primeiros aliens:")
for alien in aliens[:15]:
    print(alien)