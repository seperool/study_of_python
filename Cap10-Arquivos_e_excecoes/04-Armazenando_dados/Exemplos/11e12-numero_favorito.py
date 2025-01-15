#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 23:10:28 2025

@author: sergio
"""

import json

def get_number_favorite():
    """Pega o número favorito do usuário e salva num arquivo json."""
    # Define o nome do arquivo onde o número será salvo.
    filename = "favorite_num.json"
    # Solicita ao usuário que informe seu número favorito e armazena como string.
    num = input("Informe seu número favorito: ")
    # Abre o arquivo no modo de escrita ("w"). O 'with open' garante que o arquivo será fechado corretamente, mesmo em caso de erros.
    with open(filename, "w") as f_obj:
        # Usa json.dump() para salvar o número (que está como string) no arquivo JSON.
        json.dump(num, f_obj)

def return_favorite_num():
    """Lembra do número favorito do usuário lendo do arquivo json."""
    # Define o nome do arquivo onde o número está salvo.
    filename = "favorite_num.json"
    try:
        # Tenta abrir o arquivo no modo de leitura ("r" - padrão, pode ser omitido).
        with open(filename) as f_obj:
            # Usa json.load() para carregar o número do arquivo JSON.
            favorite_num = json.load(f_obj)
    # Se o arquivo não existir (FileNotFoundError), a função retorna None.
    except FileNotFoundError:
        return None
    # Se o arquivo existir e for lido sem erros, a função retorna o número favorito.
    else:
        return favorite_num

def favorite_num():
    """
    Função principal que gerencia o número favorito do usuário.
    Retorna o número favorito do usuário, caso exista no arquivo.
    Caso não exista, solicita o número ao usuário e o salva para uma próxima interação.
    """
    # Chama a função return_favorite_num() para tentar obter o número favorito do arquivo.
    favorite_num = return_favorite_num()
    # Verifica se favorite_num tem um valor (ou seja, se o número foi lido do arquivo).
    if favorite_num:
        # Se o número existe, imprime uma mensagem com o número favorito. Note que é necessário converter para string, pois o json.load retorna o tipo original do dado salvo (string neste caso)
        print("Seu número favorito é: " + favorite_num)
    # Se favorite_num for None (ou seja, o arquivo não existe ou não pôde ser lido), executa o bloco else.
    else:
        # Chama a função get_number_favorite() para solicitar e salvar o número favorito do usuário.
        get_number_favorite()
        # Imprime uma mensagem informando que o número será lembrado na próxima vez.
        print("Lembrarei na próxima interação!")

# Chama a função principal para executar o programa.
favorite_num()