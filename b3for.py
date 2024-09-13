# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:32:22 2024

@author: 
"""
#3a 
import random 
sophantu= random.randint(20, 30)
phantu= [random.randint(20, 30)for _ in range(sophantu)]
print("So luong phan tu trong danh sach: ", sophantu)
print("Danh sach cac phan tu: ", phantu)

#3b
import random 
so_phan_tu= random.randint(20, 30)
binhphuong= [random.uniform (18, 99)**2 for _ in range(so_phan_tu)]
print("So luong phan tu trong danh sach: ", so_phan_tu)
print("Danh sach cac gia tri binh phuong: ", binhphuong)

