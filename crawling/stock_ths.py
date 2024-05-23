#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Desc: 同花顺 股东户数
"""
import pydash as _
import arrow
import os.path
import sys
from flask import Flask
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import pandas as pd
import core.libs.pywencai.wencai as wencai


def stock_ths_base(**kwargs) -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    res = wencai.get(**kwargs)
    return res

def stock_shareholder_latest() -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    query='最新股东户数'
    temp_df = stock_ths_base(query=query,loop=5)
    time = arrow.now().format("YYYYMMDD")
    temp_df = temp_df.drop(['股票代码','market_code'], axis=1)
    temp_df.rename(
        columns={
            "股票简称": "name",
            "最新价":"price",
            "最新涨跌幅":"zxzdf",
            "最新股东户数": "zxgdhs",
            "最新户均持股数量": "zxhjcgsl",
            "最新户均持股市值": "zxhjcgsz",
            "最新户均持股比例": "zxhjcgbl",
            f"股东人数变动公告日[{time}]": "declaration_date",
        },
        inplace=True,
    )
    print(temp_df)
    return temp_df

def stock_shareholder_history() -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    query='最近两年股东户数'
    temp_df = stock_ths_base(query)
    return temp_df


if __name__ == "__main__":
    df = stock_shareholder_latest()
    # print(df)

