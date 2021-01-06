"""empty message

Revision ID: c0c481b096e0
Revises: 
Create Date: 2021-01-04 13:24:24.585111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0c481b096e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actors', sa.Column('movie_id', sa.Integer(), nullable=True))
    op.drop_constraint('actors_movie_fkey', 'actors', type_='foreignkey')
    op.create_foreign_key(None, 'actors', 'movies', ['movie_id'], ['id'])
    op.drop_column('actors', 'movie')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actors', sa.Column('movie', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'actors', type_='foreignkey')
    op.create_foreign_key('actors_movie_fkey', 'actors', 'movies', ['movie'], ['id'])
    op.drop_column('actors', 'movie_id')
    # ### end Alembic commands ###