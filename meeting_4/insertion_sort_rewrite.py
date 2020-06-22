# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:19:43 2020

@author: heitk
"""

list = [21, 5, 22, 20, 12, 3, 11, 5, 13, 16]

def insertion_help(list, ele):
    i = 0
    if len(list) == 0:
        list.insert(i, ele)
    else:
        while list[i] < ele:
            i = i + 1
            if i == len(list):
                list.insert(i + 1, ele)
                return list

        list.insert(i, ele)
    return list

def insertion_sort(list):
    new_list = []

    for i in range(len(list)):
        new_list = insertion_help(new_list, list[i])

    return new_list

print (list)
print (insertion_sort(list))
