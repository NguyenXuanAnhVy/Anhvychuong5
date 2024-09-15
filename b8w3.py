# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:56:47 2024

@author: 
"""
import random
n= 10
songaunhien= [random.random() for _ in range(n)]
tong= sum(songaunhien)
nhonhat= min(songaunhien)
lonnhat= max(songaunhien)
trungbinh= tong/n
print("Trung binh: " + str(trungbinh))
print("So nho nhat: " + str(nhonhat))
print("So lon nhat: " + str(lonnhat))
