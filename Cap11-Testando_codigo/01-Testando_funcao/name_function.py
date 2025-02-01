#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:55:17 2025

@author: sergio
"""

def get_formatted_name(first, middle, last):
    """Gera um nome completo formatado de modo elegante.

    Args:
        first (str): O primeiro nome.
        middle (str): O nome do meio.
        last (str): O sobrenome.

    Returns:
        str: O nome completo formatado.
    """

    # Concatena as partes do nome com espaços
    full_name = first + " " + middle + " " + last

    # Formata o nome para capitalizar a primeira letra de cada palavra
    return full_name.title()
