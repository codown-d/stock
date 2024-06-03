# coding:utf-8

import datetime
import arrow
from werkzeug.routing import BaseConverter
from flask import session, jsonify, g
import functools
import numpy as np
import pandas as pd

# 定义正则转换器
class ReConverter(BaseConverter):
    """"""
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(ReConverter, self).__init__(url_map)
        # 保存正则表达式
        self.regex = regex


# 定义的验证登录状态的装饰器
def login_required(view_func):
    # wraps函数的作用是将wrapper内层函数的属性设置为被装饰函数view_func的属性
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        # 判断用户的登录状态
        user_id = session.get("user_id")

        # 如果用户是登录的， 执行视图函数
        if user_id is not None:
            # 将user_id保存到g对象中，在视图函数中可以通过g对象获取保存数据
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            # 如果未登录，返回未登录的信息
            return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录")

    return wrapper

def deep_merge_dicts(dict1, dict2):
    for key in dict2:
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            deep_merge_dicts(dict1[key], dict2[key])
        else:
            dict1[key] = dict2[key]
    return dict1

def get_time_date_trend(elem):
    elem_sort=sorted(elem.keys(),reverse=True)
    result=[]
    for key in elem_sort:
        result.append(int(elem[key]))
    return result

def gp_type_szsh(code:str):
    gp_type=''
    if code.find('60',0,3)==0 or code.find('68',0,4)==0:
        gp_type='sh'
    elif code.find('00',0,3)==0 or code.find('30',0,4)==0:
        gp_type='sz'
    return gp_type

def get_latest_quarter_list(quarter=9):
    year = datetime.date.today().year
    time_now = int(arrow.now().format("YYYYMMDD"))
    list = ['0331','0630','0930','1231']
    new_list=[]
    i = 0
    while i <=10:
        for num in list:
            time=int(f'{year-i}{num}')
            if(time_now>time):
                new_list.append(f'{time}')
        i +=1
    new_list.sort(reverse=True)
    return new_list[:quarter]

def calc_pre_minute_change(df,sec):
    volume= df['成交量'].resample(f'{sec}s', label='right', closed='left').sum()
    volume_price= df['成交额'].resample(f'{sec}s', label='right', closed='left').sum()
    new_df = pd.DataFrame({
    "成交量": volume,
    '成交额':volume_price
    })
    new_df['成交量变化率']=new_df['成交量'].pct_change()*100
    new_df['成交量累计变化'] =new_df["成交量变化率"].cumsum(axis=0)/100

    return new_df

if __name__ == '__main__':
    list = get_latest_quarter_list()
    print(list)