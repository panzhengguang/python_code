"""initial migration

Revision ID: 20e6db366b15
Revises: 39f910c890e4
Create Date: 2015-12-27 20:44:58.065000

"""

# revision identifiers, used by Alembic.
revision = '20e6db366b15'
down_revision = '39f910c890e4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('body_html', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_comments_timestamp', 'comments', ['timestamp'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_comments_timestamp', 'comments')
    op.drop_table('comments')
    ### end Alembic commands ###
