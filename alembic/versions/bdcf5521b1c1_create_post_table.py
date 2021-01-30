"""create post table

Revision ID: bdcf5521b1c1
Revises: b44300fa6522
Create Date: 2021-01-24 21:47:59.239258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdcf5521b1c1'
down_revision = 'b44300fa6522'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('title', sa.String(50), unique = True),
        sa.Column('body', sa.String(1000)),
        sa.Column('owner_id', sa.Integer),
        sa.Column('is_active', sa.Boolean),
        sa.Column('created_date', sa.DateTime),
        
    )


def downgrade():
    pass
