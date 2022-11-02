from aiogram import types
from aiogram.dispatcher.filters import Text

import database as db
import keyboards.keyboards as kb
from data import texts, paths_images
from loader import dp


@dp.message_handler(commands='start')
@dp.callback_query_handler(Text('start'))
async def start(message: types.Message):
    """Стартовое сообщение"""
    if 'data' in message:
        await message.message.delete()

    user_id = message.from_user.id
    user_data = await db.getters.get_user_data(user_id)

    if not user_data:
        user_data = (
            user_id,
            message.from_user.first_name,
            message.from_user.username,
            message.date
        )
        await db.setters.add_new_user(user_data)

    with open(paths_images.START_PHOTO, 'rb') as photo:
        await dp.bot.send_photo(
            user_id,
            photo,
            caption=texts.START,
            reply_markup=await kb.start_menu()
        )
