#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import arrow
import requests
import pandas as pd
import numpy as np
import os.path
import sys
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import akshare as ak
from core.utils.commons import calc_pre_minute_change, deep_merge_dicts, gp_type_szsh
# 东财数据中心基础数据


def stock_detail_em(dict2) -> pd.DataFrame:
    """
    东方财富网
    """
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"
    dict1 = {
        "pageSize": 6000,
        "pageNumber": 1,
        'quoteType': 0,
        'source': 'WEB',
        "client": 'WEB',

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
        "sortColumns": "HOLDER_NUM",  # HOLD_NOTICE_DATE,SECURITY_CODE
        "sortTypes": "1",  # -1,-1 控制sortColumns 排序
        "reportName": "RPT_HOLDERNUMLATEST",
        "columns": "SECURITY_CODE,SECURITY_NAME_ABBR,END_DATE,INTERVAL_CHRATE,HOLDER_NUM,PRE_HOLDER_NUM,HOLDER_NUM_CHANGE,HOLDER_NUM_RATIO,END_DATE,PRE_END_DATE",
    }
    temp_df = stock_detail_em(params)
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
        "sortColumns": "END_DATE,SECURITY_CODE,EITIME",
        "sortTypes": "-1,-1,-1",
        "reportName": "RPT_SHARE_HOLDER_INCREASE",
        "columns": "f2,SECURITY_CODE,SECURITY_NAME_ABBR,NEWEST_PRICE,CHANGE_RATE_QUOTES,CHANGE_NUM,AFTER_CHANGE_RATE,CHANGE_FREE_RATIO",
        'quoteColumns': 'f2~01~SECURITY_CODE~NEWEST_PRICE,f3~01~SECURITY_CODE~CHANGE_RATE_QUOTES',
        'filter': f'(DIRECTION="增持")'
    }
    temp_df = stock_detail_em(params)
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

#实时分时分钟数据
def stock_fenshi_detail(code) -> pd.DataFrame:
    url = "http://31.push2.eastmoney.com/api/qt/stock/details/sse"
    secid = f'0.{code}' if gp_type_szsh(code)=='sz' else f'1.{code}'
    params = {
        'fields1': 'f1,f2,f3,f4',
        'fields2': 'f51,f52,f53,f54,f55',
        'mpi':  2000,
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fltt':  2,
        'pos': '-0',
        'secid': secid,
        'wbp2u': '4097055408292064|0|1|0|web'

    }
    r = requests.get(url, params=params,stream=True)
    for line in r.iter_lines(chunk_size=1024):
        if line:
            data_json= line.decode('utf-8')[6:]  
            data_json=json.loads(data_json)
            temp_df = pd.DataFrame([item.split(",") for item in data_json["data"]["details"]],columns=[
            "时间",
            "股价",
            "成交量",
            '未成交',
            "主动买卖",
            ])
            temp_df['时间']=pd.to_datetime(temp_df['时间'],format='mixed',dayfirst=True)
            temp_df['股价'] = pd.to_numeric(temp_df['股价'])
            temp_df['成交量'] = pd.to_numeric(temp_df['成交量'])
            temp_df['成交额'] = np.around(temp_df['成交量']*temp_df['股价']*100,2)
            # res_df = temp_df.loc[temp_df['时间'] >= '09:30:00']
            # temp_df=temp_df.set_index(keys='时间')
            print(temp_df)
            return temp_df

#历史分时分钟数据
def stock_history_fenshi_detail(symbol,start_date,end_date) -> pd.DataFrame:
    temp_df = ak.stock_zh_a_hist_min_em(symbol=symbol, start_date=start_date, end_date=end_date, period="1", adjust="")
    return temp_df
def stock_history_fenshi_detail_xinlang(symbol) -> pd.DataFrame:
    temp_df = ak.stock_zh_a_minute(symbol=symbol,  period='1', adjust="qfq")
    return temp_df

if __name__ == '__main__':
    stock_history_fenshi_detail('603650',start_date="2024-06-04 09:30:00", end_date="2024-06-04 15:00:00")
    # calc_res=calc_pre_minute_change(temp_df,60)
    # print(calc_res.to_string())
    # print(calc_res.loc[calc_res['时间'] >= '09:25:00'])
    
    # print(calc_res.loc[calc_res['时间'] >= '09:30:57'])
