#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import arrow
import pandas as pd
from tqdm import tqdm
import math

cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import crawling.stock_dfcf as dfcf
from core.models import StockTimePrice
import crawling.stock_code as stock
from core.models import db
import tempfile
# 更新股东信息

def batch_tasks_volume():
    try:
        temp_df = stock.stock_code()
        # temp_df=temp_df[(temp_df["code"] <= '000802')]
        temp_df= temp_df["code"].to_list()
        step=400
        cycle=math.ceil(len(temp_df)/step)
        for num in tqdm(list(range(cycle))):
            code_list = temp_df[step*num:step*(num+1)]
            stock_tick_volume(code_list)
    except Exception as e:
        logging.error(f"batch_tasks_volume处理异常：{e}")
    return None

def stock_tick_volume(code_list):
    try:
        new_df = pd.DataFrame()
        results = run(fetch_stocks, code_list)
        for res in results:
            temp_df = res['data']
            temp_code = res['code']
            if temp_df is not None:
                temp_df['代码']=temp_code
                temp_df['ID']=temp_df['时间']+'_'+temp_df['代码']
                new_df=pd.concat([new_df,temp_df],axis=0, ignore_index=True)
        data_list = [{
            'ID': row["ID"], 
            '时间': row["时间"], 
            "代码": row['代码'], 
            "开盘": row['开盘'], 
            "收盘": row['收盘'], 
            "最高": row['最高'], 
            "最低": row['最低'], 
            "成交量": row['成交量'], 
            "成交额": row['成交额'], 
            "均价": row['均价'], 
            } for index,row in new_df.iterrows()]
        if len(data_list):
            inser_ignore =  StockTimePrice.__table__.insert().prefix_with('IGNORE').values(data_list)
            db.session.execute(inser_ignore)
            db.session.commit()
        return "add success"
    except Exception as e:
        logging.error(f"stock_tick_volume处理异常：{e}")
    return None
def run(f, my_iter):
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(tqdm(executor.map(f, my_iter), total=len(my_iter)))
    return results
def fetch_stocks(code,time=arrow.now().format("YYYY-MM-DD")):
    
    err_coor_path=f'{cpath}/stock_date/{time}_error_code.csv'
    time='2024-06-03'
    try:
        temp_df = dfcf.stock_history_fenshi_detail(code,f"{time} 09:25:00", f"{time} 15:00:00")
        return {'data':temp_df,'code':code}
    except Exception as e:
        logging.error(f"stock_history_fenshi_detail处理异常：{e}{code}")
        try:
            err_code_df =  pd.read_csv(err_coor_path,dtype={'error_code': str,})
            err_code_df.loc[len(err_code_df.index)] = [code]
            # err_code_df = err_code_df.drop(err_code_df[err_code_df['error_code'] == '023030'].index)
            err_code_df.to_csv(err_coor_path, mode='w', index=False, header=True, sep=',')
        except Exception as e:
            df = pd.DataFrame([code],columns=['error_code'])
            df.to_csv(err_coor_path, mode='w', index=False, header=True, sep=',')
        return {'data':None,'code':code}
# main函数入口
if __name__ == '__main__':
    batch_tasks_volume('123')
    # stock_tick_volume()
    # res=fetch_stocks('000001')
    # print(res['data'])