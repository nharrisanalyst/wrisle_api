"""create table table for real

Revision ID: cbba7eedf476
Revises: 6072c27aa7a0
Create Date: 2025-05-20 17:04:42.674814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbba7eedf476'
down_revision: Union[str, None] = '6072c27aa7a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
