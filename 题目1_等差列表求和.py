# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 09:07:44 2025

@author: 陈倩菲
"""

# 根据起始项a₁和步长值，可以对等差数列求和，即a₁+ a₂+……+an的值
n = int(input("请输入n的值（n为整数）："))
d = int(input("请输入步长d的值："))
a = int(input("请输入起始项a₁的值："))
# 输入n、d、a₁值
sum_range = 0
# 设置储存列表之和的变量，并预设为0
for x in range(1,n+1):
    an = a+(x-1)*d
    sum_range += an
# 将遍历的值累加到预设的变量
print("a₁+ a₂+……+an的值为",sum_range)
# 打印最后的结果

