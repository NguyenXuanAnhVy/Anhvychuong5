# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:52:36 2024

@author: 
"""
while True: 
    try:
       giatri = float(input("Nhap mot so thuc trong khoang [-99, 99]: "))
       if -99 <= giatri <= 99:
            print("Gia tri hop le.",giatri)
            break
       else:
            print("Gia tri khong nam trong khoang [-99, 99]. Vui long nhap lai.")
    except:
        print("Gia tri nhap vao khong phai la so thuc. Vui long nhap lai.")
