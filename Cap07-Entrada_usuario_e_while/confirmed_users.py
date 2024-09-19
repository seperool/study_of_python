#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:12:26 2024

@author: sergio
"""

#Transferindo itens de uma lista para outra, usando while

unconfirmed_users = ["alice","brian","candace"]
confirmed_users = []

while unconfirmed_users: #O laço continuar enquanto a lista não for vazia
    current_user = unconfirmed_users.pop() #pesca o ultimo item da lista
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user) #Adiciona o item na lista
print("\nThe following users have been confirmed:")
for confirmed in confirmed_users:
    print(confirmed.title())