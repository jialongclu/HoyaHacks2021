"""empty message

Revision ID: 52113a059b4b
Revises: d91b4f2e1569
Create Date: 2021-01-30 11:15:28.241894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52113a059b4b'
down_revision = 'd91b4f2e1569'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweets',
    sa.Column('tweet_id', sa.BigInteger(), nullable=False),
    sa.Column('tweet', sa.String(), nullable=True),
    sa.Column('tweet_sentiment', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('likes_count', sa.Integer(), nullable=True),
    sa.Column('datestamp', sa.String(), nullable=True),
    sa.Column('day1Price', sa.Float(), nullable=True),
    sa.Column('day2Price', sa.Float(), nullable=True),
    sa.Column('day3Price', sa.Float(), nullable=True),
    sa.Column('day4Price', sa.Float(), nullable=True),
    sa.Column('day5Price', sa.Float(), nullable=True),
    sa.Column('company', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('tweet_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweets')
    # ### end Alembic commands ###
