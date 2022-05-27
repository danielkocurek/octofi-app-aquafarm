"""empty message

Revision ID: b70a0d3ff50d
Revises: 74bf8eefcafd
Create Date: 2022-05-27 21:20:30.846759

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b70a0d3ff50d'
down_revision = '74bf8eefcafd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('region', sa.JSON(), nullable=False),
    sa.Column('experience_year', sa.Integer(), nullable=False),
    sa.Column('education', sa.String(length=128), nullable=False),
    sa.Column('salary', sa.String(length=128), nullable=True),
    sa.Column('roles', postgresql.ARRAY(sa.String(length=128)), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jobs')
    # ### end Alembic commands ###
