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
    
    def test_store_single_response(self):
        """Testa se uma única resposta é armazenada de forma apropriada."""
        question = "What language did you first learn to speak?" # Define a pergunta da pesquisa
        my_survey = AnonymousSurvey(question) # Cria uma instância da classe AnonymousSurvey
        my_survey.store_response('English') # Armazena uma resposta

        self.assertIn('English', my_survey.responses) # Verifica se a resposta foi armazenada
    
    def test_store_three_response(self):
        """Testa se três respostas são armazenadas de forma apropriada."""
        question = "What language did you first learn to speak?" # Define a pergunta da pesquisa
        my_survey = AnonymousSurvey(question) # Cria uma instância da classe AnonymousSurvey
        responses = ['English','Spanish','Mandarin'] # Define uma lista de respostas
        for response in responses: # Itera sobre a lista de respostas
            my_survey.store_response(response) # Armazena cada resposta
        
        for response in responses: # Itera sobre a lista de respostas
            self.assertIn(response, my_survey.responses) # Verifica se cada resposta foi armazenada

unittest.main() # Executa os testes