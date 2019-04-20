"""empty message

Revision ID: 9fd4289321e3
Revises: b64885e0ef81
Create Date: 2019-04-20 18:52:13.749046

"""

# revision identifiers, used by Alembic.
revision = '9fd4289321e3'
down_revision = 'b64885e0ef81'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###