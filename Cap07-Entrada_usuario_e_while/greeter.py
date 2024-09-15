#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 03:25:58 2024

@author: sergio
"""
#Função input() e prompt

#name = input("Please enter your name: ")
#print("Hello, " + name.title() + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your name? " #Adicionando mais linhas na mensagem
name = input(prompt) #Passando o texto como prompt da função input
print("Hello, "+name.title()+"!")