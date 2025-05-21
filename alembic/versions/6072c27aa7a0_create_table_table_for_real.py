"""create table table for real

Revision ID: 6072c27aa7a0
Revises: 80fafebcdb4c
Create Date: 2025-05-20 17:04:14.838818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6072c27aa7a0'
down_revision: Union[str, None] = '80fafebcdb4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
