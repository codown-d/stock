#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import datetime
import logging
import os.path
import sys
from flask import Flask



cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
print(cpath)
sys.path.append(cpath)
from job.save_stock_vol import save_stocks_vol
from job.get_stock_volume import  batch_tasks_volume, handle_error_tick_volume, handle_vol
from core.models import db
from config import config_map
logging.basicConfig(filename="logs/log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)

app = Flask(__name__)

# 根据配置模式的名字获取配置参数的类
config_class = config_map.get('dev')
app.config.from_object(config_class)
def main():   
    start = time.time()
    _start = datetime.datetime.now()
    logging.info("######## 任务执行时间: %s #######" % _start.strftime("%Y-%m-%d %H:%M:%S.%f"))
    # 获取每日最新股票数据
    with app.app_context():
        db.init_app(app)
        # batch_tasks_volume()
        # handle_error_tick_volume()
        save_stocks_vol()
    logging.info("######## 完成任务, 使用时间: %s 秒 #######" % (time.time() - start))

# main函数入口
if __name__ == '__main__':
    main()
