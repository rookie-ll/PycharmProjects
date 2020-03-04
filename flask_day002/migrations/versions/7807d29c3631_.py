"""empty message

Revision ID: 7807d29c3631
Revises: 
Create Date: 2019-04-13 03:09:21.022484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7807d29c3631'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('class_one',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_jsj',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('tel', sa.String(length=11), nullable=True),
    sa.Column('c_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['c_id'], ['class_one.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_jsj')
    op.drop_table('class_one')
    # ### end Alembic commands ###