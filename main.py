from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot('6339583214:AAEJZoonfPmU3CpUMH0WtuQfpRt0FPDOqfQ')
@bot.message_handler(commands=['help',  'start'])
async def send_welcome(message):
    await bot.reply_to(message, 'What`s up dude')

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    text_message = message.text
    text_message = text_message.lower()
    if 'дела' in message or 'настроение' in message:
        await bot.reply_to(message, 'Хорошо, а у тебя?')
    elif 'шутка' in message:
        await bot.reply_to(message, 'Колобок повесился')
    else:
        await bot.reply_to(message, 'Извините, я вас не понял?')

import asyncio
asyncio.run(bot.polling())