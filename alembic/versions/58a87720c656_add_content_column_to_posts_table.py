"""add content column to posts table

Revision ID: 58a87720c656
Revises: 76087e5f0155
Create Date: 2022-05-18 20:16:02.828044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58a87720c656'
down_revision = '76087e5f0155'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
