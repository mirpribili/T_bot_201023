from utils.set_bot_commands import set_default_commands

# импортируем при запуске бота наши фильтры мидлевари
async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    # оповещает всех админов ято бот запущен и готов к работе

    await on_startup_notify(dp)

    # автоматичекски всплывающие подсказки с командами
    # по символу / типа /help итд
    await set_default_commands(dp)

# выполним код только при запуске имменно ээтого файла

if __name__ == '__main__':
    from aiogram import executor
    # ТУТ УЖЕ ИМПОРТИРУЕМ ВИДОИЗМЕНЕННЫЙ ДИСПАТЧЕР ПРОшедший через наши хендлеры
    from handlers import dp

# собирает наши update's
    # запускаем пулинг
    executor.start_polling(dp, on_startup=on_startup)
