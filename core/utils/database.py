from core.models import db

def check_table_exists(table_name):
    """check table exists"""
    inspector = db.inspect(db.engine)
    return inspector.has_table(table_name)

def table_drop_all():
    """check table exists""" 
    db.drop_all()
    db.create_all()

