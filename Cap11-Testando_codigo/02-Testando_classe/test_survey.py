#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:43:34 2025

@author: sergio
"""

import unittest
# Importa a classe AnonymousSurvey do módulo survey
from survey import AnonymousSurvey

# Define uma classe de teste chamada testAnonmyousSurvey que herda de unittest.TestCase
class testAnonmyousSurvey(unittest.TestCase):
    """Testes para a classe AnonmyousSurvey."""
    # Define um método setUp que é executado antes de cada método de teste
    def setUp(self):
        """
        Cria uma pesquisa e um conjunto de respostas que poderão ser usados em 
        todos os métodos de teste.
        """
        # Define a pergunta da pesquisa
        question = "What language did you first learn to speak?"
        # Cria uma instância da classe AnonymousSurvey com a pergunta definida
        self.my_survey = AnonymousSurvey(question)
        # Define uma lista de respostas
        self.responses = ['English','Spanish','Mandarin']
        
    # Define um método de teste para verificar se uma única resposta é 
    #armazenada corretamente
    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma apropriada."""
        # Armazena a primeira resposta da lista na pesquisa
        self.my_survey.store_response(self.responses[0])
        # Verifica se a resposta foi armazenada corretamente na lista
        #de respostas da pesquisa
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    # Define um método de teste para verificar se três respostas 
    #são armazenadas corretamente
    def test_store_three_response(self):
        """Testa se três respostas são armazenadas de forma apropriada."""
        # Itera sobre a lista de respostas e armazena cada resposta na pesquisa
        for response in self.responses:
            self.my_survey.store_response(response)
        
        # Itera sobre a lista de respostas e verifica se cada resposta 
        #foi armazenada corretamente
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

# Executa os testes unitários
unittest.main()