#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
from tqdm import tqdm

cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import crawling.stock_dfcf as dfcf
from core.models import StockTimePrice
import crawling.stock_code as stock
from core.models import db
# 更新股东信息
def stock_tick_volume():
    try:
        temp_df = stock.stock_code()
        temp_df=temp_df[(temp_df["code"] <= '300618')]
        # temp_df=temp_df[(temp_df["code"] >= '000508') & (temp_df["code"] <= '000618')]
        columns=['ID', '时间', "代码", "开盘", "收盘",  "最高", "最低", "成交量", "成交额", "均价", ]
        new_df = pd.DataFrame(columns=columns)
        print(new_df)
        my_iter= temp_df["code"].to_list()
        results = run(fetch_stocks, my_iter)
        for res in results:
            temp_df = res['data']
            temp_code = res['code']
            if temp_df is not None:
                temp_df['代码']=temp_code
                temp_df['ID']=temp_df['时间']+'_'+temp_df['代码']
                new_df=pd.concat([new_df,temp_df])
        print(new_df)
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
            } for index,row in temp_df.iterrows()]
        if len(data_list):
            inser_ignore =  StockTimePrice.__table__.insert().prefix_with('OR IGNORE').values(data_list)
            db.session.execute(inser_ignore)
            db.session.commit()
        return "add success"
    except Exception as e:
        logging.error(f"stock_tick_volume处理异常：{e}")
    return None
def run(f, my_iter):
    with ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(f, my_iter), total=len(my_iter)))
    return results
def fetch_stocks(code):
    try:
        temp_df = dfcf.stock_history_fenshi_detail(code,"2024-06-04 09:25:00", "2024-06-04 15:00:00")
        return {'data':temp_df,'code':code}
    except Exception as e:
        logging.error(f"stock_history_fenshi_detail处理异常：{e}{code}")
        return {'data':None,'code':code}
# main函数入口
if __name__ == '__main__':
    stock_tick_volume()
    # res=fetch_stocks('000509')
    # print(res['data'])