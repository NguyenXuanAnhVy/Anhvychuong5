# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:28:44 2024

@author: 
"""
#B46
tong= 979
for x in range(1, tong//2+1):
    for y in range(1, tong//7+1):
        for z in range(1, tong//9+1):
            if 2 * x + 7 * y + 9 * z == tong:
                print("x =", x, "y =", y, "z =", z)
#B47
tong= 979
solonnhat= 0
bonghiem= [[0, 0, 0]]*1
for x in range(1, tong//2+1):
    for y in range(1, tong//7+1):
        for z in range(1, tong//9+1):
            if 2 * x + 7 * y + 9 * z == tong:
                lonnhat= x+y+z
                if lonnhat > solonnhat:
                    solonnhat = lonnhat
                    bonghiem= [[x, y, z]]
                elif lonnhat == solonnhat:
                    bonghiem += [[x, y, z]]
i= 0
while i < len(bonghiem):
    print("x =", bonghiem[i][0], "y =", bonghiem[i][1], "z =", bonghiem[i][2])
    i += 1
#B48
tong= 979
sonhonhat= 0
bonghiem= [[0, 0, 0]]*1
for x in range(1, tong//2+1):
    for y in range(1, tong//7+1):
        for z in range(1, tong//9+1):
            if 2 * x + 7 * y + 9 * z == tong:
                nhonhat= x+y+z
                if nhonhat < sonhonhat:
                    sonhonhat = nhonhat
                    bonghiem= [[x, y, z]]
                elif nhonhat == sonhonhat:
                    bonghiem += [[x, y, z]]
i= 0
while i < len(bonghiem):
    print("x =", bonghiem[i][0], "y =", bonghiem[i][1], "z =", bonghiem[i][2])
    i += 1


