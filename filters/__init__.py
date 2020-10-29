# from aiogram import Dispatcher
#
# # from .is_admin import AdminFilter
#
# def setup(dp: Dispatcher):
#     # dp.filters_factory.bind(AdminFilter)
#     pass
from aiogram import Dispatcher

# ИМПОРТИРУЕМ фильтр
from .private_chat import IsPrivate


def setup(dp: Dispatcher):
    # регистрируем фильтр
    dp.filters_factory.bind(IsPrivate)
