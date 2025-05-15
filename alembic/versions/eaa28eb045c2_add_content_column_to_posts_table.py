"""add content column to posts table

Revision ID: eaa28eb045c2
Revises: e8e5c23e0e72
Create Date: 2025-05-14 14:44:08.095416

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eaa28eb045c2'
down_revision: Union[str, None] = 'e8e5c23e0e72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content',sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
