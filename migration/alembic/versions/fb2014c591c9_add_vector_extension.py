"""add_vector_extension

Revision ID: fb2014c591c9
Revises: b007da527345
Create Date: 2024-08-24 01:15:17.220075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb2014c591c9'
down_revision: Union[str, None] = 'b007da527345'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector;")


def downgrade() -> None:
    op.execute("DROP EXTENSION IF EXISTS vector;")
