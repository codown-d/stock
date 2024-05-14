#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os.path
import sys
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current, os.pardir))
sys.path.append(cpath)
import crawling.stock_hist_em as she
from models import StockStats
from core import db
# 读取当天股票数据
def fetch_stocks():
    try:
        data = she.stock_zh_a_spot_em()
        if data is None or len(data.index) == 0:
            return None
        print(data.columns)
        stock = StockStats(
            username='',
            email='',
        )
        db.session.add(stock)
        # if date is None:
        #     data.insert(0, 'date', datetime.datetime.now().strftime("%Y-%m-%d"))
        # else:
        #     data.insert(0, 'date', date.strftime("%Y-%m-%d"))
        # data.columns = list(tbs.TABLE_CN_STOCK_SPOT['columns'])
        # data = data.loc[data['code'].apply(is_a_stock)].loc[data['new_price'].apply(is_open)]
        return data
    except Exception as e:
        logging.error(f"stockfetch.fetch_stocks处理异常：{e}")
    return None
if __name__ == "__main__":
    fetch_stocks()