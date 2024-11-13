#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:44:21 2024

@author: sergio
"""

#Módulo que importa outro módulo
#Importando módulo e classe User
from userpai import User

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