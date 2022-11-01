from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import keyboards.keyboards as kb
import database as db
from data import texts
from loader import dp


@dp.callback_query_handler(Text('quizzes'))
async def select_level(call: types.CallbackQuery):
    '''Выбор уровня сложности'''
    await call.answer()
    await call.message.delete()
    await call.message.answer(
        texts.SELECT_LEVEL,
        reply_markup=await kb.select_level()
    )


@dp.callback_query_handler(Text(startswith='qz_level_'))
@dp.callback_query_handler(
    lambda call: call.data == 'wrong' or call.data == 'right'
)
async def send_question(call: types.CallbackQuery, state: FSMContext):
    '''Отправляет вопрос'''
    await call.answer()

    if 'qz' in call.data:
        level = f'level_{call.data.split("_")[-1]}'
        current_question = 1
        await state.update_data(
            level=level,
            current_question=current_question,
            count_right_answer=0
        )
    else:
        state_data = await state.get_data()
        level = state_data['level']
        current_question = state_data['current_question'] + 1
        count_right_answer = state_data['count_right_answer']

        if call.data == 'right':
            count_right_answer += 1

        await state.update_data(
            current_question=current_question,
            count_right_answer=count_right_answer
        )

    if not texts.QUIZZES[level].get(current_question):
        await send_result_quiz(call, state)
        return

    msg_text = (
        f'{texts.QUIZZES[level][current_question]["text"]}\n\n'
        '<b>Варианты ответов:</b>\n'
    )
    variants_answer = texts.QUIZZES[level][current_question]['variants_answer']
    msg_text += (
        '\n'.join(
            [
                f'<b>{num}.</b> {answer}' for num, answer in enumerate(
                variants_answer, 1)
            ]
        )
    )

    await call.message.edit_text(
        msg_text,
        reply_markup=await kb.select_right_answer(level, current_question)
    )


async def send_result_quiz(call: types.CallbackQuery, state: FSMContext):
    '''Отправляет результат викторины'''
    await call.answer()
    await call.message.delete()
    state_data = await state.get_data()

    # Подсчёт результата в процентах
    count_right_answer = state_data['count_right_answer']
    level = state_data['level']
    count_questions = len(texts.QUIZZES[level])
    result = int((count_right_answer / count_questions * 100))

    # Запись результата в таблицу БД
    user_id = call.from_user.id
    await db.setters.add_result_quiz(user_id, level, result)

    # Отправка результата пользователю
    if result <= 40:
        msg_text = texts.RESULT_QUIZ_40.format(result=result)
    elif 40 < result <= 80:
        msg_text = texts.RESULT_QUIZ_60.format(result=result)
    else:
        msg_text = texts.RESULT_QUIZ_80.format(result=result)

    await call.message.answer(
        msg_text
    )

    await state.reset_state()