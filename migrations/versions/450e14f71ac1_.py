"""empty message

Revision ID: 450e14f71ac1
Revises: 22f979f6daef
Create Date: 2022-12-08 09:31:28.971834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '450e14f71ac1'
down_revision = '22f979f6daef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_ingredients',
    sa.Column('user_ingredient_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ingredient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.ingredient_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_ingredient_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_ingredients')
    # ### end Alembic commands ###
