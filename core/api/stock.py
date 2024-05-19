# coding:utf-8

import os.path
import sys

cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current, os.pardir))
sys.path.append(cpath)
from core.constants import STOCK_BASE_IND
from core.api import api
import akshare as ak
from indicator import getMACD

@api.route("/stock/summary",methods=['GET'])
def get_stock_summary():
    stock_summary = ak.stock_sse_summary()
    print(stock_summary)
    return 'stock_summary.to_string'

@api.route("/stock/history",methods=['GET'])
def get_stock_zh_a_hist(symbol='603777',period='daily',start_date='20220101',end_date='20240519',):
    stock_zh_a_hist = ak.stock_zh_a_hist(symbol,period,start_date,end_date)
    stock_zh_a_hist['diff'],  stock_zh_a_hist['dea'],stock_zh_a_hist['macd']=getMACD( stock_zh_a_hist['收盘'].values)
    print(stock_zh_a_hist)
    return 'stock_summary.to_string'

if __name__ == '__main__':
    get_stock_zh_a_hist()

