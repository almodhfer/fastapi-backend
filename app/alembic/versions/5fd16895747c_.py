"""empty message

Revision ID: 5fd16895747c
Revises: 4f3bb3087985
Create Date: 2020-05-31 19:43:18.999586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fd16895747c'
down_revision = '4f3bb3087985'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('is_superuser', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_superuser')
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###