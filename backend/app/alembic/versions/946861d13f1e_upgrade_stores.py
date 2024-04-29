"""upgrade stores

Revision ID: 946861d13f1e
Revises: a1649fa23599
Create Date: 2024-04-28 14:03:13.149071

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '946861d13f1e'
down_revision = 'a1649fa23599'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'stock_unit')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('stock_unit', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###