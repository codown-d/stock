import os.path
import sys
from flask import Flask
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from tqdm import tqdm
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)
from core.models import db, get_stock_model
from job.fetch_stock_Info import get_stock_code
from config import config_map
app = Flask(__name__)

config_class = config_map.get("dev")
app.config.from_object(config_class)
db = SQLAlchemy(app)

# def init_db():
#     # 1. 获取数据列表
#     temp_df = get_stock_code()
#     code_list = temp_df.to_dict(orient='records') 
#     total=len(code_list)
#     # 2. 动态创建数据库表
#     for data in tqdm(code_list, total=total):
#         code = data['code']
#         get_stock_model(code)
#     # 初始化数据库表
#     with app.app_context():
#         print('create table start')
#         db.create_all() #执行这个代码先导入所有的db model

#     print('create table success end')

# def execute_sql():
#     # 创建参数化查询的查询字符串
#     with app.app_context():
#         db.drop_all()
# if __name__ == '__main__':
#     execute_sql()