# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:47:35 2024

@author: 
"""
import math
n= int(input("Nhap so nguyen duong n: "))
chinhphuong= False
canbac2= int(math.sqrt(n))
if canbac2 * canbac2 == n:
    chinhphuong= True
if chinhphuong:
    print(n, "la so chinh phuong.")
else:
    print(n, "khong phai la so chinh phuong.")
