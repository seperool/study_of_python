#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:49:50 2024

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
        #Atributo default
        self.login_attempts = 0
    
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
    
    ##Incrementa login_attempts em 1,
    ##conta cada tentativa de login
    def increment_login_attempts(self):
        self.login_attempts += 1
        self.tentativas_login()
    
    ##Reseta as tentativas de login
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Tentativas de login resetada!")
        self.tentativas_login()
    
    def tentativas_login(self):
        print(f"Tentativas de login: {self.login_attempts}")

#Instância
user_1 = user("Mario", "Mario",nick="mariomario",
              email="mario@bol.com")

#Incrementando tentativas de login
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

#Resetando tentativas de login
user_1.reset_login_attempts()