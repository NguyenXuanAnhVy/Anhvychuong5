# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:33:24 2024

@author: 
"""
x= int(input("Nhap x: "))
y= int(input("Nhap y: "))
while y != 0:
    x, y = y, x % y
print(x)
