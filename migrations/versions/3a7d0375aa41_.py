"""empty message

Revision ID: 3a7d0375aa41
Revises: 409c10e8f747
Create Date: 2022-06-20 18:03:23.460239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a7d0375aa41'
down_revision = '409c10e8f747'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('special',
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('affiliation', sa.String(length=100), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(precision=50), nullable=True),
    sa.Column('quantity', sa.Float(precision=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('affiliation', sa.String(length=100), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(precision=50), nullable=True),
    sa.Column('quantity', sa.Float(precision=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    op.drop_table('special')
    # ### end Alembic commands ###
