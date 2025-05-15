"""add last few columns to posts table

Revision ID: edc7f5a7ddbd
Revises: 62baf92a41e8
Create Date: 2025-05-14 15:30:12.078782

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edc7f5a7ddbd'
down_revision: Union[str, None] = '62baf92a41e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    
    pass
