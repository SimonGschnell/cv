"""empty message

Revision ID: f1b4741024fe
Revises: fbfb2be5a026
Create Date: 2020-03-15 12:11:13.551869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1b4741024fe'
down_revision = 'fbfb2be5a026'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=400), nullable=True),
    sa.Column('logo', sa.String(length=400), nullable=True),
    sa.Column('date', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects')
    # ### end Alembic commands ###
