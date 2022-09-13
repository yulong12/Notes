
from jqdatasdk import *
import pandas as pd
# import time
auth("18811158173","demo123Demo")

# df=get_all_securities(types=['stock'])
# print(df[:2])
# 设置行列不忽略
pd.set_option('display.max_rows',100000)
pd.set_option('display.max_columns',10)
'''resample函数的使用'''
#转换周期：日K转换为周K
df=get_price('000001.XSHG',count=20,end_date='2022-02-22',frequency='daily',panel=False)
df['weekday']=df.index.weekday

print(df)
# 获取周K（当周的）：开盘价（当周第一天）、收盘价（当周最后一天）、最高价（当周）、最低价（当周）
df_week=pd.DataFrame()
df_week['open'] =df['open'].resample('W').first()
df_week['close'] =df['close'].resample('W').last()
df_week['high'] =df['high'].resample('W').max()
df_week['low'] =df['low'].resample('W').min()

print(df_week)

#汇总统计：统计一下月成交量、成交额(Sum)
df_week['volume(sum)']=df['volume'].resample('W').sum()
df_week['money(sum)']=df['money'].resample('W').sum()

print(df_week)