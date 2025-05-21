"""create table table

Revision ID: d5958c36e8ef
Revises: 38538e8aeef4
Create Date: 2025-05-20 16:48:57.981445

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5958c36e8ef'
down_revision: Union[str, None] = '38538e8aeef4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
