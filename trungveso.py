# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:03:40 2024

@author: 
"""
import random
vesonhanh= [[], [], [], [], []]
for k in range(5):
    ve= random.sample(range(1, 46), 6)
    for i in range(len(ve)):
        for j in range(0, len(ve) - i - 1):
            if ve[j] > ve[j + 1]:
                ve[j], ve[j + 1] = ve[j + 1], ve[j]
    vesonhanh[k] = ve
daysotrungthuong= random.sample(range(1, 46), 6)
for i in range(len(daysotrungthuong)):
    for j in range(0, len(daysotrungthuong) - i - 1):
        if daysotrungthuong[j] > daysotrungthuong[j + 1]:
            daysotrungthuong[j], daysotrungthuong[j + 1]= daysotrungthuong[j + 1], daysotrungthuong[j]
print("Day so trung thuong: ", daysotrungthuong)
tongtien= 0
giaveso= 10000
for ve in vesonhanh:
    print("Ve so: ", ve)
    sotrung = len(set(ve).intersection(daysotrungthuong))
    if sotrung == 6:
        tienthuong= 10000000000
    elif sotrung == 5:
        tienthuong= 10000000
    elif sotrung == 4:
        tienthuong= 300000
    elif sotrung == 3:
        tienthuong= 30000
    else:
        tienthuong= 0
    print("So trung: ", sotrung)
    print("Tien thuong cho ve trung thuong: ", tienthuong)
    tongtien += tienthuong
print("Tong so tien nguoi choi nhan duoc: ", tongtien)

        