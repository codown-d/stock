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
import crawling.stock_ths as ths
import akshare as ak
from core.utils.commons import calc_pre_minute_change
from core.models import get_stock_model
from core.models import db
# 更新股东信息
def fetch_tick_volume():
    try:
        temp_df = ths.stock_code()
        temp_df = temp_df[(temp_df["code"].str.startswith('00')|temp_df["code"].str.startswith('30')|temp_df["code"].str.startswith('60')|temp_df["code"].str.startswith('688')) & ~temp_df['name'].str.contains('ST')]
        print(temp_df.to_string())
        result = temp_df.to_dict(orient='records') 
  
        with ThreadPoolExecutor(max_workers=100) as executor:
            to_do = []
            for res in result:
                code =res['code']
                future = executor.submit(fetch_stocks, code)
                to_do.append(future)
            for future in as_completed(to_do):  # 并发执行
                res_future = future.result()
                temp_df=res_future['date']
                temp_code=res_future['code']
                # calc_res=calc_pre_minute_change(temp_df,60)[:8]
                if temp_code=='300945':
                    print(temp_code)
                    model = get_stock_model(temp_code)
                    stock = model(代码=temp_code)
                    db.session.add(stock)
                    db.session.commit()
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