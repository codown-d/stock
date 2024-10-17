#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
from concurrent.futures import ThreadPoolExecutor
import time
import arrow
import pandas as pd
from tqdm import tqdm
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import crawling.stock_dfcf as dfcf
import crawling.stock_code as stock
def batch_tasks_volume():
    t='2024-07-29'
    try:
        path =  f'{cpath}/stock_date/stock_vol/{t}.parquet'
        temp_df= stock_tick_volume(t)
        print(temp_df)
        temp_df.to_parquet(path, compression= 'gzip')
    except Exception as e:
        logging.error(f"batch_tasks_volume处理异常：{e}")
    return None

def stock_tick_volume(t):
    try:
        code_df = stock.stock_code()
        code_list= code_df["code"].to_list()
        code_list.sort(reverse = False)
        new_df = pd.DataFrame()
        progress = tqdm(total=len(code_list), desc="Processing")
        while len(code_list):
            progress.update(1)
            code = code_list.pop()
            temp_df = fetch_stocks(code,t)
            time.sleep(2)
            new_df=pd.concat([new_df,temp_df],axis=0, ignore_index=True)
        progress.close()
        return new_df
    except Exception as e:
        logging.error(f"stock_tick_volume处理异常：{e}")
    return None
def run(f, my_iter):
    time.sleep(3)
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
        return {'data':None,'code':code}
if __name__ == '__main__':
    batch_tasks_volume()
    
    # new_data = fetch_stocks('688328','2024-07-29')  
    # print(new_data)
