from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import vars

token = vars.TOKEN

bot = Bot(token=token)
dp = Dispatcher(bot)

print(bot)

# only text
@dp.message_handler()  # тут фильтры можно добавлять
async def get_message_then_send(message: types.Message):
    # from user id
    chat_id = message.chat.id
    text = "важное сообщение!"
    result_send_message = await bot.send_message(chat_id=chat_id, text=text)
    print(result_send_message)

    # задание 1
    # - Необходимо отправить нашим ботом в группу с chat_id = -1001359487461 фотографию, которую вы нашли в интернете по ссылке: https://i.pinimg.com/originals/f4/d2/96/f4d2961b652880be432fb9580891ed62.png
    result_send_message = await bot.send_photo(chat_id=chat_id,
                                               photo="https://i.pinimg.com/originals/f4/d2/96/f4d2961b652880be432fb9580891ed62.png")
    print(result_send_message.photo[-1].file_unique_id)
    # задание 2
    # У вас есть чат-группа с chat_id = -1001359487461, где находится ваш бот-админ. Вы хотите этим ботом установить новое название чата "Моя мини-супер группа" (или придумайте своё). Сделайте это с помощью запроса через API.
    try:
        result_send_message = await bot.set_chat_title(chat_id=chat_id, title="Как же могучи могучь!")
        # Can't change private chat title
        print(result_send_message)
    except:
        pass

    # Найдите эту группу (она приватная, поэтому есть только инвайт ссылка) с помощью нужного метода по chat_id = -1001359487461 и зайдите в нее, и насладитесь результатом своей работы! (после этого можете сразу выходить)
    try:
        invite_link = await bot.export_chat_invite_link(chat_id=chat_id)
        # Can't invite members to a private chat
        print(invite_link)
    except:
        pass

    # Определите username вышеуказанного бота с помощью любого метода.
    bot_user = await bot.get_me()
    print(bot_user.username)



# в start_polling запускается как сбор update
# так вся их проработка до попадания в handler
executor.start_polling(dp)
