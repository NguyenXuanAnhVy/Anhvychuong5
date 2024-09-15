# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:07:05 2024

@author: 
"""
import math
giatri= [2, 4, 8, 16, 32, 64, 128]
print("n\tlog(n)\tn*log(n)\tn^2\t\tn^3")
for n in giatri:
    log_n= math.log(n)
    n_log_n= n*log_n
    n_cb2= n**2
    n_cb3= n**3
    log_n_chuoi= str(round(log_n, 2))
    n_log_n_chuoi= str(round(n_cb2, 2))
    n_cb2_chuoi= str(n_cb2)
    n_cb3_chuoi= str(n_cb3)
    print(str(n) + "\t" + log_n_chuoi + "\t" + n_log_n_chuoi + "\t" + n_cb2_chuoi + "\t" + n_cb3_chuoi)
