# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:17:12 2024

@author: 
"""
try:
    khoangcach= float(input("Nhap khoang cach(km): "))
    tiencuoc= 0
    if khoangcach > 0:
        tiencuoc += 15000
        khoangcach -= 1
        while khoangcach > 0 and khoangcach > 4:
            tiencuoc += 13500
            khoangcach -= 1
        while khoangcach > 0:
            tiencuoc += 11000
            khoangcach -= 1
        if khoangcach + 5 > 120:
            tiencuoc *= 0.9
            print("Tien cuoc taxi: " + str(int(tiencuoc)) + "đ")
except:
  print("Vui long nhap mot so hop le.")  
          
