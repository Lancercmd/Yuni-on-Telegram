import config
import sys

from aiogram import Bot, Dispatcher, executor, types
from os import path

sys.path.append(path.dirname(__file__))

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# ====================================================================== Logger
from Yuni.modules.bot_management import logger

# ====================================================================== Chat
from Yuni.modules.interactive import chat

@dp.message_handler(commands=['start', 'help'])
async def _(message: types.Message):
    since = await logger.start(message)
    await chat.start(message)
    await logger.end(message, since)

#@dp.message_handler(commands=['test'])
async def _(message: types.Message):
    since = await logger.start(message)
    await chat.test(message)
    await logger.end(message, since)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)