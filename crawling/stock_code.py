#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import sys
import akshare as ak
import arrow
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import crawling.stock_ths as ths
import pandas as pd
from core.constants import ST_STOCK_CODE
# 更新股东信息
def stock_code():
    # time = arrow.now().format("YYYYMMDD")
    time = '2024-10-10'
    path = f'{cpath}/stock_date/{time}_stock_code.csv'
    try:
        csvframe = pd.read_csv(path,dtype={'code': str,})
        return csvframe
    except Exception as e:
        temp_df =  ak.stock_zh_a_spot_em()
        df_st_code = pd.DataFrame({'code': ST_STOCK_CODE}) 
        new_st_stock=pd.concat([df_st_code], ignore_index=True)
        temp_df["code"]=temp_df["代码"]
        temp_df = temp_df[(temp_df["code"].str.startswith('00')|
                           temp_df["code"].str.startswith('30')|
                           temp_df["code"].str.startswith('60')|
                           temp_df["code"].str.startswith('688'))& 
                           ~temp_df["名称"].str.contains('ST')]
        # temp_df=temp_df[temp_df['最新价']]
        # print(temp_df[temp_df["code"] == '603381'])
        temp_df = temp_df.dropna(axis='index', how='any')
        new_df = pd.DataFrame({
            'code':temp_df['code'],
            'name':temp_df['名称'],
            })
        new_df = new_df[~new_df["code"].isin(new_st_stock['code'])]
        new_df.to_csv(path, mode='w', index=False, header=True, sep=',')
        print(new_df)
        return new_df 

if __name__ == '__main__':
    stock_code()