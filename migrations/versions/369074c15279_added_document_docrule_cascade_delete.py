"""added document docRule cascade delete

Revision ID: 369074c15279
Revises: cf223989b82b
Create Date: 2024-05-23 00:34:38.569642

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '369074c15279'
down_revision: Union[str, None] = 'cf223989b82b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('queue_doc_type_id_fkey', 'queue', type_='foreignkey')
    op.create_foreign_key(None, 'queue', 'docrules', ['doc_type_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'queue', type_='foreignkey')
    op.create_foreign_key('queue_doc_type_id_fkey', 'queue', 'docrules', ['doc_type_id'], ['id'])
    # ### end Alembic commands ###