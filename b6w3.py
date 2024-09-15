# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:39:28 2024

@author: 
"""
try:
    n= int(input("Nhap so lan in chu 'Hello': "))
    if n < 1000:
        for _ in range(n):
            print("Hello")
    else:
        print("Tham so khong hop le, phai nho hon 1000.")
except:
    print("Vui long nhap mot so nguyen hop le.")