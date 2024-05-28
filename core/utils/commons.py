# coding:utf-8

from werkzeug.routing import BaseConverter
from flask import session, jsonify, g
import functools


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

def gp_type_szsh(gp):
    gp_type=''
    code = gp['code']
    if code.find('60',0,3)==0:
        gp_type='sh'
    elif code.find('00',0,3)==0:
        gp_type='sz'
    elif code.find('688',0,4)==0:
        gp_type='sh'
    elif code.find('300',0,4)==0:
        gp_type='sz'
    return gp_type!=''