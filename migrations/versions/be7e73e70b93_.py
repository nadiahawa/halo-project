"""empty message

Revision ID: be7e73e70b93
Revises: 983d9aed4d3d
Create Date: 2022-05-30 19:30:41.795532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be7e73e70b93'
down_revision = '983d9aed4d3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'character')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('character', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
