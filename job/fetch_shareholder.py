#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os.path
import sys
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import crawling.stock_hist_em as she
import crawling.stock_ths as ths
from core.models import  Shareholder
# 更新股东信息
def fetch_shareholder():
    try:
        df = ths.stock_shareholder_history()
        df=df.where(df.notnull(), None)
        if df is None or len(df.index) == 0:
            return None
        items = df.to_dict(orient='records')
        list=[]
        columns=['code','name','price','price_range','shareholder_count','shareholder_chigu_shuliang','shareholder_chigu_shizhi','shareholder_chigu_bili']
        for item in items:
            d=dict()
            info=dict()
            for key in item:
                if key in columns:
                    d[key]=item[key]
                else:
                    info[key]=item[key]
            d['info']=info
            list.append(d)
        print(list)
        Shareholder.insert_or_update_all(list)
        return df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
       