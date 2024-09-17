#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:59:24 2024

@author: sergio
"""

prompt = "\nTell me soomething, and I will repeat it back to you:"
prompt += "\n(Enter 'quit' to end the program.)"
prompt += "\n"

active = True

message = ""
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)