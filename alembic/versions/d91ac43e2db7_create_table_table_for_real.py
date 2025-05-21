"""create table table for real

Revision ID: d91ac43e2db7
Revises: 857e30038452
Create Date: 2025-05-20 17:00:19.950581

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd91ac43e2db7'
down_revision: Union[str, None] = '857e30038452'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
