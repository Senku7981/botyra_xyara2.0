import sqlite3


DB_PATH = 'database/database.sqlite'


async def get_connect(db_name=DB_PATH):
    '''Возвращает подключение к БД'''
    return sqlite3.connect(db_name)


async def execute_query(query, params=None, fetch=False, db_name=DB_PATH):
    '''Отправляет запрос к БД'''
    connect = await get_connect(db_name)
    cursor = connect.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    if fetch == 'one':
        return cursor.fetchone()
    elif fetch == 'all':
        return cursor.fetchall()

    connect.commit()
    connect.close()


async def create_tables():
    '''Создание таблиц в БД'''
    users = '''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        username TEXT,
        date_reg TIMESTAMP
    );
    '''
    result_quizzes = '''
    CREATE TABLE IF NOT EXISTS result_quizzes (
        user_id INTEGER,
        level_quiz TEXT,
        result INTEGER
    );
    '''

    await execute_query(users)
    await execute_query(result_quizzes)