from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='stop')
button3 = types.KeyboardButton(text='Информация')
button4 = types.KeyboardButton(text='showanimal')
button5 = types.KeyboardButton(text='close')
button6 = types.KeyboardButton(text='make')
button7 = types.KeyboardButton(text='live')
keyboard1 = [
    
 [button1, button2, button3, button4, button5],
 [button6, button7],
]
keyboard2 = [
    
 [button1, button2, button3],
 
 
] 
 
 

keyboard1 = types.ReplyKeyboardMarkup(keyboard=keyboard1)

keyboard2 = types.ReplyKeyboardMarkup(keyboard=keyboard2)