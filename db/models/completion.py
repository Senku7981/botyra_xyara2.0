import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from ..db_session import SqlAlchemyBase


class Completion(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'completions'
    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, autoincrement=True, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer)
    time = sqlalchemy.Column(sqlalchemy.DateTime)
    result = sqlalchemy.Column(sqlalchemy.Integer)
    quiz_name = sqlalchemy.Column(sqlalchemy.Text)