#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import akshare as ak
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import crawling.stock_ths as ths
# 更新股东信息
def get_stock_code():
    try:
        temp_df =  ak.stock_zh_a_spot_em()
        temp_df["code"]=temp_df["代码"]
        temp_df = temp_df[(temp_df["code"].str.startswith('00')|temp_df["code"].str.startswith('30')|temp_df["code"].str.startswith('60')|temp_df["code"].str.startswith('688'))]
        return temp_df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
if __name__ == '__main__':
    get_stock_code()