"""empty message

Revision ID: 126abaea015e
Revises: 3be2a2de8aad
Create Date: 2020-01-20 03:09:09.045612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '126abaea015e'
down_revision = '3be2a2de8aad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('reply_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['reply_id'], ['message.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_timestamp'), 'message', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_message_timestamp'), table_name='message')
    op.drop_table('message')
    # ### end Alembic commands ###