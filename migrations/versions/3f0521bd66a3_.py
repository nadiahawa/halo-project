"""empty message

Revision ID: 3f0521bd66a3
Revises: 903096fe6bea
Create Date: 2022-06-11 21:16:08.053699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f0521bd66a3'
down_revision = '903096fe6bea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('character', sa.Column('quantity', sa.Float(precision=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('character', 'quantity')
    # ### end Alembic commands ###
