from . import keys
from .work_db import *


async def add_new_user(user_data):
    """Добавление нового пользователя"""
    query = '''
    INSERT INTO users
        {}
    VALUES
        ({});
    '''.format(*await keys.get_keys_for_query(keys.USERS))

    await execute_query(query, user_data)


async def add_result_quiz(user_id, level, result):
    """Добавляет результат в таблицу"""
    query = '''
    INSERT INTO result_quizzes
        {}
    VALUES
        ({});
    '''.format(*await keys.get_keys_for_query(keys.RESULT_QUIZZES))

    await execute_query(query, [user_id, level, result])
