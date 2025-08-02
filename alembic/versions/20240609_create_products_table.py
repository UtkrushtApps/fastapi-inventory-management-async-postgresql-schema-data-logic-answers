"""
create products table

Revision ID: 20240609_create_products_table
Revises: 
Create Date: 2024-06-09
"""

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(length=255), nullable=False, unique=True, index=True),
        sa.Column('description', sa.String(length=1024), nullable=True),
        sa.Column('quantity', sa.Integer(), nullable=False, default=0),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')),        
    )

def downgrade():
    op.drop_table('products')
