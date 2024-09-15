# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:37:11 2024

@author: 
"""
n= int(input("Nhap n: "))
x, y = n, n
while y != 0:
    x, y = y, x % y
gcd_n= x
for i in range(n):
    for j in range(n):
        a, b = i + 1, j + 1
        x, y = a, b
        while y != 0:
            x, y = y, x % y
        if x == 1:
            print('*', end= '')
        else:
            print('', end= '')
    print()
    
        
    
