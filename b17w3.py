# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:26:15 2024

@author: 
"""
n= int(input("Nhap n= "))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('*', end= ' ')
        else:
            print(' ', end= ' ')
    print()
       
     
     