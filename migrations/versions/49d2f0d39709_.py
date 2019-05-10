"""empty message

Revision ID: 49d2f0d39709
Revises: 2491c2746123
Create Date: 2019-05-10 21:02:37.514295

"""

# revision identifiers, used by Alembic.
revision = '49d2f0d39709'
down_revision = '2491c2746123'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('files', sa.Column('Downloads', sa.Integer(), nullable=True))
    op.add_column('files', sa.Column('Read_num', sa.Integer(), nullable=True))
    op.add_column('files', sa.Column('category', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('files', 'category')
    op.drop_column('files', 'Read_num')
    op.drop_column('files', 'Downloads')
    # ### end Alembic commands ###