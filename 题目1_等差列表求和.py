# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 09:07:44 2025

@author: 陈倩菲
"""

n = int(input("请输入n的值（n为整数）："))
# 输入n值
sum_range = 0
# 设置储存列表之和的变量，并预设为0
for x in range(1,n*2,2):
# 由于题目中的等差列表步长值为2，因此设置结束值为n*2
    sum_range += x
# 将遍历的值累加到预设的变量
print("a₁+ a₂+……+an的值为",sum_range)
# 打印最后的结果

