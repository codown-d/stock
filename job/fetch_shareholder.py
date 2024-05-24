#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os.path
import sys
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

import crawling.stock_hist_em as she
import crawling.stock_ths as ths
from core.models import  Shareholder
# 更新股东信息
def fetch_shareholder():
    try:
        df = ths.stock_shareholder_latest()
        df=df.where(df.notnull(), None)
        if df is None or len(df.index) == 0:
            return None
        data = df.to_dict(orient='records')
        Shareholder.insert_or_update_all(data)
        return df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
       