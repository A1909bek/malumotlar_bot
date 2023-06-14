
import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5967138698:AAFBqy2hN8LQC8pr2I2qoB1pP7LGc4oI3Bo'

logging.basicConfig(level=logging.INFO)

wikipedia.set_lang('uz')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    await message.reply("Assalomu alaykum")



@dp.message_handler()
async def search(message: types.Message):

    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bunday maqola topilmadi!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)