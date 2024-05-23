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
from core.models import DFCFStockInfo
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

if __name__ == '__main__':
    fetch_stocks()
    #DFCFStockInfo.insert_or_update_all([{'f2': 5.44, 'f3': 20.09, 'f4': 0.91, 'f5': 885799, 'f6': 442341123.69, 'f7': 20.53, 'f8': 26.81, 'f9': -437.81, 'f10': 2.88, 'f11': 0.0, 'f12': '300155', 'f14': '安居宝', 'f15': 5.44, 'f16': 4.51, 'f17': 4.51, 'f18': 4.53, 'f20': 3053078927, 'f21': 1797374390, 'f22': 0.0, 'f23': 2.33, 'f24': 62.87, 'f25': -8.11, 'f26': 20110107, 'f37': -0.13, 'f38': 561227744.0, 'f39': 330399704.0, 'f40': 45814182.64, 'f41': -30.0323928509, 'f45': -1743368.99, 'f46': -185.840738775654, 'f48': 0.430823999196, 'f49': 44.6342402978, 'f57': 10.5485145967, 'f61': 0.770637335242, 'f100': '计算机设备', 'f112': -0.003106349, 'f113': 2.329998907, 'f114': -77.92, 'f115': -71.07, 'f221': 20240331, 'date': '2024-05-22', 'id': '2024-05-22_300155'}])
       