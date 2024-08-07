"""empty message

Revision ID: 517a45b2e62c
Revises: 73a3d004c227
Create Date: 2021-08-31 20:58:39.490140

"""

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '517a45b2e62c'
down_revision = '73a3d004c227'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'dashboards',
        sa.Column('uuid', sa.Text(), nullable=False),
        sa.Column('name', sa.Text(), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('is_archived', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('uuid'),
    )
    op.create_table(
        'explore_states',
        sa.Column('uuid', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('is_archived', sa.Boolean(), nullable=True),
        sa.Column('type', sa.Text(), nullable=False),
        sa.Column('state', sa.Text(), nullable=True),
        sa.Column('dashboard_id', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ['dashboard_id'],
            ['dashboards.uuid'],
        ),
        sa.PrimaryKeyConstraint('uuid'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('explore_states')
    op.drop_table('dashboards')
    # ### end Alembic commands ###
