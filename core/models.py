# -*- coding:utf-8 -*-

import logging
import os.path
import sys
from sqlalchemy import Column, Integer, String,Date,Float

cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from core.utils.database import BaseMixin

class StockTimePrice(BaseMixin,db.Model):
    __tablename__ = "stock_time_price"
    ID = Column(String(40),primary_key=True,nullable=False)  
    时间 = Column(db.DateTime,nullable=False)  
    代码 = Column(String(10),nullable=False)
    开盘 = Column(db.Float,nullable=False)
    收盘 = Column(db.Float,nullable=False)    
    最高 = Column(db.Float,nullable=False)  
    最低 = Column(db.Float,nullable=False)  
    成交量 = Column(db.Integer,nullable=False)  
    成交额 = Column(db.Float,nullable=False)  
    均价 = Column(db.Float,nullable=False)  


class DFCFStockInfo(BaseMixin,db.Model):
    __tablename__ = "stock_info"
    id = db.Column(db.String(40),primary_key=True,nullable=False)  # 用户编号
    date = db.Column(db.String(30),nullable=False)  # 日期
    f12 = db.Column(db.String(10), nullable=False)# 代码
    f14 = db.Column(db.String(8), nullable=False)# 名称
    f2 = db.Column(db.Float)  # 最新价
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
    code = db.Column(db.String(10),primary_key=True)  # 股票代码
    name = db.Column(db.String(8),nullable=False)  # 股票名称
    price = db.Column(db.Float,nullable=True)  # 最新价格
    shareholder_chigu_shizhi = db.Column(db.Float,nullable=True)  # 最新户均持股市值
    quarter_0 = db.Column(db.Integer,nullable=True)  
    quarter_1 = db.Column(db.Integer,nullable=True)  
    quarter_2 = db.Column(db.Integer,nullable=True)  
    quarter_3 = db.Column(db.Integer,nullable=True)  
    quarter_4 = db.Column(db.Integer,nullable=True)  
    quarter_5 = db.Column(db.Integer,nullable=True)  
    quarter_6 = db.Column(db.Integer,nullable=True)  
    quarter_7 = db.Column(db.Integer,nullable=True)  
    quarter_8 = db.Column(db.Integer,nullable=True)  
    quarter_9 = db.Column(db.Integer,nullable=True)  
    shareholder_level_1 = db.Column(db.Float,nullable=True)  
    shareholder_level_2 = db.Column(db.Float,nullable=True)  

    def update_orm_object(self,orm_object, data):
        for key, value in data.items():
            if hasattr(orm_object, key):
                setattr(orm_object, key, value)

    def insert_or_update_base(self,stockData):
        code=stockData['code']
        existing_stock = self.query.filter_by(code=code).first()
        if existing_stock:
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
        for x in range(0, len(data)):
            item = data[x]
            self.insert_or_update_base(self,item)
        db.session.commit()


class StockSummaryVolume(BaseMixin,db.Model):
    __tablename__ = "stock_summary_volume"
    date = Column(db.DateTime,primary_key=True,nullable=False)  
    code = Column(String(10),primary_key=True,nullable=False)  
    name = Column(String(8),nullable=False)
    vol_5m =Column(Float,nullable=False)
    vol_10m =Column(Float,nullable=False)
    vol_15m =Column(Float,nullable=False)
    vol_20m =Column(Float,nullable=False)
    vol_25m =Column(Float,nullable=False)
    vol_30m =Column(Float,nullable=False)
    vol_35m =Column(Float,nullable=False)
    vol_40m =Column(Float,nullable=False)
    vol_45m =Column(Float,nullable=False)
    vol_50m =Column(Float,nullable=False)
    vol_55m =Column(Float,nullable=False)
    vol_60m =Column(Float,nullable=False)
    h_vol =Column(Integer,nullable=False)

class StockIndicators(BaseMixin,db.Model):
    __tablename__ = "stock_indicators"
    date = Column(db.DateTime,primary_key=True,nullable=False)  
    code = Column(String(10),primary_key=True,nullable=False)  
    name = Column(String(8),nullable=False)
    vol = Column(Float,nullable=False)
    macd = Column(Float,nullable=False)
    dif = Column(Float,nullable=False)
    dea = Column(Float,nullable=False)
    cci = Column(Float,nullable=False)




# def get_stock_model(cid, cid_class_dict={}):
#     if cid not in cid_class_dict:
#         cls_name = table_name = f'stock_{cid}'
#         cls = type(cls_name, (StockIndicators, ), {'__tablename__': table_name  })
#         cid_class_dict[cid] = cls
#     return cid_class_dict[cid]
