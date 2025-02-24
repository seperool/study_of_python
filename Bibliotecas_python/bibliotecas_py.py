# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 23:07:22 2024

@author: Sérgio
"""

import os                            # Interação com o sistema operacional
import math                          # Funções matemáticas
import statistics                    # Funções estatísticas
import numpy as np                   # Computação numérica (arrays, matrizes)
import pandas as pd                  # Análise e manipulação de dados (DataFrames)
import json                          # Manipulação de dados JSON
import unittest                      # Testes unitários

import tensorflow as tf              # Aprendizado de máquina (Google)
from tensorflow import keras         # API de alto nível para redes neurais
from tensorflow.keras import layers  # Camadas para redes neurais

import sklearn                       # Aprendizado de máquina (scikit-learn)
import matplotlib.pyplot as plt      # Criação de gráficos
import Pygal                         # Criação de gráficos vetoriais escaláveis
import seaborn as sns                # Visualização de dados (baseado no Matplotlib)

import kivy                          # Desenvolvimento de aplicativos multi-touch

# Bibliotecas adicionais (Quarto - para outputs formatados)
from IPython.display import Markdown # Renderizar Markdown
from tabulate import tabulate        # Formatar tabelas de texto