#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:23:17 2024

@author: sergio
"""

#Classe usuário
class user():
    
    #Atributos
    def __init__(self,first_name,last_name,nick='',email='',local=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nick = nick
        self.local = local
    
    #Métodos
    def describe_user(self):
        print("\nResumo do usuário:")
        print("Nome: " + self.first_name.title() + 
              " " + self.last_name.title())
        if self.email:
            print("email: " + self.email)
        if self.nick:
            print("Nick: " + self.nick)
        if self.local:
            print("O local do usuário: " + self.local.title())
    
    def greet_user(self):
        nome_completo = self.first_name
        nome_completo += " "
        nome_completo += self.last_name
        print("\nOlá " + nome_completo.title() + "!")
        if self.nick:
            print("aka " + self.nick + "!")

#Criando instâncias da classe
john_user = user("john", "master",
                 nick="jonny_master",
                 email="john.master@bol.com.br")

marcelo_user = user("marcelo", "pereira",
                    nick="mperio",
                    email="marcel_p@gmail.com",
                    local="Rio de janeiro")

susana_user = user("susana", "marinho",nick="susanao")

#Chamando métodos
##Descrições
john_user.describe_user()
marcelo_user.describe_user()
susana_user.describe_user()

##Saudação aos usuários
john_user.greet_user()
marcelo_user.greet_user()
susana_user.greet_user()