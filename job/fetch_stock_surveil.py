#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os.path
import threading
import sys
import os
import pandas as pd   #将数据保存至相应文件中
from concurrent.futures import ThreadPoolExecutor,as_completed

cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)
from core.utils.commons import gp_type_szsh
import akshare as ak
from crawling.stock_dfcf import stock_fenshi_detail

def main(list_code):
    try:
        with ThreadPoolExecutor(max_workers=1000) as executor:
            to_do = []
            print(list_code)
            for code in list_code:
                future = executor.submit(fetch_stocks, code)
                to_do.append(future)
            for future in as_completed(to_do):  # 并发执行
                f = future.result()
                print(f)
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None

def fetch_stocks(code):
    try:
        stock_zh_a_hist_df = stock_fenshi_detail(code=code)
        return {'date':stock_zh_a_hist_df,'code':code}
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None

# main函数入口
if __name__ == '__main__':
    main(['300059','000001'])
    # timer =threading.Timer(5.0, lambda : main(['000001','600636']))
    # timer.start() 