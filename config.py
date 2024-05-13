# coding:utf-8

# import redis


class Config(object):
    """配置信息"""
    SECRET_KEY = "XHSOI*Y9dfs9cshd9"
    DIALCT = "mysql"
    DRITVER = "pymysql"
    HOST = "localhost"  # 数据库服务主机
    USERNAME = "root"  # 数据库访问用户
    PASSWORD = "123456"  # 数据库访问密码
    DATABASE = "stock"  # 数据库名称
    PORT = 3306  # 数据库服务端口
    CHARSET = "utf8mb4"  # 数据库字符集
    # 数据库
    SQLALCHEMY_DATABASE_URI = f"{DIALCT}+{DRITVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    # REDIS_HOST = "127.0.0.1"
    # REDIS_PORT = 6379

    # flask-session配置
    # SESSION_TYPE = "redis"
    # SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # SESSION_USE_SIGNER = True  # 对cookie中session_id进行隐藏处理
    # PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期，单位秒


class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}