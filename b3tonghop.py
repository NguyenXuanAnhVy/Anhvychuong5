# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:29:32 2024

@author: 
"""
idnguoidung= input("Nhap ID nguoi dung: ")
matkhau= input("Nhap mat khau: ")
if 6 <= len(idnguoidung) <= 24 and all(i not in "!@#$%^&*()-=+ " for i in idnguoidung):
    print("ID nguoi dung hop le.")
else:
    print("ID nguoi dung khong hop le.")
chuthuong, so, chuhoa, kytudacbiet= False, False, False, False
if 6 <= len(matkhau) <= 24:
    for i in matkhau:
        if i.islower():
            chuthuong= True
        elif i.isdigit():
            so= True
        elif i.isupper():
            chuhoa= True
        elif i in "$#@":
            kytudacbiet= True
    if chuthuong and so and chuhoa and kytudacbiet:
        print("Mat khau hop le.")
    else:
        print("Mat khau khong hop le.")
else:
    print("Mat khau khong hop le.")