"""Initial migration

Revision ID: e1ee4763b458
Revises: 
Create Date: 2024-10-22 03:55:44.319185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1ee4763b458'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id_role', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id_role')
    )
    op.create_table('user',
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('role', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id_user'),
    sa.UniqueConstraint('email')
    )
    op.create_table('form',
    sa.Column('id_form', sa.Integer(), nullable=False),
    sa.Column('name_form', sa.String(length=100), nullable=True),
    sa.Column('id_admin', sa.Integer(), nullable=True),
    sa.Column('fields', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['id_admin'], ['user.id_user'], ),
    sa.PrimaryKeyConstraint('id_form')
    )
    op.create_table('route',
    sa.Column('id_route', sa.Integer(), nullable=False),
    sa.Column('name_route', sa.String(length=100), nullable=True),
    sa.Column('id_admin', sa.Integer(), nullable=True),
    sa.Column('id_salesperson', sa.Integer(), nullable=True),
    sa.Column('checkin_history', sa.JSON(), nullable=True),
    sa.Column('checkout_history', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['id_admin'], ['user.id_user'], ),
    sa.ForeignKeyConstraint(['id_salesperson'], ['user.id_user'], ),
    sa.PrimaryKeyConstraint('id_route')
    )
    op.create_table('statistics',
    sa.Column('id_statistics', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('total_routes_completed', sa.Integer(), nullable=True),
    sa.Column('avg_checkin', sa.Float(), nullable=True),
    sa.Column('avg_checkout', sa.Float(), nullable=True),
    sa.Column('avg_route_time', sa.Float(), nullable=True),
    sa.Column('completion_percentage', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.id_user'], ),
    sa.PrimaryKeyConstraint('id_statistics')
    )
    op.create_table('form_response',
    sa.Column('id_form_response', sa.Integer(), nullable=False),
    sa.Column('id_salesperson', sa.Integer(), nullable=True),
    sa.Column('id_route', sa.Integer(), nullable=True),
    sa.Column('id_form', sa.Integer(), nullable=True),
    sa.Column('responses', sa.JSON(), nullable=True),
    sa.Column('photo', sa.String(length=200), nullable=True),
    sa.Column('geolocation', sa.JSON(), nullable=True),
    sa.Column('checkin_time', sa.DateTime(), nullable=True),
    sa.Column('checkout_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_form'], ['form.id_form'], ),
    sa.ForeignKeyConstraint(['id_route'], ['route.id_route'], ),
    sa.ForeignKeyConstraint(['id_salesperson'], ['user.id_user'], ),
    sa.PrimaryKeyConstraint('id_form_response')
    )
    op.create_table('geolocation',
    sa.Column('id_geolocation', sa.Integer(), nullable=False),
    sa.Column('id_salesperson', sa.Integer(), nullable=True),
    sa.Column('id_route', sa.Integer(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_route'], ['route.id_route'], ),
    sa.ForeignKeyConstraint(['id_salesperson'], ['user.id_user'], ),
    sa.PrimaryKeyConstraint('id_geolocation')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('geolocation')
    op.drop_table('form_response')
    op.drop_table('statistics')
    op.drop_table('route')
    op.drop_table('form')
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###
