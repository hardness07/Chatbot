from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

bot = AsyncTeleBot('6339583214:AAEJZoonfPmU3CpUMH0WtuQfpRt0FPDOqfQ')

#создание меню кнопок
@bot.message_handler(commands=['help',  'start'])
async def send_hello(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'Здравствуйте, чем я могу помочь?', disable_notification=True, protect_content=True)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    oneb = 'Casino🎰'
    twob = 'Random🎲'
    threeb = 'Video🎥'
    fourb = 'Photo📷'
    markup.add(oneb, twob, threeb, fourb, row_width=2)
    await bot.send_message(chat_id, '✨Menu✨', reply_markup=markup)

@bot.message_handler(commands=['help',  'start'])
async def send_welcome(message):
    chat_id = message.from_user.id
    markup = InlineKeyboardMarkup()
    oneb = InlineKeyboardButton('Casino🎰', callback_data='first')
    twob = InlineKeyboardButton('Random🎲', callback_data='second')
    threeb = InlineKeyboardButton('Video🎥', callback_data='three')
    fourb = InlineKeyboardButton('Photo📷', callback_data='four')
    markup.add(oneb)
    markup.add(twob)
    markup.add(threeb)
    markup.add(fourb)
    await bot.send_message(chat_id, '✨Menu✨', reply_markup=markup)



#для рандомного числа на кубике
@bot.message_handler(commands=['cube',  'number'])
async def send_play(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_dice(chat_id, '🎲')
    print(bot_message.dice.value)

@bot.message_handler(commands=['slot', 'casino'])
async def send_casino(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_dice(chat_id, '🎰')
    print(bot_message.dice.value)

@bot.message_handler(commands=['ball', 'basketball'])
async def send_curry(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_dice(chat_id, '🏀')
    print(bot_message.dice.value)

@bot.message_handler(commands=['myach', 'football'])
async def send_messi(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_dice(chat_id, '⚽')
    print(bot_message.dice.value)

#отправка любого стикера
@bot.message_handler(commands=['sticker', 'fun'])
async def send_sticker(message):
    chat_id = message.from_user.id
    await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAIiSWSkDFYyOiDOzsfNOVJKnDGS3bOCAAIIBAAC4HlSB91E7iQQl6jGLwQ')

#отправка текстового документа
@bot.message_handler(commands=['text', 'document'])
async def send_doci(message):
    chat_id = message.from_user.id
    await bot.send_document(chat_id, open('text.txt', 'rb'))

#отправка местоположения
@bot.message_handler(commands=['location', 'position'])
async def send_gdeya(message):
    chat_id = message.from_user.id
    await bot.send_location(chat_id, 58.062197, 56.346386)

#отправка фото
@bot.message_handler(commands=['photo', 'mem'])
async def send_youtube(message):
    chat_id = message.from_user.id
    await bot.send_photo(chat_id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQK2xNQoZUf8q_66qmTAl1E6drKD9qhp7336RqNM1lTS39PhCJhDD2N75xsOXNsKT-hTCY&usqp=CAU', caption='чиназес')



@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    text_message = message.text
    text_message = text_message.lower()
    if 'дела' in text_message or 'настроение' in text_message:
        await bot.reply_to(message, 'Хорошо, а у тебя?')
    elif 'шутка' in text_message:
        await bot.reply_to(message, 'Колобок повесился')
    else:
        await bot.reply_to(message, 'Извините, я вас не понял?')









import asyncio
asyncio.run(bot.polling())


