#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import datetime
import logging
import os.path
import sys
import arrow
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import matplotlib.pyplot as plt





cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
print(cpath)
sys.path.append(cpath)

from core.models import StockTimePrice
from job.buy_strategy import strategy_macd
from job.test import draw_macd
from indicator import talib_MACD
from crawling.trading_calendar import get_pre_trade_date

def save_stocks_vol(time=arrow.now().format("YYYY-MM-DD")):
    start_date = datetime(2024, 6, 17,9, 30, 00)
    print(start_date)
    end_date = datetime(2024,6, 17,15, 00, 00)
    path =  f'{cpath}/stock_date/stock_vol/{start_date.date()}.parquet'
    try:
        stock = StockTimePrice.query.filter(StockTimePrice.时间.between(start_date, end_date)).all()
        df = pd.DataFrame([(r.ID, r.时间, r.代码, r.开盘,r.收盘,r.最高,r.最低,r.成交量,r.成交额,r.均价) for r in stock])
        df.columns=['ID', '时间', '代码', '开盘','收盘','最高','最低','成交量','成交额','均价']
        print(df)
        df.to_parquet(path, compression= 'gzip')
        return df
    except Exception as e:
        logging.error(f"fetch_stocks处理异常：{e}")
    return None
def read_stocks_vol(time=arrow.now().format("YYYY-MM-DD")):
    pre_path =  f'{cpath}/stock_date/stock_vol/{get_pre_trade_date(time,pre=1)}.parquet'
    path =  f'{cpath}/stock_date/stock_vol/{time}.parquet'
    try:
        pre_df = pd.read_parquet(pre_path)
        df = pd.read_parquet(path)
        new_df = pd.concat([pre_df,df],axis=0)
        new_df = new_df[(new_df["代码"] == '301215')]
        grouped = new_df.groupby(by=["代码"]) 
        print(len(grouped))
        for name, group_df in grouped:
            x = group_df["时间"].to_list()
            group_df=group_df.set_index('时间')
            macd, macdsignal, macdhist = talib_MACD(group_df['收盘'])
        # print(macd,macdsignal,macdhist)
        print(x)
        plt.plot(x, macd,color='#141414',label='diff')  # 绘制折线图，添加数据点，设置点的大小
        plt.plot(x, macdsignal,color='#d90d44',label='eda' )
        # plt.plot(x, macdhist*2,color='#3dba61',label='macd' )
        plt.bar(range(len(x)),macdhist*2,color='#3dba61')
        plt.legend()
        plt.show()
        # draw_macd(df_raw=df_raw,
        #       dif=macdsignal,
        #       dea=macdhist,
        #       red_bar=red_bar,
        #       green_bar=green_bar,
        #       xtick_period=25,
        #       title=u'招商银行 MACD')
        #https://www.jianshu.com/p/6e24af39b7e6
        return df
    except Exception as e:
        logging.error(f"read_stocks_vol处理异常：{e}")
    return None
if __name__ == '__main__':
    read_stocks_vol('2024-06-24')