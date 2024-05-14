#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import datetime
import logging
import os.path
import sys
from flask import current_app

import backtest_data_daily_job as bdj

def main():
    start = time.time()
    _start = datetime.datetime.now()
    current_app.logger.info("######## 任务执行时间: %s #######" % _start.strftime("%Y-%m-%d %H:%M:%S.%f"))
    # 创建股票回测
    bdj.main()
    current_app.logger.info("######## 完成任务, 使用时间: %s 秒 #######" % (time.time() - start))

# main函数入口
if __name__ == '__main__':
    main()
