"""Initial

Revision ID: 99de26d58206
Revises: 
Create Date: 2023-11-21 22:48:27.613274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "99de26d58206"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "links",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("url", sa.String(length=255), nullable=False),
        sa.Column("time_visited", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("links")
    # ### end Alembic commands ###