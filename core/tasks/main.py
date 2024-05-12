# coding:utf-8


from celery import Celery
from core.tasks import config


# 定义celery对象
celery_app = Celery("core")

# 引入配置信息
celery_app.config_from_object(config)

# 自动搜寻异步任务
celery_app.autodiscover_tasks(["core.tasks.sms"])
