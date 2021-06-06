import requests
import telebot
from telebot import types
import re
import time

TOKEN = '1877566254:AAFxQmIGck18VDl2QTsz67QymTkIm1UCDQs'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
bot = telebot.TeleBot(TOKEN)

idStatus = [
    'false', #0
    'true'   #1
]
user_answers = [
    '1',
    '2',
    'Много',
]
usersINFO = [
    'username',
    'id'
]

toolID = [
    'id',
    'answer'
]
soCreatersID = [
    'first',
]

markup_inline_choice = types.InlineKeyboardMarkup()
agree = types.InlineKeyboardButton('Принять✅', callback_data='agree')
markup_inline_choice.add(agree)

markup_send = types.InlineKeyboardMarkup()
send = types.InlineKeyboardButton('Отправить✅', callback_data='send')
markup_send.add(send)

markup_submit = types.InlineKeyboardMarkup()
submit = types.InlineKeyboardButton('Одобрить✅', callback_data='submit')
reject = types.InlineKeyboardButton('Отказать🚫', callback_data='reject')
markup_submit.add(submit, reject)

markup_chat = types.InlineKeyboardMarkup()
chat = types.InlineKeyboardButton('⚡𝐏𝐚𝐲𝐏𝐚𝐥 𝐒𝐪𝐮𝐚𝐝⚡ | Чат', url='https://t.me/joinchat/WOy2oyuK9fZmODZi')
markup_chat.add(chat)


@bot.message_handler(commands=['start'])
def commands(message):
    bot.send_message(message.chat.id, 'Правила проекта ⚡𝐏𝐚𝐲𝐏𝐚𝐥 𝐒𝐪𝐮𝐚𝐝⚡: \n'
                                      '\n'
                                      '• Запрещена реклама, спам, флуд, распространение 🔞 фото, видео, гиф, контента.\n'
                                      '• Запрещено попрошайничество\n'
                                      '• Запрещены услуги вбивов, обналов и прочих услуг.\n'
                                      '\n'
                                      '❗️ Незнание правил не освобождает вас от ответственности. '
                                      'Выплата от суммы профита. За локи кошельков/карт ответственности не несем\n'
                                      '\n'
                                      'Нажимая кнопку принять - вы подтверждаете прочтение этих правил.\n', reply_markup=markup_inline_choice)
    idStatus[0] = '0'

@bot.message_handler(commands=['tool'])
def tool(message):
    if message.from_user.first_name == '97':
        bot.send_message(toolID[0], toolID[1])

@bot.message_handler(regexp='✍🏻')
def personalId(message):
    if message.from_user.first_name == '97':
        toolID[1] = message.text
        print(toolID[1])
        bot.send_message(message.from_user.id, 'Done.')

@bot.message_handler(regexp='id:')
def personalId(message):
    if message.from_user.first_name == '97':
        usersID[0] = message.text
        toolID[0] = re.findall("\d+", usersID[0])[0]
        print(toolID[0])
        bot.send_message(message.from_user.id, 'Done.')

@bot.callback_query_handler(func=lambda call:True)
def answer_for_question(call):
    if call.data == 'agree':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='⚡Вы ознакомились с правилами!⚡\nПерейдем к вашей заявке, вам нужно ответить на несколько вопросов.',
                              reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.message.chat.id, '🍀Как вы узнали о нашем проекте?')
        idStatus[0] = '1'

    elif call.data == 'send':
        bot.send_message(707614495, 'Новая заявка!\n'
                                    'Профиль: @'+usersINFO[0]+'\n'
                                    'Id: @'+usersINFO[1]+'\n'
                                    '1. '+ user_answers[0] +'\n'
                                    '2. '+ user_answers[1] +'\n'
                                    '3. '+ user_answers[2] +'\n', reply_markup=markup_submit)
        bot.send_message(999503141, 'Новая заявка!\n'
                                    'Профиль: @' + usersINFO[0] + '\n'
                                     'Id: @' + usersINFO[1] + '\n'
                                     '1. ' + user_answers[0] + '\n'
                                     '2. ' + user_answers[1] + '\n'
                                     '3. ' + user_answers[2] + '\n', reply_markup=markup_submit)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ваша заявка была успешно отправлена!', reply_markup=None)

    elif call.data == 'submit':
        bot.send_message(usersINFO[1], '✅Ваша заявка одобрена!✅ \n'
                                               'Дополнительная инфомация по кнопкам ниже.\n'
                                       'Дорабатывается⚙⚒', reply_markup=markup_chat)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🍀Заявка одобрена!🍀\n'
                                   'Профиль: @'+usersINFO[0]+'\n'
                                    'Id: @'+usersINFO[1]+'\n', reply_markup=None)

    elif call.data == 'reject':
        bot.send_message(usersINFO[1], '🚫Ваша заявка была отклонена!🚫')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🍀Заявка отклонена!🍀\n'
                                   'Профиль: @'+usersINFO[0]+'\n'
                                    'Id: @'+usersINFO[1]+'\n', reply_markup=None)

@bot.message_handler(func=lambda message: True)
def message_react(message):
    if idStatus[0] == '0':
        bot.send_message(message.chat.id, 'Произошла ошибка, для начала необходимо принять соглашение.')

    elif idStatus[0] == '1':
        bot.send_message(message.chat.id, '🍀Работали ли вы раньше по 1.0? \n'
                                          'Если да, то какой у вас опыт?')
        user_answers[0] = message.text

        idStatus[0] = '2'
        usersINFO[0] = message.from_user.username
        usersINFO[1] = str(message.from_user.id)

    elif idStatus[0] == '2':
        bot.send_message(message.chat.id, '🍀Сколько вы готовы уделять времени работе в день?')

        user_answers[1] = message.text

        idStatus[0] = '3'

    elif idStatus[0] == '3':
        user_answers[2] = message.text
        bot.send_message(message.chat.id, '🍀Ваша заявка готова!🍀\n Нажмите отправить, если все верно. \n'                                    
                                          '1. '+ user_answers[0] + '\n'                                         
                                          '2. '+ user_answers[1] + '\n'                                          
                                          '3. '+ user_answers[2] + '\n'
                                          ,reply_markup=markup_send)
        user_answers[2] = message.text
        idStatus[0] = '4'

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)