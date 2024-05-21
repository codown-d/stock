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
        print(df)
        if df is None or len(df.index) == 0:
            return None
        data =  df.to_dict(orient='records')
        print(type(data),data[0],len(data))
        DFCFStockInfo.insert_or_update_all([{'f2': 40.86, 'f3': 20.0, 'f4': 6.81, 'f5': 260875, 'f6': 1031647307.0, 'f7': 12.31, 'f8': 12.79, 'f9': 50.37, 'f10': 4.69, 'f11': 0.0, 'f12': '688559', 'f14': '海目星', 'f15': 40.86, 'f16': 36.67, 'f17': 37.0, 'f18': 34.05, 'f20': 8333887320, 'f21': 8333887320, 'f22': 0.0, 'f23': 3.49, 'f24': 52.75, 'f25': 14.45, 'f26': 20200909, 'f37': 1.75, 'f38': 203962000.0, 'f39': 203962000.0, 'f40': 1047962891.87, 'f41': 17.0436549329, 'f45': 41361785.72, 'f46': 31.010608351209, 'f48': 5.456738091507, 'f49': 26.5208604919, 'f57': 77.9633749126, 'f61': 5.530603446917, 'f100': '专用设备', 'f112': 0.202791626, 'f113': 11.695093687, 'f114': 25.9, 'f115': 25.14, 'f221': 20240331, 'date': '2024-05-21'}])
        return df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None

if __name__ == '__main__':
    # fetch_stocks()
    DFCFStockInfo.insert_or_update_all([{'f2': 40.86, 'f3': 20.0, 'f4': 6.81, 'f5': 260875, 'f6': 1031647307.0, 'f7': 12.31, 'f8': 12.79, 'f9': 50.37, 'f10': 4.69, 'f11': 0.0, 'f12': '688559', 'f14': '海目星', 'f15': 40.86, 'f16': 36.67, 'f17': 37.0, 'f18': 34.05, 'f20': 8333887320, 'f21': 8333887320, 'f22': 0.0, 'f23': 3.49, 'f24': 52.75, 'f25': 14.45, 'f26': 20200909, 'f37': 1.75, 'f38': 203962000.0, 'f39': 203962000.0, 'f40': 1047962891.87, 'f41': 17.0436549329, 'f45': 41361785.72, 'f46': 31.010608351209, 'f48': 5.456738091507, 'f49': 26.5208604919, 'f57': 77.9633749126, 'f61': 5.530603446917, 'f100': '专用设备', 'f112': 0.202791626, 'f113': 11.695093687, 'f114': 25.9, 'f115': 25.14, 'f221': 20240331, 'date': '2024-05-21'}])
       