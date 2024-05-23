"""removed UQ on values

Revision ID: 8568245f42ab
Revises: 369074c15279
Create Date: 2024-05-23 11:05:11.849630

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8568245f42ab'
down_revision: Union[str, None] = '369074c15279'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('values_value_key', 'values', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('values_value_key', 'values', ['value'])
    # ### end Alembic commands ###