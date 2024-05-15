#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import datetime
import logging
import os.path
import sys
from flask import current_app
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)
from core.fetch_stocks import fetch_stocks

def main():
    start = time.time()
    _start = datetime.datetime.now()
    print('current_app',current_app)
    current_app.logger.info("######## 任务执行时间: %s #######" % _start.strftime("%Y-%m-%d %H:%M:%S.%f"))
    # 获取每日最新股票数据
    fetch_stocks()
    current_app.logger.info("######## 完成任务, 使用时间: %s 秒 #######" % (time.time() - start))

# main函数入口
if __name__ == '__main__':
    main()
