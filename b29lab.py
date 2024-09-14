# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:05:57 2024

@author: 
"""
while True:
    try:
        n= int(input("Nhap vao day so nguyen duong: "))
        if n>0:
            break
        else:
            print("So nhap vao phai la mot so nguyen duong. Vui long thu lai.")
    except:
        print("Dau vao khong hop le. Vui long nhap mot so nguyen.")
tong= 0
for chuso in str(n):
    tong += int(chuso)
    print("Tong cac chu so ", n, "la:", tong)
