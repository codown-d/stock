#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Desc: 同花顺 股东户数
"""
import re
import datetime
import pydash as _
import arrow
import os.path
import sys
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import pandas as pd
import core.libs.pywencai as wencai
from dateutil.relativedelta import relativedelta           # 引入新的包


def stock_ths_base(**kwargs) -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    temp_df = wencai.get(**kwargs)
    time = arrow.now().format("YYYYMMDD")
    temp_df[time]=temp_df['最新股东户数']
    # temp_df = temp_df.drop(['股票代码','market_code',f'股东人数变动公告日[{time}]'], axis=1)
    # temp_df.columns=[
    #         "股票代码",
    #         "最新价",
    #         "最新涨跌幅",
    #         "股票简称",
    #         "最新户均持股数量",
    #         "最新户均持股市值",
    #         "最新户均持股比例",
    #         '-',
    #         '-',
    #         '-',
    #         '-',
    #         '-',
    #         '-',
    #         '-',
    #         '-',
    #         '-',
    #         '-',
    #         '-',
    #         '-',
    #     ]
    today = datetime.date.today()
    quarter_end_day = datetime.date(today.year,today.month - (today.month - 1) % 3 +2, 1) + relativedelta(months=1,days=-1)
    quarter_end_day.isoformat() 
    print(temp_df.columns,today,quarter_end_day)
    temp_df=temp_df[['股票代码', '最新价', '股票简称','market_code']]
    print(temp_df)
    return temp_df

def stock_shareholder_latest() -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    query='最新股东户数'
    temp_df = stock_ths_base(query=query,loop=1)
    return temp_df

def stock_shareholder_history() -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    query='最近8个季度股东户数，最新股东户数'
    temp_df = stock_ths_base(query=query,loop=1)
    print(temp_df)
    # new_column=[]
    # for col in temp_df.columns:
    #     pattern = r"\[(.*?)\]"
    #     result = re.findall(pattern, col)
    #     if(len(result)):
    #         new_column.append(result[0])
    #     else:
    #         new_column.append(col)
    # temp_df.columns=new_column
    return temp_df


if __name__ == '__main__':
    stock_shareholder_history()

