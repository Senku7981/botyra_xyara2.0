import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from ..db_session import SqlAlchemyBase


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users'
    user_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True)
    reg_time = sqlalchemy.Column(sqlalchemy.DateTime)