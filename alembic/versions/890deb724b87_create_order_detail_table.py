"""create order detail table

Revision ID: 890deb724b87
Revises: 06bfdcfcad38
Create Date: 2023-12-23 17:49:33.178304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '890deb724b87'
down_revision: Union[str, None] = '06bfdcfcad38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'order_detail',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('order_id', sa.Integer, nullable=False),
        sa.Column('product_id', sa.Integer, nullable=False),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('price', sa.Integer, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=False))

    op.create_foreign_key('fk_order_detail_order_id', 'order_detail', 'order', ['order_id'], ['id'])


def downgrade() -> None:
    op.drop_constraint('fk_order_detail_order_id', 'order_detail', type_='foreignkey')
    op.drop_table('order_detail')
