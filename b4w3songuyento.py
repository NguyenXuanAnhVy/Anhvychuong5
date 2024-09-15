# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:43:06 2024

@author: 
"""
n= int(input("Nhap n: "))
sont= [True] * n
sont[0] = sont[1] = False
for i in range(2, int(n**0.5) + 1):
    if sont[i]:
        for j in range(i*i, n, i):
            sont[j] = False
so= sum(sont)
print(so)



