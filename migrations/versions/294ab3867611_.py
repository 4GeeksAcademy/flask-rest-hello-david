"""empty message

Revision ID: 294ab3867611
Revises: d6a1cf05edf1
Create Date: 2024-07-08 16:14:17.826359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '294ab3867611'
down_revision = 'd6a1cf05edf1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personas',
    sa.Column('id_persona', sa.Integer(), nullable=False),
    sa.Column('nombre_persona', sa.String(length=200), nullable=False),
    sa.Column('peso', sa.Integer(), nullable=False),
    sa.Column('color_de_piel', sa.String(length=50), nullable=False),
    sa.Column('color_de_pelo', sa.String(length=50), nullable=True),
    sa.Column('genero', sa.String(length=50), nullable=True),
    sa.Column('birth_year', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_persona')
    )
    op.create_table('planetas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_planeta', sa.String(length=100), nullable=False),
    sa.Column('periodo_rotacion', sa.Integer(), nullable=False),
    sa.Column('diametro', sa.Float(), nullable=False),
    sa.Column('clima', sa.String(length=50), nullable=False),
    sa.Column('terreno', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehiculos',
    sa.Column('id_vehiculos', sa.Integer(), nullable=False),
    sa.Column('nombre_vehiculos', sa.String(length=100), nullable=False),
    sa.Column('modelo', sa.String(length=90), nullable=False),
    sa.Column('longitud', sa.Float(), nullable=False),
    sa.Column('tripulacion', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_vehiculos')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehiculos')
    op.drop_table('planetas')
    op.drop_table('personas')
    # ### end Alembic commands ###
