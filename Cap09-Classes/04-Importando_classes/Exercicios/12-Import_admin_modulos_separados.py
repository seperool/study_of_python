#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:42:49 2024

@author: sergio
"""

#Importando módulo, que importa outro módulo
import adminfilhas

#Instância
admin_user = adminfilhas.Admin("marcelo", "fonseca")

#Chamandas
admin_user.describe_user()
admin_user.privileges.show_privileges()