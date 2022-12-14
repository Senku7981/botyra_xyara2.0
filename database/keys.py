USERS = ('user_id', 'first_name', 'username', 'date_reg')
RESULT_QUIZZES = ('user_id', 'level_quiz', 'result')


async def get_keys_for_query(keys):
    """Возвращает ключи для запроса"""
    variables = str(keys)
    values = ', '.join(['?' for _ in keys])

    return variables, values