# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:18:49 2024

@author: 
"""
while True:
    try:
        giatri= float(input("Nhap gia tri so huc trong khoang [-89.9, 88.8]: "))
        if -89.9 <= giatri <= 88.8:
            print("Gia tri hop le.", giatri)
            break
        else:
            print("Gia tri khong nam trong khoang [-89.9, 88.8]. Vui long nhap lai.")
    except: 
      print("Gia tri vua nhap khong phai la so thuc. Vui long nhap lai.")
            