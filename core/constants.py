# coding:utf-8

from sqlalchemy import FLOAT

# 图片验证码的redis有效期, 单位：秒
IMAGE_CODE_REDIS_EXPIRES = 180

# 短信验证码的redis有效期, 单位：秒
SMS_CODE_REDIS_EXPIRES = 300

# 发送短信验证码的间隔, 单位：秒
SEND_SMS_CODE_INTERVAL = 60

# 登录错误尝试次数
LOGIN_ERROR_MAX_TIMES = 5

# 登录错误限制的时间, 单位：秒
LOGIN_ERROR_FORBID_TIME = 600

# 七牛的域名
QINIU_URL_DOMAIN = "http://o91qujnqh.bkt.clouddn.com/"

# 城区信息的缓存时间, 单位：秒
AREA_INFO_REDIS_CACHE_EXPIRES = 7200

# 首页展示最多的房屋数量
HOME_PAGE_MAX_HOUSES = 5

# 首页房屋数据的Redis缓存时间，单位：秒
HOME_PAGE_DATA_REDIS_EXPIRES = 7200

# 房屋详情页展示的评论最大数
HOUSE_DETAIL_COMMENT_DISPLAY_COUNTS = 30

# 房屋详情页面数据Redis缓存时间，单位：秒
HOUSE_DETAIL_REDIS_EXPIRE_SECOND = 7200

# 房屋列表页面每页数据容量
HOUSE_LIST_PAGE_CAPACITY = 2

# 房屋列表页面页数缓存时间，单位秒
HOUES_LIST_PAGE_REDIS_CACHE_EXPIRES = 7200

# 支付宝的网关地址（支付地址域名）
ALIPAY_URL_PREFIX = "https://openapi.alipaydev.com/gateway.do?"

STOCK={
    "DFCF":{
        "f2":'最新价',
        "f3":'涨跌幅',
        "f4":'涨跌额',
        "f5":'成交量',
        "f6":'成交额',
        "f7":'振幅',
        "f8":'换手率',
        "f10":'量比',
        "f11":'5分钟涨跌',
        "f12":'代码',
        "f13":'市盈率(动)',
        "f14":'名称',
        "f15":'最高',
        "f16":'最低',
        "f17":'今开',
        "f18":'昨收',
        "f20":'总市值',
        "f21":'流通市值',
        "f22":'涨速',
        "f23":'市净率',
        "f24":'60日涨跌幅',
        "f25":'年初至今涨跌幅',
        "f26":'上市时间',
        "f37":'加权净资产收益率',
        "f38":'总股本',
        "f39":'已流通股份',
        "f40":'营业收入',
        "f41":'营业收入同比增长',
        "f45":'归属净利润',
        "f46":'归属净利润同比增长',
        "f48":'每股未分配利润',
        "f49":'毛利率',
        "f57":'资产负债率',
        "f61":'每股资本公积金',
        "f100":'所处行业',
        "f112":'每股收益',
        "f113":'每股净资产',
        "f114":'市盈率(静)',
        "f115":'市盈率TTM',
        "f221":'报告期',
    }
}
STOCK_BASE_IND={
    'macd':{},
    'macds':{},
    'macdh':{}
}