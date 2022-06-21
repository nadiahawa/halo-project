"""empty message

Revision ID: bf120e5be46c
Revises: adaf37f0c3f0
Create Date: 2022-06-20 17:22:45.453919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf120e5be46c'
down_revision = 'adaf37f0c3f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cartitems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(length=255), nullable=True),
    sa.Column('cart', sa.Integer(), nullable=True),
    sa.Column('item_type', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['cart'], ['cart.id'], ),
    sa.ForeignKeyConstraint(['item'], ['character.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('cart_item_fkey', 'cart', type_='foreignkey')
    op.drop_constraint('cart_author_fkey', 'cart', type_='foreignkey')
    op.drop_column('cart', 'author')
    op.drop_column('cart', 'item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('item', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('cart', sa.Column('author', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_foreign_key('cart_author_fkey', 'cart', 'user', ['author'], ['id'])
    op.create_foreign_key('cart_item_fkey', 'cart', 'character', ['item'], ['id'])
    op.drop_table('cartitems')
    # ### end Alembic commands ###