from core import db

def check_table_exists(table_name):
    """check table exists"""
    print(table_name,123,db)
    inspector = db.inspect()
    return inspector.has_table(table_name)

