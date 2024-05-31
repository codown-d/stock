#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import logging
import os.path
import sys
import os
import pandas as pd   #将数据保存至相应文件中
import arrow
from concurrent.futures import ThreadPoolExecutor,as_completed
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

from core.utils.commons import gp_type_szsh
import akshare as ak
def fetch_stocks_all_code():
    try:
        stock_info_a_code_name_df = ak.stock_info_a_code_name()
        result = stock_info_a_code_name_df.to_dict(orient='records') 
        with ThreadPoolExecutor(max_workers=1000) as executor:
            to_do = []
            for res in result:
                code = res['code']
                if(gp_type_szsh(code)==True and int(code)<1000):
                    future = executor.submit(fetch_stocks, code)
                    to_do.append(future)
            for future in as_completed(to_do):  # 并发执行
                d = future.result()
                code = d['code']
                date = d['date']
                date.to_csv(f'{cpath}/stock_date/csv/basic/{code}.csv', mode='w', index=False, header=True, sep=',')
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
def fetch_trade_day(n):
    try:
        time = arrow.now().format("YYYY-MM-DD")
        df = ak.tool_trade_date_hist_sina()
        df['trade_date']= pd.to_datetime(df['trade_date'])
        start_date = pd.to_datetime('2019-01-01')
        end_date = pd.to_datetime(time)
        df_filtered = df[(df['trade_date'] >= start_date) & (df['trade_date'] <= end_date)]
        print(df_filtered)
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
# 历史数据
time = arrow.now().format("YYYYMMDD")
def fetch_stocks(code):
    try:
        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period="daily", start_date="20200101", end_date=time, adjust="")
        print(code)
        return {'date':stock_zh_a_hist_df,'code':code}
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None

# main函数入口
if __name__ == '__main__':
    fetch_stocks_all_code() 