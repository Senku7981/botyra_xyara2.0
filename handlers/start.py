from aiogram import types
from aiogram.dispatcher.filters import Text

from db import db_session
from db.db_func import *
import database as db
import keyboards.keyboards as kb
from data import texts, paths_images
from loader import dp


@dp.message_handler(commands='start')
@dp.callback_query_handler(Text('start'))
async def start(message: types.Message):
    print('test')
    dp.bot.send_message(message.chat.id, 'test')
# async def start(message: types.Message):
#     """Стартовое сообщение"""
#     db_sess = db_session.create_session()
#     if 'data' in message:
#         await message.message.delete()

    # user_id = message.from_user.id
    # user_data = await get_user(db_sess, user_id)

    # if not user_data:
    #     user_data = (
    #         user_id,
    #         message.from_user.first_name,
    #         message.from_user.username,
    #         message.date
    #     )
        # await create_user(db_sess, user_id)

    # with open(paths_images.START_PHOTO, 'rb') as photo:
    #     await dp.bot.send_photo(
    #         user_id,
    #         photo,
    #         caption=texts.START,
    #         reply_markup=await kb.start_menu()
    #     )
    # print('created')
