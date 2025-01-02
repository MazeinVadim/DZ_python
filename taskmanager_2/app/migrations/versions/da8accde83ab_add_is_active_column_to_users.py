"""Add is_active column to users

Revision ID: da8accde83ab
Revises: 2011779c390d
Create Date: 2025-01-01 20:13:05.286468

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da8accde83ab'
down_revision: Union[str, None] = '2011779c390d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###