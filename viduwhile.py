# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:56:28 2024

@author: Student
"""
# while
so= 0
n = int(input("Nhap vao so lan can lap: "))
while (so < n):
    print("Lan lap thu: ", so + 1, "\tBien dem:", so)
    so = so + 1
# while co else
so= 0
n= int(input("Nhap vao so lan can nhap: "))
while (so<n):
    print("Lan lap thu: ", so + 1, "\tBien dem:", so)
    so = so + 1
else:
    print("\nThuc hien lenh trong else, do:", "\nso=", so, "\nn=", n, "\nbool(so<n)=", bool(so<n))
    