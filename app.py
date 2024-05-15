# coding:utf-8
from core import create_app
from flask_migrate import Migrate
from core.models import db


# 创建flask的应用对象
app = create_app("dev")
Migrate(app,db)

if __name__ == '__main__':
    app.run()
