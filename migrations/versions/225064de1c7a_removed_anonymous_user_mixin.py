"""REMOVED ANONYMOUS USER MIXIN

Revision ID: 225064de1c7a
Revises: d36c356b03d4
Create Date: 2020-08-20 11:55:16.457640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '225064de1c7a'
down_revision = 'd36c356b03d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=60),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=60),
               nullable=True)

    # ### end Alembic commands ###
