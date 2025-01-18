#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 23:09:13 2025

@author: sergio
"""

import json

def get_stored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    # Carrega o nome do usuário se foi armazenado anteriormente
    # Caso contrário, pede que o usuário forneça o nome e armazena essa informação
    filename = "username.json"

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Pede um novo nome de usuário."""
    username = input("What is your name? ")
    filename = "username.json"
    with open(filename,'a') as f_obj:
        json.dump(username, f_obj)
    return username

def confirme_user(usernames):
    for username in usernames:
        answer = input("You are "+ username + "? (S/N) \n")
        if answer == 'N':
            pass
        elif answer == 'S':
            break
    return username
        
def greet_user():
    """Saúda o usuário pelo nome."""
    resposta = input("Já é cadastrado?(s/n) \n")
    if resposta == "s":
        usernames = get_stored_username()
        username = confirme_user(usernames)
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + 
              username + "!")

greet_user()