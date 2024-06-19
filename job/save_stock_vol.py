#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import datetime
import logging
import os.path
import sys
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
print(cpath)
sys.path.append(cpath)

from core.models import StockTimePrice

path =  f'{cpath}/output.parquet'
def save_stocks_vol():
    try:
        start_date = datetime(2024, 6, 6,9, 30, 00)
        end_date = datetime(2024,6, 6,15, 00, 00)
        stock = StockTimePrice.query.filter(StockTimePrice.时间.between(start_date, end_date)).all()
        df = pd.DataFrame([(r.ID, r.时间, r.代码, r.开盘,r.收盘,r.最高,r.最低,r.成交量,r.成交额,r.均价) for r in stock])
        df.columns=['ID', '时间', '代码', '开盘','收盘','最高','最低','成交量','成交额','均价']
        print(df)
        df.to_parquet(path, compression= 'gzip')
        return df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
def read_stocks_vol():
    try:
        df = pd.read_parquet(path)
        print(df)
        return df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
if __name__ == '__main__':
    read_stocks_vol()