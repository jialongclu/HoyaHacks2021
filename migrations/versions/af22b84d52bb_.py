"""empty message

Revision ID: af22b84d52bb
Revises: 50780a4c6441
Create Date: 2021-01-30 14:47:57.768037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af22b84d52bb'
down_revision = '50780a4c6441'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweets',
    sa.Column('tweet_id', sa.BigInteger(), nullable=False),
    sa.Column('tweet', sa.String(), nullable=True),
    sa.Column('tweet_sentiment', sa.Integer(), nullable=True),
    sa.Column('tweet_name', sa.String(), nullable=True),
    sa.Column('tweet_username', sa.String(), nullable=True),
    sa.Column('tweet_likes', sa.Integer(), nullable=True),
    sa.Column('tweet_datestamp', sa.Date(), nullable=True),
    sa.Column('day1Price', sa.Float(), nullable=True),
    sa.Column('day2Price', sa.Float(), nullable=True),
    sa.Column('day3Price', sa.Float(), nullable=True),
    sa.Column('day4Price', sa.Float(), nullable=True),
    sa.Column('day5Price', sa.Float(), nullable=True),
    sa.Column('company', sa.String(), nullable=True),
    sa.Column('numOfTweets', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('tweet_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweets')
    # ### end Alembic commands ###
