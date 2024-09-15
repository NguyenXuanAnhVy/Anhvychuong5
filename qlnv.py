# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:33:46 2024

@author: 
"""
# Danh sách nhân viên văn phòng
nv_van_phong_list = [
    {'ma_nv': 'NV001', 'ho_ten': 'Nguyen Van A', 'luong_co_ban': 5000, 'luong_hang_thang': 6000, 'so_ngay': 20},
    {'ma_nv': 'NV002', 'ho_ten': 'Tran Thi B', 'luong_co_ban': 5200, 'luong_hang_thang': 6200, 'so_ngay': 22},
    {'ma_nv': 'NV003', 'ho_ten': 'Le Van C', 'luong_co_ban': 4800, 'luong_hang_thang': 5800, 'so_ngay': 18},
    {'ma_nv': 'NV004', 'ho_ten': 'Hoang Thi D', 'luong_co_ban': 5300, 'luong_hang_thang': 6300, 'so_ngay': 21},
    {'ma_nv': 'NV005', 'ho_ten': 'Pham Van E', 'luong_co_ban': 4900, 'luong_hang_thang': 5900, 'so_ngay': 19}
]

# Danh sách nhân viên bán hàng
nv_ban_hang_list = [
    {'ma_nv': 'NV006', 'ho_ten': 'Nguyen Thi F', 'luong_co_ban': 4500, 'luong_hang_thang': 5500, 'so_san_pham': 100},
    {'ma_nv': 'NV007', 'ho_ten': 'Vu Van G', 'luong_co_ban': 4600, 'luong_hang_thang': 5600, 'so_san_pham': 110},
    {'ma_nv': 'NV008', 'ho_ten': 'Dao Thi H', 'luong_co_ban': 4700, 'luong_hang_thang': 5700, 'so_san_pham': 120},
    {'ma_nv': 'NV009', 'ho_ten': 'Do Van I', 'luong_co_ban': 4800, 'luong_hang_thang': 5800, 'so_san_pham': 130},
    {'ma_nv': 'NV010', 'ho_ten': 'Nguyen Thi J', 'luong_co_ban': 4900, 'luong_hang_thang': 5900, 'so_san_pham': 140}
]

# In thông tin của tất cả các nhân viên văn phòng
print("Nhân viên văn phòng:")
i = 0
while i < len(nv_van_phong_list):
    nv = nv_van_phong_list[i]
    print("Mã NV:", nv['ma_nv'])
    print("Họ và tên:", nv['ho_ten'])
    print("Lương cơ bản:", nv['luong_co_ban'])
    print("Lương hàng tháng:", nv['luong_hang_thang'])
    print("Số ngày làm việc:", nv['so_ngay'])
    print()
    i += 1

# In thông tin của tất cả các nhân viên bán hàng
print("Nhân viên bán hàng:")
i = 0
while i < len(nv_ban_hang_list):
    nv = nv_ban_hang_list[i]
    print("Mã NV:", nv['ma_nv'])
    print("Họ và tên:", nv['ho_ten'])
    print("Lương cơ bản:", nv['luong_co_ban'])
    print("Lương hàng tháng:", nv['luong_hang_thang'])
    print("Số sản phẩm bán được:", nv['so_san_pham'])
    print()
    i += 1
