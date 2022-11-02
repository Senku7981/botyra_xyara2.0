from aiogram import executor, bot
from db import db_session

from database import work_db
from loader import dp


async def on_startup(dp):
    """Действия при запуске бота"""
    print('Бот запущен!')

    # Создание БД и таблиц в ней
    await work_db.create_tables()
    # await db_session.global_init('database/database.sqlite')

if __name__ == '__main__':
    # db_session.global_init('database/database.sqlite')
    executor.start_polling(dp, on_startup=on_startup(dp))
