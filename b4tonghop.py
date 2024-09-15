# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:47:36 2024

@author: 
"""
import random
luachon= ['keo', 'bua', 'bao']
diemnguoi= 0
diemmay= 0
while True:
    nguoi= input("Nhap lua chon cua ban(keo, bua, bao) hoac 'thoat' de ket thuc: ")
    if nguoi == 'thoat':
       break
    if nguoi not in luachon:
        print("Lua chon khog hop le. Vui long chon lai.")
        continue
    may= random.choice(luachon)
    print("May ra: ", may)
    if nguoi == may:
        ketqua= "Hoa"
    elif (nguoi == 'keo' and may == 'bao') or (nguoi == 'bao' and may == 'bua') or (nguoi == 'bua' and may == 'keo'):
        ketqua= "Nguoi thang."
        diemnguoi += 1
    else:
        ketqua= "May thang."
        diemmay += 1
    print("=> Ket qua: ", ketqua)
    print("Diem nguoi: ", diemnguoi, "Diem may: ", diemmay)
print("Tro choi ket thuc.")
print("Diem cuoi cung - Nguoi: ", diemnguoi, "Diem may: ", diemmay)