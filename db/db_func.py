import sqlalchemy
import datetime
from sqlalchemy.orm import Session
from __all_models import *


async def create_user(db_sess: Session, user_id):
    """
    Добавление пользавателя в базу данных
    db_sess - текущая сессия
    user_id - id пользователя телеграмма
    """
    user = User()
    user.user_id = user_id
    user.reg_time = datetime.datetime.now()
    db_sess.add(user)
    db_sess.commit()


async def create_completion(db_sess: Session, user_id, result, quiz_name):
    """
    Добавление результата о выполнении викторины
    db_sess - текущая сессия
    user_id - id пользователя телеграмма
    result - результат выполнения викторины
    quiz_name = название викторины
    """
    completion = Completion()
    completion.user_id = user_id
    completion.result = result
    completion.quiz_name = quiz_name
    db_sess.add(completion)
    db_sess.commit()


async def get_user(db_sess: Session, user_id):
    user = db_sess.get(User, user_id)
    if not user:
        return False
    return user
