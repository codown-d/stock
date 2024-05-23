#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Desc: 同花顺 股东户数
"""

import os.path
import sys
from flask import Flask

cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)
import requests
import pandas as pd
from core.utils.commons import deep_merge_dicts
import execjs

def get_hexin_v():
    with open(cpath+'/core/utils/hexin_v.js', 'r', encoding='utf-8') as f:
        wlz_js = execjs.compile(f.read())
    hexin_v = wlz_js.call("getHexinV")
    print("hexin-v: ", hexin_v)
    return hexin_v
def stock_ths_base(dict2) -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    url = "https://www.iwencai.com/gateway/urp/v7/landing/getDataList"
    dict1 = {
        "rsh": "3",#第几页
        "typed": "1",# limit
        "preParams": "",
        "ts": "1",
        "f": "1",
        "qs": "result_rewrite",
        "selfsectsn": "",
        "querytype": "stock",
        "searchfilter": "",
        'tid':'stockpick',
        "queryarea": "",
    }
    headers= {
    "hexin-v": get_hexin_v(), 
    "Cookie":'ta_random_userid=jsdw0iexxs;v=A_M2oXj2kdfKxl2DamGIEQ1bgvwYKIqAQb_LC6WUTyBNAR3iLfgXOlGMW3e2'
    }
    params = deep_merge_dicts(dict1, dict2)
    print(params)
    r = requests.post(url, params=params,headers=headers)
    print(r)
    data_json = r.json()
    if not data_json["data"]["result"]:
        return pd.DataFrame()
    temp_df = pd.DataFrame(data_json["data"]["result"])
    return temp_df

def stock_shareholder_latest() -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    params = {
        "w": "最新股东户数",#过滤条件
    }
    temp_df = stock_ths_base(params)
    return temp_df

def stock_shareholder_history() -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    params = {
        "w": "",#过滤条件
    }
    temp_df = stock_ths_base(params)
    return temp_df


if __name__ == "__main__":
   
    print( execjs.eval("new Date"))
    df = stock_shareholder_latest()
    # print(df)

