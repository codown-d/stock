# -*- coding:utf-8 -*-

import os.path
import sys
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from core.utils.database import BaseMixin

class StockIndicators(db.Model):
    __tablename__ = "stock_indicators"
    date = db.Column(db.String(32), primary_key=True)  # 用户编号
    code = db.Column(db.String(8), primary_key=True)  # 用户编号
    name = db.Column(db.String(32), nullable=False)  # 用户编号
    close = db.Column(db.Float, nullable=False)  # 收盘价
    macd = db.Column(db.Float, nullable=False)
    macds = db.Column(db.Float, nullable=False)
    macdh = db.Column(db.Float, nullable=False)
    kdjk = db.Column(db.Float, nullable=False)
    kdjd = db.Column(db.Float, nullable=False)
    kdjj = db.Column(db.Float, nullable=False)
    boll_ub = db.Column(db.Float, nullable=False)
    boll = db.Column(db.Float, nullable=False)
    boll_lb = db.Column(db.Float, nullable=False)
    trix = db.Column(db.Float, nullable=False)
    trix_20_sma = db.Column(db.Float, nullable=False)
    tema = db.Column(db.Float, nullable=False)
    cr = db.Column(db.Float, nullable=False)
    cr_ma1 = db.Column(db.Float, nullable=False)
    cr_ma2 = db.Column(db.Float, nullable=False)
    cr_ma3 = db.Column(db.Float, nullable=False)
    rsi_6 = db.Column(db.Float, nullable=False)
    rsi_12 = db.Column(db.Float, nullable=False)
    rsi = db.Column(db.Float, nullable=False)
    rsi_24 = db.Column(db.Float, nullable=False)
    vr = db.Column(db.Float, nullable=False)
    vr_6_sma = db.Column(db.Float, nullable=False)
    roc = db.Column(db.Float, nullable=False)
    rocma = db.Column(db.Float, nullable=False)
    rocema = db.Column(db.Float, nullable=False)
    pdi = db.Column(db.Float, nullable=False)
    mdi = db.Column(db.Float, nullable=False)
    dx = db.Column(db.Float, nullable=False)
    adx = db.Column(db.Float, nullable=False)
    adxr = db.Column(db.Float, nullable=False)
    wr_6 = db.Column(db.Float, nullable=False)
    wr_10 = db.Column(db.Float, nullable=False)
    wr_14 = db.Column(db.Float, nullable=False)
    cci = db.Column(db.Float, nullable=False)
    cci_84 = db.Column(db.Float, nullable=False)
    tr = db.Column(db.Float, nullable=False)
    atr = db.Column(db.Float, nullable=False)
    dma = db.Column(db.Float, nullable=False)
    dma_10_sma = db.Column(db.Float, nullable=False)
    obv = db.Column(db.Float, nullable=False)
    sar = db.Column(db.Float, nullable=False)
    psy = db.Column(db.Float, nullable=False)
    psyma = db.Column(db.Float, nullable=False)
    br = db.Column(db.Float, nullable=False)
    ar = db.Column(db.Float, nullable=False)
    emv = db.Column(db.Float, nullable=False)
    emva = db.Column(db.Float, nullable=False)
    bias = db.Column(db.Float, nullable=False)
    mfi = db.Column(db.Float, nullable=False)
    mfisma = db.Column(db.Float, nullable=False)
    vwma = db.Column(db.Float, nullable=False)
    mvwma = db.Column(db.Float, nullable=False)
    ppo = db.Column(db.Float, nullable=False)
    ppos = db.Column(db.Float, nullable=False)
    ppoh = db.Column(db.Float, nullable=False)
    wt1 = db.Column(db.Float, nullable=False)
    wt2 = db.Column(db.Float, nullable=False)
    supertrend_ub = db.Column(db.Float, nullable=False)
    supertrend = db.Column(db.Float, nullable=False)
    supertrend_lb = db.Column(db.Float, nullable=False)
    dpo = db.Column(db.Float, nullable=False)
    madpo = db.Column(db.Float, nullable=False)
    vhf = db.Column(db.Float, nullable=False)
    rvi = db.Column(db.Float, nullable=False)
    rvis = db.Column(db.Float, nullable=False)
    fi = db.Column(db.Float, nullable=False)
    force_2 = db.Column(db.Float, nullable=False)
    force_13 = db.Column(db.Float, nullable=False)
    ene_ue = db.Column(db.Float, nullable=False)
    ene = db.Column(db.Float, nullable=False)
    ene_le = db.Column(db.Float, nullable=False)
    stochrsi_k = db.Column(db.Float, nullable=False)
    stochrsi_d = db.Column(db.Float, nullable=False)

