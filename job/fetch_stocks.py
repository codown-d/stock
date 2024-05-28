#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os.path
import sys
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

from core.libs import get_now_date
import crawling.stock_hist_em as she
import crawling.stock_ths as ths
from core.models import DFCFStockInfo, Shareholder
# 读取当天股票数据
def fetch_stocks():
    try:
        df = she.stock_zh_a_spot_em()
        df['date']=get_now_date()
        df['id']= df['date']+'_'+ df['f12']
        print('df',df)
        if df is None or len(df.index) == 0:
            return None
        data =  df.to_dict(orient='records')
        DFCFStockInfo.insert_or_update_all(data)
        return df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
       