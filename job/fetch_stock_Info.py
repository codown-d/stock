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
import pandas as pd
# 更新股东信息
def stock_code():
    path = f'{cpath}/stock_date/stock_code.csv'
    try:
        csvframe = pd.read_csv(path,dtype={'code': str,})
        return csvframe
    except Exception as e:
        temp_df =  ak.stock_zh_a_spot_em()
        print(temp_df)
        temp_df["code"]=temp_df["代码"]
        temp_df = temp_df[(temp_df["code"].str.startswith('00')|temp_df["code"].str.startswith('30')|temp_df["code"].str.startswith('60')|temp_df["code"].str.startswith('688'))]
        new_df = pd.DataFrame({
            'code':temp_df['code'],
            'name':temp_df['名称'],
            })
        new_df.to_csv(path, mode='w', index=False, header=True, sep=',')
        return new_df.to_string()  