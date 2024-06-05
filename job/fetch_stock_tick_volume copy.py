#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
from concurrent.futures import ThreadPoolExecutor,as_completed



cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import crawling.stock_dfcf as dfcf
import crawling.stock_ths as ths
import akshare as ak
from core.utils.commons import calc_pre_minute_change
from core.models import StockTimePrice, get_stock_model
from core.models import db
import crawling.stock_code as stock
# 更新股东信息
def stock_tick_volume():
    try:
        temp_df = stock.stock_code()
        result = temp_df.to_dict(orient='records') 
        with ThreadPoolExecutor(max_workers=100) as executor:
            to_do = []
            for res in result:
                code =res['code']
                if code =='300475':
                    future = executor.submit(fetch_stocks, code)
                    to_do.append(future)
            list=[]
            for future in as_completed(to_do):  # 并发执行
                res_future = future.result()
                temp_df=res_future['date']
                temp_code=res_future['code']
                for i,row in temp_df.iterrows():
                    print(row,row['时间'])
                    list.append(StockTimePrice(时间=row['时间'], 代码=temp_code, 开盘=row['开盘'], 收盘=row['收盘'], 最高=row['最高'], 最低=row['最低'],成交量=row['成交量'],成交额=row['成交额'],均价=row['均价']))
                # tuples =[tuple(x) for x in temp_df.values]
                # print(tuples[0])
                # list.append( StockTimePrice(tuples[0]))
            db.session.add_all(list)

    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
def fetch_stocks(code):
    try:
        stock_zh_a_hist_df = dfcf.stock_history_fenshi_detail(code,"2024-06-04 09:30:00", "2024-06-04 15:00:00")
        return {'date':stock_zh_a_hist_df,'code':code}
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
# main函数入口
if __name__ == '__main__':
    stock_tick_volume()