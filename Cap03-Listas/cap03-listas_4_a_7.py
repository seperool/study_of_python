#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:46:40 2024

@author: sergio
"""

#4)
nomes = ["zico","stephen king","Muhammad ali"]
print('Caro '+nomes[0].title()+',\nGostaria de sua presença no jantar.')
print('Caro '+nomes[1].title()+',\nGostaria de sua presença no jantar.')
print('Caro '+nomes[2].title()+',\nGostaria de sua presença no jantar.')

#5)
#Não poderá comparecer
nao_comparecer = nomes.pop()
print(nao_comparecer.title() + ' Não poderá comparecer.')

#Novo convidado
nomes.append('mano brown')
print(nomes)

#Novos convites
print('Caro '+nomes[0].title()+',\nGostaria de sua presença no jantar.')
print('Caro '+nomes[1].title()+',\nGostaria de sua presença no jantar.')
print('Caro '+nomes[2].title()+',\nGostaria de sua presença no jantar.')

#6)
#Foram encontrados mais lugares
print("Foi encontrado uma mesa maior, terão mais 3 convidados.")

nomes.insert(0, 'lula')
nomes.insert(2, 'brizola')
nomes.append('silvio santos')

print(nomes)

#Novos convites
print('Caro '+nomes[0].title()+',\nGostaria de sua presença no jantar.')
print('Caro '+nomes[1].title()+',\nGostaria de sua presença no jantar.')
print('Caro '+nomes[2].title()+',\nGostaria de sua presença no jantar.')
print('Caro '+nomes[3].title()+',\nGostaria de sua presença no jantar.')
print('Caro '+nomes[4].title()+',\nGostaria de sua presença no jantar.')
print('Caro '+nomes[5].title()+',\nGostaria de sua presença no jantar.')

#7)
#mensagem de desculpas sobre o problema de mesas
print("Por conta de um problema de mesas, teremos apenas 2 convidados, \npedimos desculpas a todos os convidados.")

#Removendo convidados
conv_remov = nomes.pop()
print("Sentimos muito " + conv_remov.title() + ", você foi desconvidado." + "\nAgradecemos a paciência.")

conv_remov = nomes.pop()
print("Sentimos muito " + conv_remov.title() + ", você foi desconvidado." + "\nAgradecemos a paciência.")

conv_remov = nomes.pop()
print("Sentimos muito " + conv_remov.title() + ", você foi desconvidado." + "\nAgradecemos a paciência.")

conv_remov = nomes.pop()
print("Sentimos muito " + conv_remov.title() + ", você foi desconvidado." + "\nAgradecemos a paciência.")

#Confirmando convidados
print("Olá " + nomes[0].title() + ", sua presença ainda é esperada.")
print("Olá " + nomes[1].title() + ", sua presença ainda é esperada.")

#Limpando lista
del nomes[1]
del nomes[0]
print(nomes)
