# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:06:53 2024

@author: 
"""
chuoi= input("Nhap mot chuoi: ")
#Tính độ dài của chuỗi
dodai= len(chuoi)
print("Do dai cua chuoi: ", dodai)
#Đếm các ký tự đặc biệt
kytu= "!@#$%^&*()-=+./"
dacbiet= 0
for kt in chuoi:
    if kt in kytu:
        dacbiet += 1
print("So luong ky tu dac biet: ", dacbiet)
#Đếm các ký tự chữ cái từ a-z
kytuchucai= 0
for kt in chuoi:
    if kt.islower():
        kytuchucai += 1
print("So luong ky tu chu cai thuong (a-z): ", kytuchucai)
#Đếm các ký tự chữ số từ 0-9
kytuchuso= 0
for kt in chuoi:
    if kt.isdigit():
        kytuchuso += 1
print("So luong chu so (0-9):", kytuchuso)
#Đếm các ký tự chữ cái viết hoa (A-Z)
kytuviethoa= 0
for kt in chuoi:
    if kt.isupper():
        kytuviethoa += 1
print("So luong chu cai viet hoa (A-Z): ", kytuviethoa)


    
