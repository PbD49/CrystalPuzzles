"""Add deleted column in training

Revision ID: 6402face495f
Revises: 75e3aa08c6f2
Create Date: 2024-04-17 20:32:55.893766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6402face495f'
down_revision: Union[str, None] = '75e3aa08c6f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Trainings', sa.Column('deleted', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Trainings', 'deleted')
    # ### end Alembic commands ###
