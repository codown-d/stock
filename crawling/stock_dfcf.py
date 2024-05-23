#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os.path
import sys
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
print(cpath)
sys.path.append(cpath)
import pandas as pd
import requests
from core.utils.commons import deep_merge_dicts

# 东财数据中心基础数据
def stock_detail_em(dict2) -> pd.DataFrame:
    """
    东方财富网
    """
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    dict1 = {
        "pageSize":6000,
        "pageNumber":1,
        'quoteType':0,
        'source':'WEB',
        "client":'WEB',
       
    }
    params = deep_merge_dicts(dict1, dict2)
    r = requests.get(url, params=params)
    data_json = r.json()
    temp_df = pd.DataFrame(data_json["result"]["data"])
    return temp_df

# 股东户数（最新）clear
def stock_management_detail() -> pd.DataFrame:
    """
    东方财富网-股东户数（最新）
    https://data.eastmoney.com/gdhs/
    """
    params = {
        "sortColumns":"HOLDER_NUM",#HOLD_NOTICE_DATE,SECURITY_CODE
        "sortTypes":"1",#-1,-1 控制sortColumns 排序
        "reportName":"RPT_HOLDERNUMLATEST",
        "columns":"SECURITY_CODE,SECURITY_NAME_ABBR,END_DATE,INTERVAL_CHRATE,HOLDER_NUM,PRE_HOLDER_NUM,HOLDER_NUM_CHANGE,HOLDER_NUM_RATIO,END_DATE,PRE_END_DATE",
    }
    temp_df= stock_detail_em(params)
    temp_df.rename(
        columns={
            "SECURITY_CODE": "代码",
            "SECURITY_NAME_ABBR": "名称",
            "f2": "最新价",
            "f3": "涨跌幅",
            "HOLDER_NUM": "本次股东户数",
            "PRE_HOLDER_NUM": "上次股东户数",
            "HOLDER_NUM_CHANGE": "增减",
            "HOLDER_NUM_RATIO": "增减比例",
            "INTERVAL_CHRATE": "区间涨跌幅",
            "END_DATE": "本期报告",
            "PRE_END_DATE": "上期报告",
        },
        inplace=True,
    )
    print(temp_df)
    return temp_df

# 股东增减持
def stock_management_increase_detail_em() -> pd.DataFrame:
    params = {
       "sortColumns":"END_DATE,SECURITY_CODE,EITIME",
        "sortTypes":"-1,-1,-1",
        "reportName":"RPT_SHARE_HOLDER_INCREASE",
        "columns":"f2,SECURITY_CODE,SECURITY_NAME_ABBR,NEWEST_PRICE,CHANGE_RATE_QUOTES,CHANGE_NUM,AFTER_CHANGE_RATE,CHANGE_FREE_RATIO",
        'quoteColumns':'f2~01~SECURITY_CODE~NEWEST_PRICE,f3~01~SECURITY_CODE~CHANGE_RATE_QUOTES',
        'filter':f'(DIRECTION="增持")'
    }
    temp_df= stock_detail_em(params)
    temp_df.rename(
        columns={
            "SECURITY_CODE": "代码",
            "SECURITY_NAME_ABBR": "名称",
            "NEWEST_PRICE": "最新价",
            "CHANGE_RATE_QUOTES": "涨跌幅",
            "CHANGE_NUM": "变动数量(万股)",
            "AFTER_CHANGE_RATE": "占总股本比例",
            "CHANGE_FREE_RATIO": "占流通股比例",
        },
        inplace=True,
    )
    print(temp_df)
    return temp_df
if __name__ == '__main__':
    stock_management_detail()