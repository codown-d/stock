#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Desc: 同花顺 股东户数
"""
import re
import pydash as _
import arrow
import os.path
import sys
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import pandas as pd
import core.libs.pywencai as wencai


def stock_ths_base(**kwargs) -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    temp_df = wencai.get(**kwargs)
    temp_df = temp_df.drop(['股票代码','market_code'], axis=1)
    temp_df.rename(
        columns={
            "股票简称": "name",
            "最新价":"price",
            "最新涨跌幅":"price_range",
            "最新股东户数": "shareholder_count",
            "最新户均持股数量": "shareholder_chigu_shuliang",
            "最新户均持股市值": "shareholder_chigu_shizhi",
            "最新户均持股比例": "shareholder_chigu_bili",
        },
        inplace=True,
    )
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
    new_column=[]
    for col in temp_df.columns:
        pattern = r"\[(.*?)\]"
        result = re.findall(pattern, col)
        if(len(result)):
            new_column.append(result[0])
        else:
            new_column.append(col)
    temp_df.columns=new_column
    return temp_df


if __name__ == '__main__':
    stock_shareholder_history()

