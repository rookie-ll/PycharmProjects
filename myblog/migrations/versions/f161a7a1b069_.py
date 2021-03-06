"""empty message

Revision ID: f161a7a1b069
Revises: 126abaea015e
Create Date: 2020-02-10 02:02:57.434765

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f161a7a1b069'
down_revision = '126abaea015e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=100), nullable=True))
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=100), nullable=True))
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###
