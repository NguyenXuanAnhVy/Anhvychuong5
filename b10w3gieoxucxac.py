# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:03:41 2024

@author: tienx
"""
import random
gieoxucxac = 1000000  
solanitnhat_1_6 = 0
for _ in range(gieoxucxac):
    lan_1 = 0
    for _ in range(6):
        if random.randint(1, 6) == 1:
            lan_1 += 1
    if lan_1 >= 1:
        solanitnhat_1_6 += 1
solanitnhat2so_1_12 = 0
for _ in range():
    _1 = 0
    for _ in range(12):
        if random.randint(1, 6) == 1:
            _1 += 1
    if lan_1 >= 2:
        solanitnhat2so_1_12 += 1
xacsuat_1_6 = solanitnhat_1_6 / gieoxucxac
xacsuat_1_12 = solanitnhat2so_1_12 / gieoxucxac
print("Xác suất để có ít nhất một số 1 khi gieo xúc xắc 6 lần là: " + str(xacsuat_1_6))
print("Xác suất để có ít nhất hai số 1 khi gieo xúc xắc 12 lần là: " + str(xacsuat_1_12))

