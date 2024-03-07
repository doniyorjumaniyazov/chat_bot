import asyncio
import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging
import random
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher()
keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        types.KeyboardButton(text="Информация")
    ]
])
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
 name = message.chat.first_name
 await message.answer(f"Привет, {name}", reply_markup=keyboard2)
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
 await message.reply("Я бот - твой друг и товарищ ")
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())

