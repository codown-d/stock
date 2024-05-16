#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import current_app
import logging
from core.libs import get_now_date
import crawling.stock_hist_em as she
from core.models import DFCFStockInfo,db
# 读取当天股票数据
def fetch_stocks():
    try:
        df = she.stock_zh_a_spot_em()
        if df is None or len(df.index) == 0:
            return None
        for x in range(0, len(df)):
            item = df.iloc[x].to_dict()
            item['date']=get_now_date()
            if(item['f2']!='-'):
                stock = DFCFStockInfo(**item)
                db.session.add(stock)
        db.session.commit()
        return df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None