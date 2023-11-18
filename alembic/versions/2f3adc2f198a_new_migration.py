"""New Migration

Revision ID: 2f3adc2f198a
Revises: 
Create Date: 2023-11-18 10:26:49.867291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f3adc2f198a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('titatic',
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('Name', sa.String(), nullable=False),
    sa.Column('Survived', sa.String(), nullable=True),
    sa.Column('Pclass', sa.Integer(), nullable=True),
    sa.Column('Sex', sa.String(), nullable=True),
    sa.Column('Age', sa.Numeric(), nullable=True),
    sa.Column('Siblings_Spouses_Aboard', sa.Integer(), nullable=True),
    sa.Column('Parents_Children_Aboard', sa.Integer(), nullable=True),
    sa.Column('Fare', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('Name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('titatic')
    # ### end Alembic commands ###
