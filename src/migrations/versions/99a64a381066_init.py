"""Init

Revision ID: 99a64a381066
Revises: 
Create Date: 2023-06-01 16:44:04.766813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99a64a381066'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('telegram_id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('telegram_id', name=op.f('uq_users_telegram_id')),
    sa.UniqueConstraint('user_name', name=op.f('uq_users_user_name'))
    )
    op.create_table('urls',
    sa.Column('original_url', sa.TEXT(), nullable=False),
    sa.Column('shorted_url', sa.TEXT(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), nullable=False),
    sa.Column('telegram_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['telegram_id'], ['users.telegram_id'], name=op.f('fk_urls_telegram_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_urls'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('urls')
    op.drop_table('users')
    # ### end Alembic commands ###
