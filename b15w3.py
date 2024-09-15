# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:11:53 2024

@author: 
"""
i= int(input("Nhap so nguyen i: "))
k= int(input("Nhap co so k (tu 2 den 16): "))
if k < 2 or k > 16:
    print("Co so k phai nam trong khoang tu 2 den 16.")
else:
    if i == 0:
        print("0")
    else:
        chuso= "0123456789ABCDEF"
        ketqua= ""
        so= i
        while so > 0:
          conlai= so % k
          ketqua= chuso[conlai] + ketqua
          so= so // k
          print(ketqua)
          
