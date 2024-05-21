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
        print('stockData',self)
        date=stockData['date']
        f12=stockData['f12']
        existing_stock = self.query.filter_by(date=date,f12=f12).first()
        if existing_stock:
            update_orm_object(existing_stock, stockData)
        else:
            stock = self(**stockData)
            db.session.add(stock)
    # 插入或更新数据
    @classmethod
    def insert_or_update(self,data:dict):
        BaseMixin.insert_or_update_base(data)
        db.session.commit()
    # 插入或更新多条数据
    @classmethod
    def insert_or_update_all(self,data:list):
        for x in range(0, len(data)):
            item = data[x]
            BaseMixin.insert_or_update_base(item)
        db.session.commit()

