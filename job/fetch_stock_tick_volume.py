#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
from concurrent.futures import ThreadPoolExecutor,as_completed
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import crawling.stock_dfcf as dfcf
import akshare as ak
from core.utils.commons import calc_pre_minute_change
# 更新股东信息
def fetch_tick_volume():
    try:
        temp_df = ak.stock_info_a_code_name()
        temp_df = temp_df[(temp_df["code"].str.startswith('00')|temp_df["code"].str.startswith('30')|temp_df["code"].str.startswith('60')|temp_df["code"].str.startswith('688')) & ~temp_df['name'].str.contains('ST')]
        result = temp_df.to_dict(orient='records') [:2]
        print(result)
        with ThreadPoolExecutor(max_workers=1000) as executor:
            to_do = []
            for res in result:
                code =res['code']
                future = executor.submit(fetch_stocks, code)
                to_do.append(future)
            for future in as_completed(to_do):  # 并发执行
                f = future.result()
                temp_df=f['date']
                calc_res=calc_pre_minute_change(temp_df,60)[:20]
                print(calc_res)
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
def fetch_stocks(code):
    try:
        stock_zh_a_hist_df = dfcf.stock_fenshi_detail(code=code)
        return {'date':stock_zh_a_hist_df,'code':code}
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
# main函数入口
if __name__ == '__main__':
    fetch_tick_volume()