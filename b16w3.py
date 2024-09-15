# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:21:33 2024

@author: 
"""
n= int(input("Nhap so nguyen duong n:"))
if n <= 0:
    print("So vua nhap phai la so nguyen duong.")
else:
    chuoinhiphan= ""
    so= n
    while so > 0:
        conlai= so % 2
        chuoinhiphan += str(conlai)
        so= so // 2
    if chuoinhiphan == "":
        chuoinhiphan = "0"
    print(chuoinhiphan)
    
