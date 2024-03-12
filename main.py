import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import keyboard1, keyboard2
from image import fox
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher()
keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        types.KeyboardButton(text="Информация")
    ]
])
#Хендлер на команду
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
 name = message.chat.first_name
 await message.answer(f"на гап инди, {name}", reply_markup=keyboard1)
 
# @dp.message(Command("a"))
# async def cmd_a(message: types.Message):
#     name = message.chat.first_name 
#     await message.answer(f"ташкил бугунми шундо, {name}", reply_markup=keyboard2)

# @dp.message(Command("b"))
# async def cmd_b(message: types.Message):
#     name = message.chat.first_name 
#     await message.answer(f"нерда булжок, {name}", reply_markup=keyboard2) 

# @dp.message(Command("c"))
# async def cmd_c(message: types.Message):
#     name = message.chat.first_name 
#     await message.answer(f"менюда новило бор, {name}", reply_markup=keyboard2) 
    
# 
@dp.message (Command('showanimal'))
async def cmd_d(message: types.Message):
  
    name = message.chat.first_name 
    img_fox = fox()
    #await message.answer(f"what kind of animal do you want, {name}", reply_markup=keyboard1)
    await message.answer_photo(photo=img_fox)
    await bot.send_photo(message.from_user, photo=img_fox)




@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text
    #await message.answer(f'Ты написал: {msg_user}', reply_markup=keyboard2)
    name = message.chat.first_name
    if 'hello' in message.text.lower():
        await message.reply(f"И тебе привет, {name}, reply_markup=keyboard2")
    if 'by' in message.text.lower():
        await message.reply(f"Пока, {name}")
    

 
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())

