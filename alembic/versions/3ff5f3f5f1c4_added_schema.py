"""added schema

Revision ID: 3ff5f3f5f1c4
Revises: 92c89d9a7ab6
Create Date: 2024-02-02 02:44:00.260914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ff5f3f5f1c4'
down_revision: Union[str, None] = '92c89d9a7ab6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
