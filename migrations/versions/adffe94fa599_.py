"""empty message

Revision ID: adffe94fa599
Revises: 26c7947f37e0
Create Date: 2024-05-22 15:39:35.559907

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'adffe94fa599'
down_revision = '26c7947f37e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stock_indicators', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=mysql.DATETIME(),
               type_=sa.String(length=32),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stock_indicators', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.String(length=32),
               type_=mysql.DATETIME(),
               existing_nullable=False)

    # ### end Alembic commands ###