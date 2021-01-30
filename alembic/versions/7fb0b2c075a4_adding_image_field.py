"""adding Image Field

Revision ID: 7fb0b2c075a4
Revises: bdcf5521b1c1
Create Date: 2021-01-25 17:06:02.503358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fb0b2c075a4'
down_revision = 'bdcf5521b1c1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(

        'posts',
        sa.Column('url', sa.String(200))
    )


def downgrade():
    pass
