# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:16:02 2024

@author: 
"""
thang= int(input("Nhap thang: "))
nam= int(input("Nhap nam: "))
namnhuan= False
if ( nam % 4 ==0 and nam % 100 != 0) or (nam % 400 ==0):
    lanamnhuan= True
#Xác định số ngày trong tháng
if thang ==2:
    if lanamnhuan:
        songay = 29
    else:
        songay = 28
elif thang in [4, 6, 9, 11]:
    songay= 30
else:
    songay= 31
print("Thang" + str(thang) + "nam" + str(nam) + "co" + str(songay) + "ngay")
    
