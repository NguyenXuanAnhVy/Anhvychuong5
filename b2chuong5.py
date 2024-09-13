# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:38:02 2024

@author: 
"""
sochan= [number for number in range(2020, 3839)if number % 2==0]
chia9= [number for number in range(2020, 3839)if number % 9==0]
danhsach= len(chia9)
for i in range(danhsach):
    if i < danhsach - 1:
        print(chia9[i], end='\t')
    else:
        print(chia9[i])
