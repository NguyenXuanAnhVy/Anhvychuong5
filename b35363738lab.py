# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:05:58 2024

@author: 
"""
#B35
n= int(input("Nhap so nguyen duong: "))
S= 0
for i in range(1, n+1):
    S += i
print("Tong S= 1 + 2 + 3 + ... + n la: ", S)
#B36
n= int(input("Nhap so: "))
S= 0
for i in range(1, n+1):
    S += i*i
print("Tong S = 12 + 32 + ... + n^2 la: ", S)
#B37
n= int(input("Nhap so nguyen duong n (phai la so chan): "))
if n%2 != 0:
    print("So vua nhap vao khong phai so chan.")
else:
    S= 0
    for i in range(2, n+1, 2):
        S += i
    print("Tong S = 2 + 4 + 6 + ... + n la: ", S)
#B38
n= int(input("Nhap so nguyen duong n (phai la so le): "))
if n%2 == 0:
    print("So vua nhap khong phai la so le.")
else:
    S= 1
    for i in range(1, n+1):
        S *= i
    print("Tich S = 1 * 2 * 3 * ... * n la: ", S)
