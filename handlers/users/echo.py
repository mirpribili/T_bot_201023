# from aiogram import types
# from loader import dp
#
#
# @dp.message_handler()
# async def bot_echo(message: types.Message):
#     await message.answer(message.text)
from aiogram import types
from loader import dp


# ПОРЯДОК ИМЕЕТ ЗНАЧЕНИЕ 1й ТОТ ЧТО ВЫШЕ


# 1й способ регистрации хендлера
# dp.register_message_handler(наша ф-я)

# 2й способ регистрации хендлера
# @dp.message_handler() # по умолчанию чюда летят content_types=types.ContentTypes.TEXT
# Если хотите что то другое ловить то указывайте тип явно типа
# content_types==types.ContentTypes.PHOTO
#
# допустим нужно ловить channel_post тогда
# @dp.channel_post_handler()
@dp.message_handler()
async def bot_echo(message: types.Message):
    # тайп хинт для подсказок))
    # types.Message) а тут можно найти всет ипы объектов доступные в телеграме)
    # message. ...

    # Эхо бот)

    # Получим chat_id и text
    chat_id = message.from_user.id
    text = message.text

    # Получим объект бота - вариант 1 (из диспатчера)
    # bot = dp.bot

    # Получим объект бота - вариант 2 (из контекста)
    # from aiogram import Bot
    # bot = Bot.get_current()

    # Получим объект бота - вариант 3 (из модуля loader)
    from loader import bot

    # Отправим сообщение пользователю - вариант 1
    await bot.send_message(chat_id=chat_id, text=text)

    # Отправим сообщение пользователю - вариант 2 (без ввода chat_id)
    # await message.answer(text=text)

    # Отправим сообщение пользователю - вариант 3 (с реплаем)
    # await message.reply(text=text)
    # аналог
    # await bot.send_message(chat_id=chat_id, text=text, reply_to_message_id=message.message_id)
