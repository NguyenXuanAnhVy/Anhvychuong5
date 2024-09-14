# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:34:22 2024

@author: 
"""
a= int(input("Nhap a: "))
b= int(input("Nhap b: "))
c= int(input("Nhap c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giac deu.")
    elif a == b or b == c or a == c:
        print("Tam giac can.")
    elif (a**2) + (b**2) == c**2 or (a**2) + (c**2) == b**2 or (b**2) + (c**2) == a**2:
        print("Tam giac vuong.")
    else:
        print("Tam giac thuong.")
else:
    print("Ba so khong tao thanh tam giac.")
        