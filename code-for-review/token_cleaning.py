#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:28:30 2020

@author: JiaJian
"""

word = input("Enter word: ")
if "'" in word[0] and "'" in word[-1]:
    word = word.replace("'", "")

word = word.strip(",!?. \"")

symbols = [',', '.', '?', '!', '"']
for symbol in symbols:
    word = word.replace(symbol, "")

if word == "":
    print("Achtung: Kein Token gefunden.")
else:
    print(word)
