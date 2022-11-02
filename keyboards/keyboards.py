from aiogram import types

from data import texts


async def get_inline_button(button_data):
    """Возвращает inline-кнопку"""
    text, data = button_data
    params_button = {'text': text}

    if data.startswith('http'):
        params_button['url'] = data
    else:
        params_button['callback_data'] = data

    return types.InlineKeyboardButton(**params_button)


async def get_keyboard(buttons_user, type_kb='inline', row_width=1):
    """Генерирует и возвращает клавиатуру"""
    if type_kb == 'inline':
        keyboard = types.InlineKeyboardMarkup(row_width=row_width)
        buttons = []

        for i in buttons_user:
            if type(i) == list:
                row = []

                for b_data in i:
                    row.append(await get_inline_button(b_data))

                buttons.append(row)
            else:
                buttons.append(await get_inline_button(i))
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                             row_width=row_width)
        buttons = []

        for i in buttons_user:
            if type(i) == 'list':
                row = []

                for text in i:
                    row.append(types.KeyboardButton(text))

                buttons.append(row)
            else:
                buttons.append(types.KeyboardButton(i))

    for row in buttons:
        keyboard.add(*row)

    return keyboard


async def start_menu():
    """Кнопки на старте"""
    buttons = [
        [
            (texts.START_BUTTON_1, 'basic_info'),
            (texts.START_BUTTON_2, 'quizzes'),
        ]
    ]

    return await get_keyboard(buttons)


async def select_museum():
    """Выбор музея"""
    buttons = [
        [
            (texts.MUSEUM_BUTTON_1, 'museum_1'),
            (texts.MUSEUM_BUTTON_2, 'museum_2'),
            (texts.MUSEUM_BUTTON_3, 'museum_3'),
            (texts.MUSEUM_BUTTON_4, 'museum_4'),
            (texts.MUSEUM_BUTTON_5, 'museum_5'),
            (texts.BACK_BUTTON, 'start'),
        ]
    ]

    return await get_keyboard(buttons)


async def museum_buttons():
    """Кнопки под информацией о музее"""
    buttons = [
        [
            (texts.OPERATOR_BUTTON, texts.OPERATOR_LINK),
            (texts.BACK_BUTTON, 'basic_info')
        ]
    ]

    return await get_keyboard(buttons)


async def select_level():
    """Выбор уровня сложности"""
    buttons = [
        [
            (texts.LEVEL_1, 'qz_level_1'),
            (texts.LEVEL_2, 'qz_level_2'),
            (texts.LEVEL_3, 'qz_level_3'),
            (texts.BACK_BUTTON, 'start')
        ]
    ]

    return await get_keyboard(buttons)


async def select_right_answer(level, current_question):
    """Выбор правильного ответа"""
    variants_answer = texts.QUIZZES[level][current_question]['variants_answer']
    right_answer = texts.QUIZZES[level][current_question]['right_answer_id']
    buttons = [[]]

    for num, _ in enumerate(variants_answer, 1):
        cb = 'right' if num == right_answer else 'wrong'
        buttons[0].append(
            (num, cb)
        )

    return await get_keyboard(buttons, row_width=4)
