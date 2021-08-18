import logging
import random

from aiogram import Bot, Dispatcher, executor, types

#тут токен должен быть токен!
TOKEN = 'null' 

#логгинг
logging.basicConfig(level=logging.INFO)

#переменные
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#старт и хелп
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет {}!".format(message.from_user.first_name))
    await message.answer_sticker(r'CAACAgIAAxkBAAECuaBhE6f5SBpuIdJbBbrhslSZBw26VAACsQ0AAjppOUjINKv7N0gdWiAE')
    await message.reply("Мои команды:\n/random - Рандомное число от 1 до 100\n/shiza - Проверка на шизоида\n/droch - Вздрочнуть")
    print("Команда /start использована.")

#рандомайзер
@dp.message_handler(commands=['random'])
async def send_random(message: types.Message):
    await message.reply("Твоё рандомное число: {} " .format(random.randint(1, 100)))
    print("Команда /random использована.")

 # проверка на шизоида
@dp.message_handler(commands=['shiza'])
async def send_random(message: types.Message):
    await message.reply("<b>🦠 {}, ты шизоид на {}%!</b>" .format(message.from_user.first_name, random.randint(0, 100)), parse_mode=types.ParseMode.HTML)
    print("Команда /shiza использована.")

# дроч
@dp.message_handler(commands=['droch'])
async def droch_reply(message: types.Message):
    await message.reply("<b>{}, ты успешно вздрочнул! 💦</b>" .format(message.from_user.first_name), parse_mode=types.ParseMode.HTML)
    print("Команда /droch использована.")

#хандлер новый участник
@dp.message_handler(content_types=["new_chat_members"])
async def on_user_join(message: types.Message):
    await message.reply("<b>Привет {} 👋! Добро пожаловать в чат, я санитарша.</b>" .format(message.new_chat_members[0].first_name), parse_mode=types.ParseMode.HTML)
    print("Хандлер новый участник использован.")

#хандлер участник покинул
@dp.message_handler(content_types=["left_chat_member"])
async def on_user_join(message: types.Message):
    await message.reply("<b>Прощай {}! Фу кидок, ненавижу 😡.</b>" .format(message.from_user.first_name), parse_mode=types.ParseMode.HTML)
    print("Хандлер участник покинул использован.")

#эхо
@dp.message_handler()
async def send_echo(message: types.Message):
    await message.answer(message.text)

#long polling
if __name__ == '__main__':
    print("Бот запущен успешно.")
    executor.start_polling(dp, skip_updates=True)