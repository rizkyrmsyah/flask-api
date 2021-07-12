"""empty message

Revision ID: 4746b6db0550
Revises: 236305803ea6
Create Date: 2021-07-12 10:00:56.787003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4746b6db0550'
down_revision = '236305803ea6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user_activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.TEXT(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('user_activities')
