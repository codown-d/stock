#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from math import ceil, floor
import pandas as pd
import logging
import os.path
import sys
from core.utils.commons import get_time_date_trend, gp_type_szsh
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import crawling.stock_ths as ths
from core.models import  Shareholder
# 更新股东信息
def fetch_shareholder():
    try:
        df = ths.stock_shareholder_history()
        df=df.where(df.notnull(), None)
        if df is None or len(df.index) == 0:
            return None
        items = filter(gp_type_szsh,df.to_dict(orient='records') )
        print(items)
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
            trend_list=get_time_date_trend(info)
            d1=trend_list[0]
            d3=trend_list[-1]
            if(d1 and d3):
                shareholder_level_per=floor((d3-d1)/d3*10000)/100
                if shareholder_level_per >10:
                    shareholder_level='t0'
                elif shareholder_level_per <=10 and shareholder_level_per >0:
                    shareholder_level='t1'
                elif shareholder_level_per <=0 and shareholder_level_per >-10:
                    shareholder_level='t2'
                else:
                    shareholder_level='t3'
                d['shareholder_level_per'] =shareholder_level_per
                d['shareholder_level'] =shareholder_level
                list.append(d)
        Shareholder.insert_or_update_all(list)
        return df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
       