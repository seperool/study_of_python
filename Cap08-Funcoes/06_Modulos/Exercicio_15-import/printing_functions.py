#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:45:05 2024

@author: sergio
"""

#Função, trabalhando com listas
#Passando listas para função
def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, até que não haja mais nenhum.
    transfere cada design para completed_models após a impressão.
    """
    while unprinted_designs: #Enquanto a lista não for vazia o loop continua
        current_design = unprinted_designs.pop()
        
        #Simula a criação de uma impressão 3D a partir do design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Exibe todos os modelos finalizados"""
    print("\nThe following models have been printed:")
    for complet_model in completed_models: #Percorre a lista
        print(complet_model)