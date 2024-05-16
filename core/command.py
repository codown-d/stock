import click
from flask import Blueprint
import os
os.environ['NUMEXPR_MAX_THREADS'] = '16'
from core.utils.database import check_table_exists,table_drop_all

db_cmd = Blueprint('database', __name__ , cli_group=None)

@db_cmd.cli.command('check_table_exists')
@click.argument('table_name')
def check_table_exists_cmd(table_name):
    """check table exists
    :param table_name: string
    :return:bool"""
    exist=check_table_exists(table_name)
    if exist:
        print(f"Table {table_name} exists")
    else:
        print(f"Table {table_name} does not exist")
    return exist

@db_cmd.cli.command('table_drop_all')
def table_drop_all_cmd():
    """删除表并创建新的表"""
    table_drop_all()
