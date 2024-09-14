# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:57:23 2024

@author: 
"""
n= int(input("Nhap so nguyen duong: "))
sont= True
if n <= 1:
    sont= False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sont= False
            break
if sont:
    print(n, "la so nguyen to.")
else:
    print(n, "khong phai la so nguyen to.")
            
            
            
            
