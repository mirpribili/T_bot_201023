# загружаем переменные
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

#
# инстанс класса бот с помощью которого мы будем делать все
# запросы к телеге по тем методам которые он предлагает
# каждый метод асинхронный - выдает карунтину)
# просто так метод для асинхронного вызова нельзя написать его
# нужно ставить в поток
# например from asyncio import get_event_loop
# получаем поток
# loop = get_event_loop()
# но тк поток и так создается в диспатчере сделаем еще проще
# dp.loop.run_util_complete(bot.send_message(args...))
# тогда не нужно делать await оно само принимает карутины и выполняет их
#
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
#

#
#
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
