"""Initial commit

Revision ID: 8c59120d1a66
Revises: 
Create Date: 2024-02-05 19:39:12.679435

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c59120d1a66'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('trainer_id', sa.Integer(), nullable=True),
    sa.Column('DateAdd', sa.DateTime(), nullable=False),
    sa.Column('DateUpdate', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['trainer_id'], ['user.id'], use_alter=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Roles',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('DateAdd', sa.DateTime(), nullable=False),
    sa.Column('DateUpdate', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Tasks',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('DateAdd', sa.DateTime(), nullable=False),
    sa.Column('DateUpdate', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Ranks',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('DateAdd', sa.DateTime(), nullable=False),
    sa.Column('DateUpdate', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['Tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('email', sa.String(length=254), nullable=False),
    sa.Column('hashed_password', sa.String(length=128), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=True),
    sa.Column('lastname', sa.String(length=50), nullable=True),
    sa.Column('surname', sa.String(length=50), nullable=True),
    sa.Column('code', sa.Integer(), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('is_man', sa.Boolean(), nullable=False),
    sa.Column('rank_id', sa.Integer(), nullable=True),
    sa.Column('contact', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('DateAdd', sa.DateTime(), nullable=False),
    sa.Column('DateUpdate', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['rank_id'], ['Ranks.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['Roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Tokens',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('access_token', sa.String(length=450), nullable=False),
    sa.Column('refresh_token', sa.String(length=450), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('DateAdd', sa.DateTime(), nullable=False),
    sa.Column('DateUpdate', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('access_token', 'id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Tokens')
    op.drop_table('Users')
    op.drop_table('Ranks')
    op.drop_table('Tasks')
    op.drop_table('Roles')
    op.drop_table('Groups')
    # ### end Alembic commands ###