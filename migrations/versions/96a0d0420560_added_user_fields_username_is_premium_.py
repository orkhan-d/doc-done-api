"""added user fields username, is_premium and is_premium_due

Revision ID: 96a0d0420560
Revises: 6fdec64cd698
Create Date: 2024-05-14 18:07:29.345111

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96a0d0420560'
down_revision: Union[str, None] = '6fdec64cd698'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(), nullable=True))
    op.add_column('users', sa.Column('is_premium', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('is_premium_due', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_premium_due')
    op.drop_column('users', 'is_premium')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
