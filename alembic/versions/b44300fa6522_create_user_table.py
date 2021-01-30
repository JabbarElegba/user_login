"""create user table

Revision ID: b44300fa6522
Revises: 
Create Date: 2021-01-24 18:26:56.855732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b44300fa6522'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('username', sa.String(50), unique = True),
        sa.Column('hashed_password', sa.String(50)),
        sa.Column('email', sa.String(50)),
        sa.Column('is_active', sa.Boolean),
        sa.Column('created_date', sa.DateTime),
        
    )

def downgrade():
    pass
