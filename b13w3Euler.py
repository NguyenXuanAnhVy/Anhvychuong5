# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:59:29 2024

@author: 
"""
tim= False
gioihan= 100
for a in range(1, gioihan):
    for b in range(a, gioihan):
        for c in range(b, gioihan):
            for d in range(c, gioihan):
                e5= a**5 + b**5 + c**5 + d**5
                e= int(round(e5**(1/5)))
                if e**5 == e5 and e > d:
                    print(a, b, c, d, e)
                    tim= True
                    break
            if tim:
                break
        if tim:
            break
    if tim:
        break
    
