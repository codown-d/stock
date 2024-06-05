#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
from concurrent.futures import ThreadPoolExecutor,as_completed
import pandas as pd

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
        result = temp_df.to_dict(orient='records') 
        new_df = pd.DataFrame()
        with ThreadPoolExecutor(max_workers=100) as executor:
            to_do = []
            for res in result:
                code =res['code']
                # if code <='0000050':
                future = executor.submit(fetch_stocks, code)
                to_do.append(future)
            for future in as_completed(to_do):  # 并发执行
                res_future = future.result()
                temp_df=res_future['date']
                temp_code=res_future['code'] 
                temp_df['代码']=temp_code
                temp_df['ID']=temp_df['时间']+'_'+temp_df['代码']
                new_df=pd.concat([new_df,temp_df])
            print(new_df)
            # db.session.execute(
            # StockTimePrice.__table__.insert(),
            # [{
            #     "ID": row['ID'], 
            #     "时间": row['时间'], 
            #     "代码": row['代码'], 
            #     "开盘": row['开盘'], 
            #     "收盘": row['收盘'], 
            #     "最高": row['最高'], 
            #     "最低": row['最低'], 
            #     "成交量": row['成交量'], 
            #     "成交额": row['成交额'], 
            #     "均价": row['均价'], 
            #     } for index,row in temp_df.iterrows()]
            # )
            # db.session.commit()
                
                # temp_df =  temp_df.to_dict(orient='records')
                # StockTimePrice.insert_or_update_all(temp_df)
            return "add success"
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
def fetch_stocks(code):
    try:
        temp_df = dfcf.stock_history_fenshi_detail(code,"2024-06-05 09:30:00", "2024-06-05 15:00:00")
        return {'date':temp_df,'code':code}
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
# main函数入口
if __name__ == '__main__':
    stock_tick_volume()