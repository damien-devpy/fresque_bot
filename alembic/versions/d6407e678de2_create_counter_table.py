"""create counter table

Revision ID: d6407e678de2
Revises: 
Create Date: 2021-04-29 21:27:35.068349

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'd6407e678de2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'counter',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('counter', sa.BigInteger),
        sa.Column('date', sa.DateTime),
    )


def downgrade():
    op.drop_table('counter')
