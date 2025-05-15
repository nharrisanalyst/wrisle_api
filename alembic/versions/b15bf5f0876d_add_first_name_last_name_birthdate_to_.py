"""Add first_name, last_name, birthdate to User

Revision ID: b15bf5f0876d
Revises: aa595e4bfd19
Create Date: 2025-04-18 18:12:10.077415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b15bf5f0876d'
down_revision: Union[str, None] = 'aa595e4bfd19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
