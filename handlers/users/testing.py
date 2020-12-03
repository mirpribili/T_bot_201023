from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.test import Test

#Если вы задали пользователю состояние таким образом...
#await MyGroup.SuperState.set()
#Дальше пользователь вводит какой-то текст и вы ловите его. Как вы будете ловить его в хендлере?
#@dp.message_handler(state=MyGroup.SuperState)



# Кроме группы состояний можно использовать строковые значения\

@dp.message_handler(state="enter_email")
async def answer_q2(message: types.Message, state: FSMContext):
    await message.answer("OK")
    # await state.reset_data()
    await state.finish()


@dp.message_handler(state="please_email")
async def answer_q2(message: types.Message, state: FSMContext):
    await message.answer("ВВедите Ваш почтовый:")
    await state.set_state("enter_email")


# Сделаем фильтр на комманду text="/test", где не будет указано никакого состояния
@dp.message_handler(Command("test"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование.\n"
                         "Вопрос №1. \n\n"
                         "Вы часто занимаетесь бессмысленными делами "
                         "(бесцельно блуждаете по интернету, клацаете пультом телевизора, просто смотрите в потолок)?")
    # Заполняем
    # states/test.py
    # ====> Q1 = State() # необычные фильтры

    # Вариант 1 - с помощью функции сет
    # но это карутина
    await Test.Q1.set()

    # Вариант 2 - с помощью first
    # await Test.first()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # Ваирант 2 получения state
    # state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    # Вариант 1 сохранения переменных - записываем через key=var
    # Если у вас запись идет какого-то параметра (например email) то записывайте не answer,
    # а email, чтобы потом было понятно что именно доставать
    await state.update_data(answer1=answer)

    # Вариант 2 - передаем как словарь
    await state.update_data(
        {"answer1": answer}
    )

    # Вариант 3 - через state.proxy
    # ассинхронный генератор
    async with state.proxy() as data:
        data["answer1"] = answer
        # Удобно, если нужно сделать data["some_digit"] += 1
        # Или data["some_list"].append(1), т.к. не нужно сначала доставать из стейта, А потом задавать

    await message.answer("Вопрос №2. \n\n"
                         "Ваша память ухудшилась и вы помните то, что было давно, но забываете недавние события?")

    # await Test.next() / previous()
    # способ 2
    # await Test.Q2.set()
    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    # Достаем переменные из машины  состояний
    data = await state.get_data()
    temp = (await state.get_data()).get("answer1")
    #Как выгрузить сохраненные данные (какие-то данные "user") из машины состояний?
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Спасибо за ваши ответы!")
    await message.answer(f"Ответ 1: {answer1}")
    await message.answer(f"Ответ 2: {answer2}")

    await state.set_state("please_email")

    # СБрасываем пользоывателя разными состояниями чтобы он не оставлася
    # в ответе 2 вечно
    # Вариант 1
    # await state.finish()

    # Вариант завершения 2
    # await state.reset_state()

    # Вариант завершения 3 - без стирания данных в data
    # await state.reset_state(with_data=False)
    # await state.reset_data()
