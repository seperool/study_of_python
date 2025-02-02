#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:55:17 2025

@author: sergio
"""

def get_formatted_name(first, last, middle=''):
    """Gera um nome completo formatado de modo elegante.

    Args:
        first (str): O primeiro nome.
        middle (str): O nome do meio (opcional).
        last (str): O sobrenome.

    Returns:
        str: O nome completo formatado.
    """
    if middle:
        # Concatena as partes do nome com espaços, incluindo o nome do meio
        full_name = first + " " + middle + " " + last
    else:
        # Concatena as partes do nome com espaços, sem o nome do meio
        full_name = first + " " + last

    # Formata o nome para capitalizar a primeira letra de cada palavra
    return full_name.title()

