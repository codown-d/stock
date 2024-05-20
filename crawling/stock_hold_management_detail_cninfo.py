#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os.path
import sys
from flask import Flask
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
print(cpath)
sys.path.append(cpath)
import datetime
import pandas as pd
import requests
from core.utils.commons import deep_merge_dicts


def stock_hold_management_detail_cninfo(symbol: str = "增持") -> pd.DataFrame:
    """
    巨潮资讯-数据中心-专题统计-股东股本-高管持股变动明细
    http://webapi.cninfo.com.cn/#/thematicStatistics
    :param symbol: choice of {"增持", "减持"}
    :type symbol: str
    :return: 高管持股变动明细
    :rtype: pandas.DataFrame
    """
    symbol_map = {
        "增持": "B",
        "减持": "S",
    }
    current_date = datetime.datetime.now().date().isoformat()
    url = "http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1030"
    
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Content-Length": "0",
        "Host": "webapi.cninfo.com.cn",
        "Accept-Enckey": "6BRm7ABzhMPu9ynVQFcXrQ==",
        "Origin": "http://webapi.cninfo.com.cn",
        "Pragma": "no-cache",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://webapi.cninfo.com.cn/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    params = {
        "sdate": str(int(current_date[:4]) - 1) + current_date[4:],
        "edate": current_date,
        "varytype": symbol_map[symbol],
    }
    print(params)
    r = requests.post(url, headers=headers, params=params)
    data_json = r.json()
    temp_df = pd.DataFrame(data_json["records"])
    temp_df.columns = [
        "证券简称",
        "公告日期",
        "高管姓名",
        "期末市值",
        "成交均价",
        "证券代码",
        "变动比例",
        "变动数量",
        "截止日期",
        "期末持股数量",
        "期初持股数量",
        "变动人与董监高关系",
        "董监高职务",
        "董监高姓名",
        "数据来源",
        "持股变动原因",
    ]
    temp_df = temp_df[
        [
            "证券代码",
            "证券简称",
            "截止日期",
            "公告日期",
            "高管姓名",
            "董监高姓名",
            "董监高职务",
            "变动人与董监高关系",
            "期初持股数量",
            "期末持股数量",
            "变动数量",
            "变动比例",
            "成交均价",
            "期末市值",
            "持股变动原因",
            "数据来源",
        ]
    ]
    temp_df["截止日期"] = pd.to_datetime(temp_df["截止日期"], errors="coerce").dt.date
    temp_df["公告日期"] = pd.to_datetime(temp_df["公告日期"], errors="coerce").dt.date
    temp_df["期初持股数量"] = pd.to_numeric(temp_df["期初持股数量"], errors="coerce")
    temp_df["期末持股数量"] = pd.to_numeric(temp_df["期末持股数量"], errors="coerce")
    temp_df["变动数量"] = pd.to_numeric(temp_df["变动数量"], errors="coerce")
    temp_df["变动比例"] = pd.to_numeric(temp_df["变动比例"], errors="coerce")
    temp_df["成交均价"] = pd.to_numeric(temp_df["成交均价"], errors="coerce")
    temp_df["期末市值"] = pd.to_numeric(temp_df["期末市值"], errors="coerce")
    return temp_df

# 东财数据中心基础数据
def stock_detail_em(dict2) -> pd.DataFrame:
    """
    东方财富网-数据中心-资金流向-排名
    https://data.eastmoney.com/executive/gdzjc.html
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
    print(data_json)
    temp_df = pd.DataFrame(data_json["result"]["data"])
    print(temp_df)
    return temp_df

# 股东户数（最新）
def stock_management_detail() -> pd.DataFrame:
    """
    """
    params = {
        "sortColumns":"HOLDER_NUM",
        "sortTypes":"1",
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