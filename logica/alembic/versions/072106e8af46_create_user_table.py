"""create user table

Revision ID: 072106e8af46
Revises: 
Create Date: 2023-03-01 00:36:29.834283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '072106e8af46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nick_name', sa.String(50), nullable=False),
        sa.Column('full_name', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('account')
