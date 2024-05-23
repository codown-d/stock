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
    hexin_v = wlz_js.call("rt.update")
    return hexin_v

def stock_ths_base(dict2) -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    hexin_v=get_hexin_v()
    url = "https://www.iwencai.com/gateway/urp/v7/landing/getDataList"
    durl='https://www.iwencai.com/customized/chart/get-robot-data'
    dict1 = {
        'query': '股东户数',
        'urp_sort_way': 'desc',
        'urp_sort_index': '最新股东户数',
        'page': 3,
        'perpage': 50,
        'addheaderindexes': '',
        'condition': [{"dateText":"","indexName":"最新股东户数","indexProperties":[],"ci":'true',"source":"text2sql","type":"index","indexPropertiesMap":{},"reportType":"null","ciChunk":"股东户数","score":0.0,"createBy":"preCache","chunkedResult":"股东户数","uiText":"最新股东户数","valueType":"_整型数值(户|家|人|个)","domain":"abs_股票领域","sonSize":0,"logid":"e34a0ca9ec1b4be062c5c78ddc86093a","dateList":[],"order":0}],
        'codelist': '',
        'indexnamelimit': '',
        'logid': 'e34a0ca9ec1b4be062c5c78ddc86093a',
        'ret': 'json_all',
        'sessionid': '9720942b37fd5228440b248df24f4f89',
        'source': 'Ths_iwencai_Xuangu',
        'date_range[0]': '20240523',
        'iwc_token': '0ac9529817164470305696700',
        'urp_use_sort': 1,
        'user_id': 'Ths_iwencai_Xuangu_t99g9jx6zzfwi3ok1peyp39houa6uy79',
        'uuids[0]': 24087,
        'query_type': 'stock',
        'comp_id': 6836372,
        'business_cat': 'soniu',
        'uuid': 24087,
    }
    d={
    "source": "Ths_iwencai_Xuangu",
    "version": "2.0",
    "query_area": "",
    "block_list": "",
    "add_info": "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1},\"contentType\":\"json\",\"searchInfo\":true}",
    "question": "股东户数",
    "perpage": "50",
    "page": 1,
    "secondary_intent": "stock",
    "log_info": "{\"input_type\":\"typewrite\"}",
    }
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Hexin-V": hexin_v, 
        "Cookie":f"v={hexin_v}"
    }
    params = deep_merge_dicts(d, dict2)
    r = requests.post(durl, params=params,headers=headers)
    data_json = r.json()
    print(data_json)
    if not data_json["data"]["result"]:
        return pd.DataFrame()
    temp_df = pd.DataFrame(data_json["data"]["result"])
    return temp_df

def stock_shareholder_latest() -> pd.DataFrame:
    """
    同花顺问财
    https://www.iwencai.com/stockpick/load-data
    """
    params = {}
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
    df = stock_shareholder_latest()
    # print(df)

