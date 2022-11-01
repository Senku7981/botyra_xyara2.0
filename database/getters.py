from . import keys
from .work_db import *


async def get_user_data(user_id):
    '''Возвращает данные пользователя'''
    query = '''
    SELECT
        *
    FROM
        users
    WHERE
        user_id = ?
    '''
    user_data = await execute_query(query, [user_id], fetch='one')

    if user_data:
        return dict(zip(keys.users, user_data))