import click
from flask import Blueprint,current_app

from job import execute_daily_job
from .utils.database import check_table_exists

database_cmd = Blueprint('database', __name__ , cli_group=None)

@database_cmd.cli.command('check_table_exists_cmd')
@click.argument('name')
def check_table_exists_cmd(name):
    """check table exists"""
    check_table_exists(name)

# @current_app.teardown_appcontext
# def teardown_db(exception):
#     execute_daily_job()