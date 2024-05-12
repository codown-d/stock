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

STOCK_STATS_DATA = {'name': 'calculate_indicator', 'cn': '股票统计/指标计算助手库',
                    'columns': {'close': {'type': FLOAT, 'cn': '价格', 'size': 0},
                                'macd': {'type': FLOAT, 'cn': 'dif', 'size': 70},
                                'macds': {'type': FLOAT, 'cn': 'macd', 'size': 70},
                                'macdh': {'type': FLOAT, 'cn': 'histogram', 'size': 70},
                                'kdjk': {'type': FLOAT, 'cn': 'kdjk', 'size': 70},
                                'kdjd': {'type': FLOAT, 'cn': 'kdjd', 'size': 70},
                                'kdjj': {'type': FLOAT, 'cn': 'kdjj', 'size': 70},
                                'boll_ub': {'type': FLOAT, 'cn': 'boll上轨', 'size': 70},
                                'boll': {'type': FLOAT, 'cn': 'boll', 'size': 70},
                                'boll_lb': {'type': FLOAT, 'cn': 'boll下轨', 'size': 70},
                                'trix': {'type': FLOAT, 'cn': 'trix', 'size': 70},
                                'trix_20_sma': {'type': FLOAT, 'cn': 'trma', 'size': 70},
                                'tema': {'type': FLOAT, 'cn': 'tema', 'size': 70},
                                'cr': {'type': FLOAT, 'cn': 'cr', 'size': 70},
                                'cr-ma1': {'type': FLOAT, 'cn': 'cr-ma1', 'size': 70},
                                'cr-ma2': {'type': FLOAT, 'cn': 'cr-ma2', 'size': 70},
                                'cr-ma3': {'type': FLOAT, 'cn': 'cr-ma3', 'size': 70},
                                'rsi_6': {'type': FLOAT, 'cn': 'rsi_6', 'size': 70},
                                'rsi_12': {'type': FLOAT, 'cn': 'rsi_12', 'size': 70},
                                'rsi': {'type': FLOAT, 'cn': 'rsi', 'size': 70},
                                'rsi_24': {'type': FLOAT, 'cn': 'rsi_24', 'size': 70},
                                'vr': {'type': FLOAT, 'cn': 'vr', 'size': 70},
                                'vr_6_sma': {'type': FLOAT, 'cn': 'mavr', 'size': 70},
                                'roc': {'type': FLOAT, 'cn': 'roc', 'size': 70},
                                'rocma': {'type': FLOAT, 'cn': 'rocma', 'size': 70},
                                'rocema': {'type': FLOAT, 'cn': 'rocema', 'size': 70},
                                'pdi': {'type': FLOAT, 'cn': 'pdi', 'size': 70},
                                'mdi': {'type': FLOAT, 'cn': 'mdi', 'size': 70},
                                'dx': {'type': FLOAT, 'cn': 'dx', 'size': 70},
                                'adx': {'type': FLOAT, 'cn': 'adx', 'size': 70},
                                'adxr': {'type': FLOAT, 'cn': 'adxr', 'size': 70},
                                'wr_6': {'type': FLOAT, 'cn': 'wr_6', 'size': 70},
                                'wr_10': {'type': FLOAT, 'cn': 'wr_10', 'size': 70},
                                'wr_14': {'type': FLOAT, 'cn': 'wr_14', 'size': 70},
                                'cci': {'type': FLOAT, 'cn': 'cci', 'size': 70},
                                'cci_84': {'type': FLOAT, 'cn': 'cci_84', 'size': 70},
                                'tr': {'type': FLOAT, 'cn': 'tr', 'size': 70},
                                'atr': {'type': FLOAT, 'cn': 'atr', 'size': 70},
                                'dma': {'type': FLOAT, 'cn': 'dma', 'size': 70},
                                'dma_10_sma': {'type': FLOAT, 'cn': 'ama', 'size': 70},
                                'obv': {'type': FLOAT, 'cn': 'obv', 'size': 70},
                                'sar': {'type': FLOAT, 'cn': 'sar', 'size': 70},
                                'psy': {'type': FLOAT, 'cn': 'psy', 'size': 70},
                                'psyma': {'type': FLOAT, 'cn': 'psyma', 'size': 70},
                                'br': {'type': FLOAT, 'cn': 'br', 'size': 70},
                                'ar': {'type': FLOAT, 'cn': 'ar', 'size': 70},
                                'emv': {'type': FLOAT, 'cn': 'emv', 'size': 70},
                                'emva': {'type': FLOAT, 'cn': 'emva', 'size': 70},
                                'bias': {'type': FLOAT, 'cn': 'bias', 'size': 70},
                                'mfi': {'type': FLOAT, 'cn': 'mfi', 'size': 70},
                                'mfisma': {'type': FLOAT, 'cn': 'mfisma', 'size': 70},
                                'vwma': {'type': FLOAT, 'cn': 'vwma', 'size': 70},
                                'mvwma': {'type': FLOAT, 'cn': 'mvwma', 'size': 70},
                                'ppo': {'type': FLOAT, 'cn': 'ppo', 'size': 70},
                                'ppos': {'type': FLOAT, 'cn': 'ppos', 'size': 70},
                                'ppoh': {'type': FLOAT, 'cn': 'ppoh', 'size': 70},
                                'wt1': {'type': FLOAT, 'cn': 'wt1', 'size': 70},
                                'wt2': {'type': FLOAT, 'cn': 'wt2', 'size': 70},
                                'supertrend_ub': {'type': FLOAT, 'cn': 'supertrend_ub', 'size': 70},
                                'supertrend': {'type': FLOAT, 'cn': 'supertrend', 'size': 70},
                                'supertrend_lb': {'type': FLOAT, 'cn': 'supertrend_lb', 'size': 70},
                                'dpo': {'type': FLOAT, 'cn': 'dpo', 'size': 70},
                                'madpo': {'type': FLOAT, 'cn': 'madpo', 'size': 70},
                                'vhf': {'type': FLOAT, 'cn': 'vhf', 'size': 70},
                                'rvi': {'type': FLOAT, 'cn': 'rvi', 'size': 70},
                                'rvis': {'type': FLOAT, 'cn': 'rvis', 'size': 70},
                                'fi': {'type': FLOAT, 'cn': 'fi', 'size': 70},
                                'force_2': {'type': FLOAT, 'cn': 'force_2', 'size': 70},
                                'force_13': {'type': FLOAT, 'cn': 'force_13', 'size': 70},
                                'ene_ue': {'type': FLOAT, 'cn': 'ene上轨', 'size': 70},
                                'ene': {'type': FLOAT, 'cn': 'ene', 'size': 70},
                                'ene_le': {'type': FLOAT, 'cn': 'ene下轨', 'size': 70},
                                'stochrsi_k': {'type': FLOAT, 'cn': 'stochrsi_k', 'size': 70},
                                'stochrsi_d': {'type': FLOAT, 'cn': 'stochrsi_d', 'size': 70}}}
