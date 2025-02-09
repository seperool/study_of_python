#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:57:36 2025

@author: sergio
"""

class AnonymousSurvey():
    """Coleta respostas anônimas para uma pergunta de uma pesquisa."""
    
    def __init__(self,question):
        """Armazena uma pergunta e se prepara para armazenar uma resposta."""
        self.question = question # Atribui a pergunta à instância da classe
        self.responses = [] # Inicializa uma lista vazia para armazenar as respostas
    
    def show_question(self):
        """Mostra a pergunta da pesquisa."""
        print(self.question) # Imprime a pergunta da pesquisa
    
    def store_response(self, new_response):
        """Armazena uma única resposta da pesquisa."""
        self.responses.append(new_response) # Adiciona a nova resposta à lista de respostas
    
    def show_results(self):
        """Mostra todas as respostas dadas."""
        print("Survey results:") # Imprime um cabeçalho para os resultados da pesquisa
        for response in self.responses: # Itera sobre a lista de respostas
            print("- " + response) # Imprime cada resposta formatada