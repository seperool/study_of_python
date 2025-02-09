#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:33:52 2025

@author: sergio
"""

# Importa a biblioteca e classe.
from survey import AnonymousSurvey # Importa a classe AnonymousSurvey do arquivo survey.py

# Define uma pergunta e cria uma pesquisa.
question = "What language did you first learn to speak?" # Define a pergunta da pesquisa
my_survey = AnonymousSurvey(question) # Cria uma instância da classe AnonymousSurvey com a pergunta definida

# Mostra a pergunta e armazena as repostas da pergunta.
my_survey.show_question() # Exibe a pergunta da pesquisa
print("Enter 'q' at any time to quit.\n") # Instrui o usuário a digitar 'q' para sair
while True: # Loop infinito para coletar respostas
    response = input("Language: ") # Solicita a resposta do usuário
    if response == 'q': # Verifica se o usuário digitou 'q'
        break # Sai do loop se o usuário digitou 'q'
    my_survey.store_response(response) # Armazena a resposta na pesquisa

# Exibe os resultados da pesquisa.
print("\nThank you to everyone who participated in the survay!") # Mensagem de agradecimento
my_survey.show_results() # Exibe os resultados da pesquisa