class DFCFStockInfo(BaseMixin,db.Model):
    __tablename__ = "stock_info"
    id = db.Column(db.String(50),primary_key=True,nullable=False)  # 用户编号
    date = db.Column(db.String(50),nullable=False)  # 日期
    f12 = db.Column(db.String(50), nullable=False)# 代码
    f14 = db.Column(db.String(50), nullable=False)# 名称
    f2 = db.Column(db.Float and db.String(50))  # 最新价
    f3 = db.Column(db.Float, nullable=False) # 涨跌幅
    f4 = db.Column(db.Float, nullable=False) # 涨跌额
    f5 = db.Column(db.Float, nullable=False) # 成交量
    f6 = db.Column(db.Float, nullable=False)# 成交额
    f7 = db.Column(db.Float, nullable=False)# 振幅
    f8 = db.Column(db.Float, nullable=False)# 换手率
    f9 = db.Column(db.Float, nullable=False)# 市盈率动
    f10 = db.Column(db.Float, nullable=False)# 量比
    f11 = db.Column(db.Float, nullable=False)# 5分钟涨跌
    f13 = db.Column(db.Float, )# 市盈率(动)
    f15 = db.Column(db.Float, nullable=False)# 最高
    f16 = db.Column(db.Float, nullable=False)# 最低
    f17 = db.Column(db.Float, nullable=False)# 今开
    f18 = db.Column(db.Float, nullable=False)# 昨收
    f20 = db.Column(db.Float, nullable=False)#总市值
    f21 = db.Column(db.Float, nullable=False)#流通市值
    f22 = db.Column(db.Float, nullable=False)#涨速
    f23 = db.Column(db.Float, nullable=False)#市净率
    f24 = db.Column(db.Float, nullable=False)#60日涨跌幅
    f25 = db.Column(db.Float, nullable=False)#年初至今涨跌幅
    f26 = db.Column(db.Float, nullable=False)#上市时间
    f37 = db.Column(db.Float, nullable=False)#加权净资产收益率
    f38 = db.Column(db.Float, nullable=False)#总股本
    f39 = db.Column(db.Float, nullable=False)#已流通股份
    f40 = db.Column(db.Float, nullable=False)#营业收入
    f41 = db.Column(db.Float, nullable=False)#营业收入同比增长
    f45 = db.Column(db.Float, nullable=False)#归属净利润
    f46 = db.Column(db.Float, nullable=False)#归属净利润同比增长
    f48 = db.Column(db.Float, nullable=False)#每股未分配利润
    f49 = db.Column(db.Float, nullable=False)#毛利率
    f57 = db.Column(db.Float, nullable=False)#资产负债率
    f61 = db.Column(db.Float, nullable=False)#每股资本公积金
    f100 = db.Column(db.String(50))#所处行业
    f112 = db.Column(db.Float and db.String(50))#每股收益
    f113 = db.Column(db.Float, nullable=False)#每股净资产
    f114 = db.Column(db.Float, nullable=False) #市盈率(静)
    f115 = db.Column(db.Float, nullable=False) #市盈率TTM
    f221 = db.Column(db.Float, nullable=False) #报告期

class Shareholder(db.Model):
    __tablename__ = "stock_shareholder"
    code = db.Column(db.String(50),primary_key=True)  # 股票代码
    name = db.Column(db.String(50),nullable=False)  # 股票名称
    price = db.Column(db.String(50),nullable=True)  # 最新价格
    price_range= db.Column(db.String(50),nullable=True)  # 涨跌幅
    shareholder_count = db.Column(db.String(50),nullable=True)  # 最新股东户数
    shareholder_chigu_shuliang = db.Column(db.String(50),nullable=True)  # 最新户均持股数量(股) 
    shareholder_chigu_shizhi = db.Column(db.String(50),nullable=True)  # 最新户均持股市值
    shareholder_chigu_bili = db.Column(db.String(50),nullable=True)  # 最新户均持股比例
    gonggao_date = db.Column(db.String(50),nullable=False)  # 公告日期
    info = db.Column(db.JSON,nullable=True)  # 最新户均持股比例
    def update_orm_object(self,orm_object, data):
        for key, value in data.items():
            if hasattr(orm_object, key):
                setattr(orm_object, key, value)

    def insert_or_update_base(self,stockData):
        code=stockData['code']
        existing_stock = self.query.filter_by(code=code).first()
        print('existing_stock',existing_stock,code)
        if existing_stock:
            info=existing_stock.info or dict()
            info.setdefault(stockData['gonggao_date'],stockData['shareholder_count'])
            # if existing_stock.info:  
            #     info[stockData['gonggao_date']]=stockData['shareholder_count']
            #     existing_stock.info=info
            # else:
            #     existing_stock.info={}
            # stockData.setdefault('info',info)
            # print('info',existing_stock,stockData,info)
            setattr(existing_stock, 'info', info)
            # print(info,existing_stock.info)
            self.update_orm_object(self,existing_stock, stockData)
        else:
            stock = self(**stockData)
            db.session.add(stock)
    # 插入或更新数据
    @classmethod
    def insert_or_update(self,data:dict):
        self.insert_or_update_base(self,data)
        db.session.commit()
    # 插入或更新多条数据
    @classmethod
    def insert_or_update_all(self,data:list):
        print(data)
        for x in range(0, len(data)):
            item = data[x]
            self.insert_or_update_base(self,item)
        db.session.commit()
