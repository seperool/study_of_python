#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:27:14 2024

@author: sergio
"""

#Importando módulo
import admin

#Criando instância de Admin
#nome_modulo.nome_classe
user_admin = admin.Admin("marcelo", "pereira")

#Chamando uma variável instância
#variável.método
user_admin.privileges.show_privileges()