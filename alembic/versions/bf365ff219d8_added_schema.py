"""added schema

Revision ID: bf365ff219d8
Revises: 3ff5f3f5f1c4
Create Date: 2024-02-02 02:51:17.375723

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf365ff219d8'
down_revision: Union[str, None] = '3ff5f3f5f1c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
