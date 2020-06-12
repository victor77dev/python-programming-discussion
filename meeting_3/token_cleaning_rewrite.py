#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:28:30 2020

@author: JiaJian
"""

Word = input("Enter word: ")
if "'" in Word[0] and "'" in Word[-1]:
    Word = Word.replace("'", "", -1)

Word = Word.strip(",!?. \"")

symbol = [",", ".", "?", "!", "\""]
for i in symbol:
    Word = Word.replace(i, "", -1)

if Word == "":
    print("Achtung: Kein Token gefunden.")
else:
    print(Word)
