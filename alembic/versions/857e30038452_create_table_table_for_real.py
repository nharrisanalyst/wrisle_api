"""create table table for real

Revision ID: 857e30038452
Revises: e6994841a418
Create Date: 2025-05-20 16:58:12.014603

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '857e30038452'
down_revision: Union[str, None] = 'e6994841a418'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
