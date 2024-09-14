# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:28:22 2024

@author: tienx
"""
#B39
n= int(input("Nhap so: "))
S = 0.0
for i in range(1, n+1):
    S += 1/i
print("Tong S(n) = 1 + 1/2 + 1/3 + ... + 1/n la: ", S)
#B40
n= int(input("Nhap so: "))
S= 0.0
for i in range(1, n+1):
    S += 1/(2*i)
print("Tổng S(n) = 1/2 + 1/4 + ... + 1/2n là:", S)
#B41
n= int(input("Nhap so: "))
S= 0.0
for i in range(1, n+1):
    S += 1/(2*i+1)
print("Tổng S(n) = 1 + 1/3 + 1/5 + ... + 1/(2n+1) là:", S)
#B42
n= int(input("Nhap so: "))
S=0.0
for i in range(1, n+1):
    S += 1/i*(i+1)
print("Tổng S(n) = 1/(1*2) + 1/(2*3) + ... + 1/(n*(n+1)) là:", S)
#B43
n= int(input("Nhap so: "))
S=0.0
for i in range(1, n+1):
    S += i/(i+1)
print("Tổng S(n) = 1/(1*2) + 2/3 + 3/4 + ... + n/(n+1) là:", S)
#B44
n= int(input("Nhap so: "))
S=0.0
for i in range(1, n+1):
    S += (2*i-1)/(2*i+1)
print("Tổng S(n) = 1/2 + 3/4 + ... + (2n+1)/(2n+2) là:", S)
#B45
n= int(input("Nhap n: "))
x= float(input("Nhap x: "))
S= 0.0
tong= 0
for i in range(1, n+1):
    tong= 0
    for j in range(1, i+1):
        tong += j
    S += (x**i)/tong
print("Tổng S(n) = x + x^2/(1+2) + x^3/(1+2+3) + ... + x^n/(1+2+...+n) là:", S)