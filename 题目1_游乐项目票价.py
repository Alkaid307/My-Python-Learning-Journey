# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 10:42:32 2025

@author: 陈倩菲
"""

age = int(input("您的年龄是："))
while True:
    if age <= 14 or age >= 60:
        print("抱歉，您的年龄不符合安全要求")
        break
    # 排除不符合年龄要求的游客
    tour = input("请输入 单次游玩 或 一次往返：")
    # 符合年龄要求的顾客才需要再输入游玩情况
    if tour == '单次游玩':
        print('您的票价为50元')

    elif tour == '一次往返':
        print('您的票价为90元')
        break
    else:
        print('输入不符合要求，请重新输入 单次游玩 或一次往返：')
        
        
