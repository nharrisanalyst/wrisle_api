"""create table table

Revision ID: 9760965ae006
Revises: d5958c36e8ef
Create Date: 2025-05-20 16:51:06.790209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9760965ae006'
down_revision: Union[str, None] = 'd5958c36e8ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
