from aiogram import types
from aiogram.dispatcher.filters import Text

import keyboards.keyboards as kb
from data import texts
from loader import dp


@dp.callback_query_handler(Text('basic_info'))
async def select_museum(call: types.CallbackQuery):
    '''Выбор музея'''
    await call.answer()
    await call.message.delete()
    await call.message.answer(
        texts.SELECT_MUSEUM,
        reply_markup=await kb.select_museum()
    )


@dp.callback_query_handler(Text(startswith='museum_'))
async def send_info_museum(call: types.CallbackQuery):
    '''Отправляет информацию о музее'''
    await call.answer()
    await call.message.delete()
    museum = int(call.data.split('_')[-1])
    path_photo, caption = texts.MUSEUMS[museum].values()

    with open(path_photo, 'rb') as photo:
        await call.message.answer_photo(
            photo,
            caption=caption,
            reply_markup=await kb.museum_buttons()
        )