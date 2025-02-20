#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:43:34 2025

@author: sergio
"""

import unittest
from survey import AnonymousSurvey

class testAnonmyousSurvey(unittest.TestCase):
    """Testes para a classe AnonmyousSurvey."""
    def setUp(self):
        """
        Cria uma pesquisa e um conjunto de respostas que poderão ser usados em 
        todos os métodos de teste.
        """
        question = "What language did you first learn to speak?" # Define a pergunta da pesquisa
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']
        
    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma apropriada."""
        self.my_survey.store_response(self.responses[0]) # Armazena uma resposta
        self.assertIn(self.responses[0], self.my_survey.responses) # Verifica se a resposta foi armazenada
    
    def test_store_three_response(self):
        """Testa se três respostas são armazenadas de forma apropriada."""
        for response in self.responses: # Itera sobre a lista de respostas
            self.my_survey.store_response(response) # Armazena cada resposta
        
        for response in self.responses: # Itera sobre a lista de respostas
            self.assertIn(response, self.my_survey.responses) # Verifica se cada resposta foi armazenada

unittest.main() # Executa os testes