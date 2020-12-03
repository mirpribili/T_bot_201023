# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
#
# from loader import dp
#
#
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f'Привет, {message.from_user.full_name}!')
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from loader import dp
from re import compile  # регулярки


from aiogram.utils.deep_linking import get_start_link


from loader import dp, bot
import logging

# Этот хендлер используется для диплинков в личной переписке:
# Когда пользователь переходит по ссылке http://t.me/username_bot?start=123
# Тогда по нажатию на кнопку start - боту приходит команда старт с аргументом 123
# Тогда мы можем отловить этот диплинк с помощью регулярных выражений (функция compile)
# \d\d\d - значит, что мы ловим 3 цифры подряд. (\d) - одна цифра

# encoded=True  ВНИМАНИЕ Если сюда попадет не зашифрованный линк то упадет! ставь меня после фильтров для не шифрованных
#@dp.message_handler(CommandStart(deep_link=compile(r"\d\d\d")), IsPrivate())
@dp.message_handler(CommandStart(deep_link=compile(r"\d\d\d"), encoded=True), IsPrivate())
async def bot_start_deeplink(message: types.Message):
    # С помощью функции get_args забираем аргументы после команды start. (для примера выше - будет "123")
    deep_link_args = message.get_args()

    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке. \n'
                         f'В вашей команде есть диплинк\n'
                         f'Вы передали аргумент {deep_link_args}.\n'
                         f'Ваш ID {message.from_user.id}'
                         )


# CommandStart(deep_link=None) МЕНЯ вниз или я съем все)

# В этом хендлере мы ловим простое нажатие на команду /start, не прошедшее под условие выше
@dp.message_handler(CommandStart(deep_link=None), IsPrivate())
async def bot_start(message: types.Message):
    # Для создания диплинк-ссылки - нужно получить юзернейм бота
    bot_user = await dp.bot.get_me()

    # Формируем диплинк-ссылку
    # deep_link = f"http://t.me/{bot_user.username}?start=123"
    # аналог в новых версиях)
    #deep_link = await get_start_link("123")
    deep_link = await get_start_link("123", encode=True)

    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке. \n'
                         f'В вашей команде нет диплинка.\n'
                         f'Ваша диплинк ссылка - {deep_link}')

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    non_existing_user = 666666

    # Не попадает в эррор хендер, обрабатывается тут с помощью try
    try:
        await message.answer("Неправильно закрыт <b>тег<b>")
    except Exception as err:
        await message.answer(f"Не попало в эррор хендлер. Ошибка: {err}")

    # Не попадает в эррор хендер
    try:
        await bot.send_message(chat_id=non_existing_user, text="Не существующий пользователь")
    except Exception as err:
        await message.answer(f"Не попало в эррор хендлер. Ошибка: {err}")

    # Попадает отсюда в эррор хендлер
    await message.answer("Не существует <kek>тега</kek>")
    logging.info("Это не выполнится, но бот не упадет.")

    # Все что ниже - не выполнится, но бот не упадет

    await message.answer("...")




