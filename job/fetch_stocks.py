#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import crawling.stock_hist_em as she
from core.models import DFCFStockInfo,db
from flask import Flask,current_app
# 读取当天股票数据
def fetch_stocks():
    try:
        df = she.stock_zh_a_spot_em()
        
        print('1213123',current_app.name)
        if df is None or len(df.index) == 0:
            return None
        for x in range(0, len(df)):
            item = df.iloc[x].to_dict()
            # print(type(item),item['f2'],item)
            stock = DFCFStockInfo(item)
            db.session.add(stock)
        db.session.commit()
        # if date is None:
        #     data.insert(0, 'date', datetime.datetime.now().strftime("%Y-%m-%d"))
        # else:
        #     data.insert(0, 'date', date.strftime("%Y-%m-%d"))
        # data.columns = list(tbs.TABLE_CN_STOCK_SPOT['columns'])
        # data = data.loc[data['code'].apply(is_a_stock)].loc[data['new_price'].apply(is_open)]
        return df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None