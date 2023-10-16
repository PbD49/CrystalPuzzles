"""add token table in db

Revision ID: 36710f8c8464
Revises: cdaa796e56a8
Create Date: 2023-10-16 17:25:10.906325

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '36710f8c8464'
down_revision: Union[str, None] = 'cdaa796e56a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('access_token', sa.String(length=450), nullable=False),
    sa.Column('refresh_token', sa.String(length=450), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('access_token')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token')
    # ### end Alembic commands ###