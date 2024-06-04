import os.path
import sys
from flask import Flask
from tqdm import tqdm
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)
from core.models import db, get_stock_model
from job.get_stock_code import get_stock_code
from config import config_map
app = Flask(__name__)

config_class = config_map.get("dev")
app.config.from_object(config_class)
db.init_app(app)

def init_db():
    # 1. 获取数据列表
    temp_df = get_stock_code()
    code_list = temp_df.to_dict(orient='records') 
    # 2. 动态创建数据库表
    for data in code_list:
        code = data['code']
        tqdm
        get_stock_model(code)
    # 初始化数据库表
    with app.app_context():
        print('create table start')
        db.create_all() #执行这个代码先导入所有的db model

    print('create table success end')
if __name__ == '__main__':
    init_db()