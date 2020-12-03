from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
#  я нужен для того чтобы предварительно обработать апдейт например на предмет
# пользователя например проверить язык пользователя