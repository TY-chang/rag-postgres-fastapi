"""add_knowledgebase

Revision ID: b007da527345
Revises: 
Create Date: 2024-08-23 21:08:04.030050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b007da527345'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # create knowledgebase table
    op.execute(
        """
        CREATE TABLE knowledgebase (
            id SERIAL PRIMARY KEY,
            raw_title text not null,
            raw_content text not null,
            parsed_embedding vector(3072) not null,
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW()
        );
        """
    )


def downgrade() -> None:
    op.execute("DROP TABLE knowledgebase;")
