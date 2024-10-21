#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
from concurrent.futures import ThreadPoolExecutor
import arrow
import pandas as pd
from tqdm import tqdm
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import crawling.stock_dfcf as dfcf
import crawling.stock_code as stock
def batch_tasks_volume():
    time='2024-10-18'
    try:
        path =  f'{cpath}/stock_date/stock_vol/{time}.parquet'
        temp_df= stock_tick_volume(time)
        temp_df.to_parquet(path, compression= 'gzip')
    except Exception as e:
        logging.error(f"batch_tasks_volume处理异常：{e}")
    return None

def stock_tick_volume(time):
    try:
        code_df = stock.stock_code()
        code_list= code_df["code"].to_list()
        code_list.sort(reverse = False)
        new_df = pd.DataFrame()
        results = run(lambda x: fetch_stocks(x, time) , code_list)
        for temp_df in results:
            if temp_df is not None:
                new_df=pd.concat([new_df,temp_df],axis=0, ignore_index=True)
        return new_df
    except Exception as e:
        logging.error(f"stock_tick_volume处理异常：{e}")
    return None
def run(f, my_iter):
    with ThreadPoolExecutor(max_workers=12) as executor:
        results = list(tqdm(executor.map(f, my_iter), total=len(my_iter)))
    return results
def fetch_stocks(code,time=arrow.now().format("YYYY-MM-DD")):
    try:
        temp_df = dfcf.stock_history_fenshi_detail(code,f"{time} 09:25:00", f"{time} 15:00:00")
        temp_df['代码']=code
        return temp_df
    except Exception as e:
        logging.error(f"stock_history_fenshi_detail处理异常：{e}{code}")
        err_coor_path=f'{cpath}/stock_date/{time}_error_code.csv'
        try:
            err_code_df =  pd.read_csv(err_coor_path,dtype={'error_code': str,})
            err_code_df.loc[len(err_code_df.index)] = [code]
            err_code_df.to_csv(err_coor_path, mode='w', index=False, header=True, sep=',')

        except Exception as e:
            df = pd.DataFrame([code],columns=['error_code'])
            df.to_csv(err_coor_path, mode='w', index=False, header=True, sep=',')
        return {'data':pd.DataFrame(),'code':code}
if __name__ == '__main__':
    batch_tasks_volume()
    
    # new_data = fetch_stocks('600841','2024-07-22')  
    # print(new_data)
