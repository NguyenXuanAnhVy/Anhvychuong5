# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:05:09 2024

@author: 
"""
email= input("Nhap dia chi email: ")
if email.count('@') == 1:
    phantruoc, phansau = email.split('@')
    if len(phantruoc) >= 6 and ' ' not in phantruoc:
        if '.' in phansau:
            tenmien= phansau.split('.')[0]
            morong= phantruoc.split('.')[-1]
            tenmienhople= ['gmail,com', 'yahoo.com', 'hotmail.com', 'outlook.com']
            if phansau in tenmienhople and len(morong) >=2:
                print("Day la mot dia chi email hop le.")
            else:
                print("Day khong phai la mot dia chi email hop le.")
        else:
            print("Day khong phai la mot dia chi email hop le.")
    else:
        print("Day khong phai la mot dia chi email hop le.")
else:
    print("Day khong phai la mot dia chi email hop le.")
    
