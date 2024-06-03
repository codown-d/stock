#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Desc: 同花顺 股东户数
"""
import re
import arrow
import pydash as _
import os.path
import sys


cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import pandas as pd
import core.libs.pywencai as wencai
from core.utils.commons import get_latest_quarter_list
from core.constants import ST_STOCK_CODE


def stock_ths_base(**kwargs) -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    temp_df = wencai.get(**kwargs)
    return temp_df

def stock_shareholder_latest() -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    query='最新股东户数'
    temp_df = stock_ths_base(query=query,loop=1)
    time = arrow.now().format("YYYYMMDD")
    temp_df = temp_df.drop(['股票代码','market_code',f'股东人数变动公告日[{time}]'], axis=1)
    temp_df[time]=temp_df['最新股东户数']
    return temp_df

def stock_shareholder_history() -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    query='最近8个季度股东户数，最新股东户数，第一季度股东户数'
    temp_df = stock_ths_base(query=query,loop=True)
    time = arrow.now().format("YYYYMMDD")
    temp_df = temp_df.drop(['股票代码','market_code',f'股东人数变动公告日[{time}]'], axis=1)
    temp_df[time]=temp_df['最新股东户数']
    new_column=[]
    for col in temp_df.columns:
        pattern = r"\[(.*?)\]"
        result = re.findall(pattern, col)
        if(len(result)):
            new_column.append(result[0])
        else:
            new_column.append(col)
    temp_df.columns=new_column
    quarter_list=get_latest_quarter_list()
    time = arrow.now().format("YYYYMMDD")
    temp_df=temp_df[['code', '股票简称', '最新价','最新户均持股市值',f'{time}']+quarter_list]
    temp_df.columns=[
            "code",
            "name",
            "price",
            'shareholder_chigu_shizhi',
            "quarter_0",
            "quarter_1",
            "quarter_2",
            "quarter_3",
            "quarter_4",
            'quarter_5',
            'quarter_6',
            'quarter_7',
            'quarter_8',
            'quarter_9',
        ]
    temp_df['price'] = pd.to_numeric(temp_df['price'])
    temp_df['shareholder_chigu_shizhi'] = pd.to_numeric(temp_df['shareholder_chigu_shizhi'])
    temp_df['quarter_0'] = pd.to_numeric(temp_df['quarter_0'])
    temp_df['quarter_1'] = pd.to_numeric(temp_df['quarter_1'])
    temp_df['quarter_2'] = pd.to_numeric(temp_df['quarter_2'])
    temp_df['quarter_3'] = pd.to_numeric(temp_df['quarter_3'])
    temp_df['quarter_4'] = pd.to_numeric(temp_df['quarter_4'])
    temp_df['quarter_5'] = pd.to_numeric(temp_df['quarter_5'])
    temp_df['quarter_6'] = pd.to_numeric(temp_df['quarter_6'])
    temp_df['quarter_7'] = pd.to_numeric(temp_df['quarter_7'])
    temp_df['quarter_8'] = pd.to_numeric(temp_df['quarter_8'])
    temp_df['quarter_9'] = pd.to_numeric(temp_df['quarter_9'])
    temp_df['shareholder_level_1'] = (temp_df['quarter_0']-temp_df['quarter_9'])/temp_df['quarter_9']*100
    temp_df['shareholder_level_2'] = (temp_df['quarter_0']-temp_df['quarter_5'])/temp_df['quarter_5']*100
    temp_df = temp_df.dropna() 
    print(temp_df)
    return temp_df


def st_stock_code() -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    query='一年内被立案调查公司'
    temp_df = stock_ths_base(query=query,loop=True)
    new_df = pd.DataFrame({
        'code':temp_df['code'],
        'name':temp_df['股票简称'],
        })
    # new_df = new_df.dropna() 
    return new_df
def stock_code() -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    time = arrow.now().format("YYYYMMDD")
    path = f'{cpath}/stock_date/daily_stock/{time}.csv'
    try:
        csvframe = pd.read_csv(path,dtype={'code': str,})
        return csvframe
    except Exception as e:
        df_st_code = pd.DataFrame({'code': ST_STOCK_CODE}) 
        st_stock = st_stock_code()
        new_st_stock=pd.concat([df_st_code] + [st_stock], ignore_index=True)
        query='非st，非北交所，上市天数大于20，股票流通市值大于10亿且股票流通市值小于800亿，股价涨幅大于0%，股价大于2元，五日均换手率大于1.5%，人均持股市值大于5万'
        temp_df = stock_ths_base(query=query,loop=True)
        
        new_df = pd.DataFrame({
            'code':temp_df['code'],
            'name':temp_df['股票简称'],
            'price':temp_df[f'涨跌幅:前复权[{time}]'],
            })
        new_df = new_df[~new_df["code"].isin(new_st_stock['code'])]
        new_df.to_csv(path, mode='w', index=False, header=True, sep=',')
        return new_df.to_string()  

if __name__ == '__main__':
    stock_code()

