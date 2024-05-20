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
from crawling.stock_hold_management_detail_cninfo import stock_hold_management_detail_cninfo

@api.route("/stock/summary",methods=['GET'])
def get_stock_summary():
    stock_summary = ak.stock_sse_summary()
    print(stock_summary)
    return 'stock_summary.to_string'

# 获取历史分时数据
@api.route("/stock/history",methods=['GET'])
def get_stock_zh_a_hist(symbol='603777',period='daily',start_date='20220101',end_date='20240519',):
    stock_zh_a_hist = ak.stock_zh_a_hist(symbol,period,start_date,end_date)
    stock_zh_a_hist['diff'],  stock_zh_a_hist['dea'],stock_zh_a_hist['macd']=getMACD( stock_zh_a_hist['收盘'].values)
    print(stock_zh_a_hist)
    return 'stock_summary.to_string'

# 获取历史分时数据
@api.route("/stock/min",methods=['GET'])
def get_stock_min(symbol="603777",start_date="2024-05-17 09:30:00",end_date="2024-05-20 15:00:00",period="1",):
    index_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol,start_date,end_date,period,)
    print(index_zh_a_hist_min_em_df)
    return 'stock_summary.to_string'

# 股东人数
@api.route("/stock/min",methods=['GET'])
def get_stock_hold_num_cninfo(date="20210630"):
    stock_hold_num_cninfo_df = ak.stock_hold_num_cninfo(date)
    print(stock_hold_num_cninfo_df)
    return 'stock_summary.to_string'

# 高管持股变动明细
@api.route("/stock/min",methods=['GET'])
def get_stock_hold_management_detail_cninfo(symbol="增持"):
    stock_hold_management_detail_cninfo_df = stock_hold_management_detail_cninfo(symbol)
    stock_hold_management_detail_cninfo_df.sort_values(by=['变动比例'], ascending=False)
    print(stock_hold_management_detail_cninfo_df)
    return 'stock_summary.to_string'
if __name__ == '__main__':
    get_stock_hold_management_detail_cninfo()

