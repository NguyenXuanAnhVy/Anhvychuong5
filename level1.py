# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:13:13 2024

@author: 
"""
#1
for i in range(11):
    print(i)
#2
i= 0
while i <= 10:
    print(i)
    i += 1
#3
cot= 8
dong= 8
for _ in range(cot):
    print('#' * dong)
#4
for i in range(2, 10):
    print(str(i) + '\t')
    for j in range(1, 11):
        ketqua= i*j
        print(str(i) + "x" + str(j) + "=" + str(ketqua))
#5
for i in range(0, 101, 2):
    print(i)
#6
for i in range(1, 101, 2):
    print(i)


