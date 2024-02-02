"""added tags

Revision ID: 92c89d9a7ab6
Revises: c93c5edda0e9
Create Date: 2024-02-02 02:01:45.335378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92c89d9a7ab6'
down_revision: Union[str, None] = 'c93c5edda0e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
