"""Add first_name, last_name, birthdate to User

Revision ID: 5236a6ec17b8
Revises: b15bf5f0876d
Create Date: 2025-04-18 18:15:07.197861

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5236a6ec17b8'
down_revision: Union[str, None] = 'b15bf5f0876d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
