# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:43:27 2024

@author: 
"""
while True: 
        try:
            n= int(input("Nhap vao mot so nguyen duong:"))
            if n>0:
                uocso= []
                for i in range(1, n+1):
                    if n%i ==0:
                        uocso += [i]
                break
            else:
                print("So nhap vao phai la mot so nguyen duong. Vui lòng thu lai.")
        except:
            print("Dau vao khong hop le. Vui long nhap mot so nguyen.")
#In ra các ước số
print("Cac uoc so cua ", n, "la:", uocso)
                        
                     