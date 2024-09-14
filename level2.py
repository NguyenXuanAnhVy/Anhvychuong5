# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:27:06 2024

@author: 
"""
#1
tong= 0
for i in range(101):
    tong += i
print("Tong tat ca cac so tu 0 den 100 la: ", tong)
#2
tongsochan= 0
tongsole= 0
for i in range(101):
    if i % 2 == 0:
        tongsochan += i
    else:
        tongsole += i
print("Tong cua tat ca cac so chan tu 0 den 100 la: ", tongsochan)
print("Tong cua tat ca cac so le tu 0 den 100 la: ", tongsole)


