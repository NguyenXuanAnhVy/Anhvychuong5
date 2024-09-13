# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:53:51 2024

@author: vy 
"""

# ví dụ while
# while
so= 0
n = int(input("Nhap vao so lan can lap: "))
while (so < n):
    print("Lan lap thu: ", so + 1, "\tBien dem:", so)
    so = so + 1
# while co else
so= 0
n= int(input("Nhap vao so lan can nhap: "))
while (so<n):
    print("Lan lap thu: ", so + 1, "\tBien dem:", so)
    so = so + 1
else:
    print("\nThuc hien lenh trong else, do:", "\nso=", so, "\nn=", n, "\nbool(so<n)=", bool(so<n))
#ví dụ for 
#for in
mau = ["do", "cam", "vang", "luc", "lam", "cham", "tim"]
for i in mau:
    print(i, "\t", len(i))

#for in range(1)
for i in range(10):
    print(i, end='\t')
    
#for in range(2)
for i in range(1, 10, 2):
    print(i, end='\t')
# ví dụ break 
tup= ("do", "cam", "vang", "luc", "lam", "cham", "tim")
for i in tup:
    print(i, "\t")
    if i == "do":
        break
# ví dụ continue 
tup= ("do", "cam", "vang", "luc", "lam", "cham", "tim")
for i in tup:
    if i == "vang" or i == "lam":
        continue
    print(i)
# ví dụ pass 
tup= ("do", "cam", "vang", "luc", "lam", "cham", "tim")
for i in tup:
    pass 