#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:37:53 2024

@author: sergio
"""

#Classes

#Classe-pai
class User():
    
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

#Classes-filhas
class Privileges():
    
    #Atributos
    def __init__(self):
        self.privileges = ["can add post",
                           "can delete post",
                           "can ban user"]
    #Métodos
    def show_privileges(self):
        print("\nOs privilégios do admin são:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    
    #Atributos
    def __init__(self,first_name,last_name,nick='',email='',local=''):
        #Atributo instância
        self.privileges = Privileges()
        
        #Atributos herdados
        super().__init__(first_name,last_name,nick,email,local)

#Instância
admin = Admin("marcelo", "bom fa","mfa","mfa@bol.com","nilopolis")

#Chamadas
admin.describe_user()
admin.privileges.show_privileges()