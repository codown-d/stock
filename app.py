# coding:utf-8
from core import create_app, db
from flask_script import Manager


# 创建flask的应用对象
app = create_app("dev")

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
