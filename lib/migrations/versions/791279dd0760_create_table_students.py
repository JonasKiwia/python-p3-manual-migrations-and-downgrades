"""Rename column 'name' to 'full_name' in students

Revision ID: 1a2b3c4d5e6f
Revises: 791279dd0760
Create Date: 2022-12-20 11:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1a2b3c4d5e6f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Rename column 'name' to 'full_name'
    op.alter_column('students', 'name', new_column_name='full_name')

def downgrade() -> None:
    # Rename column 'full_name' back to 'name'
    op.alter_column('students', 'full_name', new_column_name='name')
