"""empty message

Revision ID: 7fb6c7b970b6
Revises: 
Create Date: 2022-05-03 11:05:16.531236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fb6c7b970b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auditorium',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('CustomerCapacity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('customers',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=40), nullable=False),
    sa.Column('lastName', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phoneNumber', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phoneNumber')
    )
    op.create_table('movies',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=25), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('auditoriumId', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['auditoriumId'], ['auditorium._id'], ),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('tickets',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('no_of_tickets', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers._id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movies._id'], ),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('orders',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('ticket_id', sa.Integer(), nullable=True),
    sa.Column('total_amount', sa.Integer(), nullable=True),
    sa.Column('payment_reference', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ticket_id'], ['tickets._id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('tickets')
    op.drop_table('movies')
    op.drop_table('customers')
    op.drop_table('auditorium')
    # ### end Alembic commands ###
