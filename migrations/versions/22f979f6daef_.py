"""empty message

Revision ID: 22f979f6daef
Revises: 
Create Date: 2022-12-06 14:22:45.828760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22f979f6daef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredients',
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('ingredient_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('ingredients')
    # ### end Alembic commands ###
