#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:59:44 2024

@author: sergio
"""

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
    }
for name, languages in favorite_languages.items():
    if len(languages) != 1:
        print("\n" + name.title() +
              "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    elif len(languages) == 1:
        language = languages[0]
        print("\n" + name.title() +
              "'s favorite language are: " +
              language.title())