#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import arrow
import pandas as pd

cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

from indicator import talib_MACD

def strategy_macd(df):
    try:
        temp_df = talib_MACD(df)
        return temp_df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None