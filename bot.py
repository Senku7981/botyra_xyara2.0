from aiogram import executor, bot
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db import db_session
from data import config
from database import work_db
from loader import dp
import logging
import asyncio



async def on_startup(dp):
    """Действия при запуске бота"""
    print('Бот запущен!')

    # Создание БД и таблиц в ней
    await work_db.create_tables()
    # await db_session.global_init('database/database.sqlite')


async def main():
    """initialize and run bot"""
    bot = Bot(config.TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    await on_startup(dp)
    await dp.start_polling()
    # finally:
    #     await on_shutdown(dp)
    #     await bot.session.close()

# if __name__ == '__main__':
#     # db_session.global_init('database/database.sqlite')
#     executor.start_polling(dp, on_startup=on_startup)
if __name__ == '__main__':
    asyncio.run(main())
    # except (KeyboardInterrupt, SystemExit):
    #     logging.info("Bye!")
