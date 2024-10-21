#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
from concurrent.futures import ThreadPoolExecutor
import arrow
import numpy as np
import pandas as pd
from tqdm import tqdm
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import crawling.stock_dfcf as dfcf
import crawling.stock_code as stock
def batch_tasks_volume():
    time='2024-07-27'
    path =  f'{cpath}/stock_date/stock_xinlang_vol/{time}.parquet'
    code_df = stock.stock_code()
    code_list= code_df["code"].to_list()
    i = 0
    list_dict={'2024-07-15':pd.DataFrame(),
          '2024-07-16':pd.DataFrame(),
          '2024-07-17':pd.DataFrame(),
          '2024-07-18':pd.DataFrame(),
          '2024-07-19':pd.DataFrame(),
          '2024-07-22':pd.DataFrame(),
          '2024-07-23':pd.DataFrame(),
          '2024-07-24':pd.DataFrame(),
          '2024-07-25':pd.DataFrame(),
          '2024-07-26':pd.DataFrame(),}
    while i < len(code_list):
        code=code_list[i]
        if code.startswith('00'):
            code='sz'+code_list[i]
        elif code.startswith('30'):
            code='sz'+code_list[i]
        elif code.startswith('60'):
            code='sh'+code_list[i]
        elif code.startswith('688'):
            code='sh'+code_list[i]
            
        if code=='sz301226':
            df = fetch_stocks(code)
            
            print(df)
            # for element in list_dict.keys():

                # print(element)
                # print(element,list_dict[time])
                # new_data = df[(df['时间'] >= f'{time} 09:25:00') & (df['时间'] <= f'{time} 15:00:00')]
                # print(new_data)

        i += 1

def fetch_stocks(code):
    try:
        temp_df = dfcf.stock_history_fenshi_detail_xinlang(code)
        temp_df['代码']=code
        new_df=pd.DataFrame()
        new_df['代码']=temp_df['代码'].str[2:]
        new_df['时间']=temp_df['day']
        new_df['开盘']=temp_df['open']
        new_df['最高']=temp_df['high']
        new_df['最低']=temp_df['low']
        new_df['收盘']=temp_df['close']
        new_df['成交量']=pd.to_numeric(temp_df['volume'])
        return new_df
    except Exception as e:
        logging.error(f"stock_history_fenshi_detail处理异常：{e}{code}")
        return {'data':None,'code':code}
if __name__ == '__main__':
    batch_tasks_volume()
    # fetch_stocks('sh600841','2024-07-22')
    
    # data = fetch_stocks('sz301226','2024-07-25')
    # time='2024-07-25'
    # new_data = data[(data['day'] >= f'{time} 09:25:00') & (data['day'] <= f'{time} 15:00:00')]
    # print(new_data)
