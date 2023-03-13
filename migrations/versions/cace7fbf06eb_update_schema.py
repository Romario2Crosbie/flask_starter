"""update schema

Revision ID: cace7fbf06eb
Revises: 3e5f06c21344
Create Date: 2023-03-12 20:43:05.572160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cace7fbf06eb'
down_revision = '3e5f06c21344'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('property_type', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('num_bedrooms', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('num_bathrooms', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('photo', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='properties_pkey')
    )
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    
    # ### end Alembic commands ###
