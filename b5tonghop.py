# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:05:14 2024

@author: 
"""
import random
soluong= random.randint(8, 20)
choices = ['keo', 'bua', 'ao']
players = [{'name': f"Nguoi choi {i + 1}", 'choice': None} for i in range(soluong)]
may = random.choice(choices)
print(f"May : {may}\n")
for player in players:
    player['choice'] = random.choice(choices)
    if player['choice'] == may:
         kq= "Hoa"
    elif (player['choice'] == 'keo' and may == 'bao') or \
         (player['choice'] == 'bua' and may == 'keo') or \
         (player['choice'] == 'bao' and may == 'bua'):
        kq= "Thắng"
    else:
        kq= "Thua"
    print(f"{player['name']} chon {player['choice']} - {kq}")   