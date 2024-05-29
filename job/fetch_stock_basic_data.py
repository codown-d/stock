#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import logging
import os.path
import sys
import os    #获取当前工作路径
import pandas as pd   #将数据保存至相应文件中
import arrow

cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)
from core.utils.commons import gp_type_szsh
import akshare as ak

def fetch_stocks_all_code():
    try:
        stock_info_a_code_name_df = ak.stock_info_a_code_name()
        result = stock_info_a_code_name_df.to_dict(orient='records')
        for res in result:
            if(gp_type_szsh(res['code'])==True,res['code']=='000001'):
                fetch_stocks(res['code'])
        # fetch_stocks()
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
def fetch_trade_day(n):
    try:
        now_time = datetime.datetime.now()
        time = arrow.now().format("YYYY-MM-DD")
        df = ak.tool_trade_date_hist_sina()
        print(now_time,type(df['trade_date']))
        df[df['trade_date']>now_time]
        print(df)
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None

def fetch_stocks(code):
    try:
        time = arrow.now().format("YYYYMMDD")
        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code, period="daily", start_date="20240101", end_date=time, adjust="")
        result = stock_zh_a_hist_df.to_dict(orient='records')
        # with pd.ExcelWriter(f'{cpath}/stock_date/stock.xlsx') as writer:
        #     for res in result:
        #         time = res['日期'].strftime('%Y%m%d')
        #         new_date=pd.DataFrame([res])
        #         new_date.to_excel(writer, sheet_name=time,index=False)
        print(code)
        return stock_zh_a_hist_df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
# main函数入口
if __name__ == '__main__':
    fetch_trade_day(60) 