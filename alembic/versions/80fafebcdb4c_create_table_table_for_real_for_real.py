"""create table table for real for real

Revision ID: 80fafebcdb4c
Revises: d91ac43e2db7
Create Date: 2025-05-20 17:02:57.707325

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80fafebcdb4c'
down_revision: Union[str, None] = 'd91ac43e2db7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
