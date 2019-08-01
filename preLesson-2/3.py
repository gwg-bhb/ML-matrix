#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019-07-31 11:09
#@Author: daemon
#@File  : 3.py.py

import pandas as pd
import numpy as np

df1=pd.DataFrame(np.random.randn(4,4),index=list('ABCD'),columns=list('1234'))

print("1th")
print(df1)

df2=pd.DataFrame([[1,2,3,4],[2,3,4,5],[3,4,5,6]],index=list('ABC'),columns=list('ABCD'))

print("2th")
print(df2)
print(df2.shape[0])
print(df2.shape[1])
print(df2.T)

dic1={'name':['小明','小红','狗蛋','铁柱'],'age':[17,20,5,40],'gender':['男','女','女','男']}
df3=pd.DataFrame(dic1)

print("3th")
print(df3.dtypes)

df4=pd.DataFrame(np.random.randn(6,6))

print("4th")
print(df4.head())
print("5th")
print(df4.tail())

print("6th")
print(df2.index)
print(df1.columns)
print(df1.values)
print(df3['name'].values)

print("7th")
print(df1.loc['A'])
print(df1.iloc[0])