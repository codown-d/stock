
import os.path
import sys
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)

from core.models import db

def check_table_exists(table_name):
    """check table exists"""
    inspector = db.inspect(db.engine)
    return inspector.has_table(table_name)

def table_drop_all():
    """check table exists""" 
    db.drop_all()
    db.create_all()
def update_orm_object(orm_object, data):
    for key, value in data.items():
        if hasattr(orm_object, key):
            setattr(orm_object, key, value)
class BaseMixin():
    @classmethod
    def insert_or_update_base(self,stockData):
        ID=stockData['ID']
        existing_stock = self.query.filter_by(ID=ID).first()
        if existing_stock:
            pass
            # update_orm_object(existing_stock, stockData)
        else:
            stock = self(**stockData)
            db.session.add(stock)
    # 插入或更新数据
    @classmethod
    def insert_or_update(self,data:dict):
        self.insert_or_update_base(data)
        db.session.commit()
    # 插入或更新多条数据
    @classmethod
    def insert_or_update_all(self,data:list):
        for x in range(0, len(data)):
            item = data[x]
            self.insert_or_update_base(item)
        db.session.commit()

