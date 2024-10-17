#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:58:41 2024

@author: sergio
"""

import printing_functions

#Alguns designs que devem ser impressos.
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)