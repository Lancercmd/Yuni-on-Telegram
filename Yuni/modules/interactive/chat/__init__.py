import config

from aiogram import Bot, Dispatcher

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def start(message):
    await message.answer('''Yuni on Telegram
Powered by aiogram.''')

async def test(message):
    await message.answer(message)