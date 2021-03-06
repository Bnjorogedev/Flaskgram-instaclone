"""added social

Revision ID: 2379dc128d44
Revises: 95a05dbbc659
Create Date: 2020-08-15 22:15:17.911736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2379dc128d44'
down_revision = '95a05dbbc659'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('social', sa.String(length=64), nullable=False))
        batch_op.create_unique_constraint(batch_op.f('uq_user_social'), ['social'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_social'), type_='unique')
        batch_op.drop_column('social')

    # ### end Alembic commands ###
