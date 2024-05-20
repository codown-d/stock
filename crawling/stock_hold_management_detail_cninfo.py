#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import pandas as pd
import requests



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

if __name__ == '__main__':
    stock_hold_management_detail_cninfo()