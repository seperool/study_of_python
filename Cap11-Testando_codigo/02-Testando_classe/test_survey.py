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

unittest.main() # Executa os testes