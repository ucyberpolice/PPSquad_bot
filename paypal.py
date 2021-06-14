import telebot
from telebot import types
import time

TOKEN = '1877566254:AAFxQmIGck18VDl2QTsz67QymTkIm1UCDQs'
bot = telebot.TeleBot(TOKEN)

idStatus = [
    'false',
    'true'
]
user_answers = [
    '0'
]
usersINFO = [
    'username',
    'id'
]
toolID = [
    'id',
    'answer'
]
usersID = [
    'id'
]
soCreatersID = [
    'first'
]

bannedId = ['1']
clearBannedId = ['1']
TwoclearBannedId = ['1']
ThreeclearBannedId = ['1']
FourlearBannedId = ['1']

Acces = False

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
channel = types.InlineKeyboardButton('💸Канал выплат💸', url='https://t.me/joinchat/ZJWZj5mCEog4NmQy')
markup_chat.add(chat)
markup_chat.add(channel)

markup_main = types.InlineKeyboardMarkup()
info = types.InlineKeyboardButton('👁Инфо', callback_data='info')
manuals = types.InlineKeyboardButton('🎓Мануалы', callback_data='manuals')
playground = types.InlineKeyboardButton('🛠Площадки', callback_data='playground')
markup_main.add(info)
markup_main.add(manuals)
markup_main.add(playground)

manual_markup = types.InlineKeyboardMarkup()
first = types.InlineKeyboardButton('📚Работа с PayPal | Vinted', url='https://telegra.ph/Status-proekta---VORK-06-05')
second = types.InlineKeyboardButton('📚Какой товар выставлять?', url='https://telegra.ph/Kakoj-tovar-vystavlyat-06-05')
third = types.InlineKeyboardButton('Обратно', callback_data='return')
manual_markup.add(first)
manual_markup.add(second)
manual_markup.add(third)

return_markup = types.InlineKeyboardMarkup()
vinted = types.InlineKeyboardButton('Vinted.com|👗одежда', url='https://www.vinted.com/')
quoka = types.InlineKeyboardButton('Quoka.de|🧢любой стафф', url='https://www.quoka.de/')
finn = types.InlineKeyboardButton('Finn.no|👟любой стафф', url='https://www.finn.no/-')
return1 = types.InlineKeyboardButton('Обратно', callback_data='return')
return_markup.add(vinted)
return_markup.add(quoka)
return_markup.add(finn)
return_markup.add(return1)

return_mark = types.InlineKeyboardMarkup()
ret = types.InlineKeyboardButton('Обратно', callback_data='return')
return_mark.add(ret)

@bot.message_handler(regexp='@')
def persona(message):
    if message.from_user.id == 1892827220:
        bannedId[0] = message.text
        clearBannedId[0] = bannedId[0].replace('@','')
        print(bannedId[0])
        bot.send_message(message.from_user.id, 'Пользователь забанен!✅')

@bot.message_handler(regexp='#')
def persona(message):
    if message.from_user.id == 1892827220:
        bannedId[0] = message.text
        TwoclearBannedId[0] = bannedId[0].replace('#','')
        bot.send_message(message.from_user.id, 'Пользователь забанен!✅')

@bot.message_handler(regexp='%')
def persona(message):
    if message.from_user.id == 1892827220:
        bannedId[0] = message.text
        FourlearBannedId[0] = bannedId[0].replace('%','')
        bot.send_message(message.from_user.id, 'Пользователь забанен!✅')

@bot.message_handler(regexp='!')
def persona(message):
    if message.from_user.id == 1892827220:
        bannedId[0] = message.text
        ThreeclearBannedId[0] = bannedId[0].replace('!','')
        bot.send_message(message.from_user.id, 'Пользователь забанен!✅')


@bot.message_handler(commands=['start'])
def commands(message):
    if message.from_user.id == int(clearBannedId[0]):
        bot.send_message(message.chat.id, text='Ты заблокирован!')
    elif message.from_user.id == int(TwoclearBannedId[0]):
        bot.send_message(message.chat.id, text='Ты заблокирован!')
    elif message.from_user.id == int(ThreeclearBannedId[0]):
        bot.send_message(message.chat.id, text='Ты заблокирован!')
    elif message.from_user.id == int(FourlearBannedId[0]):
        bot.send_message(message.chat.id, text='Ты заблокирован!')

    else:
        idStatus[0] = '0'
        bot.send_message(message.chat.id, 'Правила проекта ⚡𝐏𝐚𝐲𝐏𝐚𝐥 𝐒𝐪𝐮𝐚𝐝⚡: \n'
                                          '\n'
                                          '• Запрещена реклама, спам, флуд, распространение 🔞 фото, видео, гиф, контента.\n'
                                          '• Запрещено попрошайничество!\n'
                                          '• Запрещены услуги вбивов, обналов и прочих услуг.\n'
                                          '• Админы могут дать бан воркеру без объяснения причины!\n'
                                          '• После профита категорически запрещается выдавать себя мамонту во избежание диспутов, если это произошло админы могут штрафовать и не выплачивать профиты!'
                                          '\n'
                                          '\n'
                                          '❗️ Незнание правил не освобождает вас от ответственности. '
                                          'Выплата от суммы профита. За локи кошельков/карт ответственности не несем\n'
                                          '\n'
                                          'Нажимая кнопку принять - вы подтверждаете прочтение этих правил.\n',
                         reply_markup=markup_inline_choice)

@bot.message_handler(func=lambda message: True)
def message_react(message):
    user_answers[0] = message.text
    if idStatus[0] == '0':
        bot.send_message(message.chat.id, 'Произошла ошибка, для начала необходимо принять соглашение.')

    elif idStatus[0] == '1':
        bot.send_message(message.chat.id, '🍀Ваша заявка готова!🍀\n'
                         + user_answers[0] + '\n'
                                             'Нажмите отправить, если все верно.\n', reply_markup=markup_send)

        bot.send_message(1892827220, '🔔Новая заявка!🔔\nПрофиль: @{0}\n'
                                     'ID: @{1}\n'.format(message.from_user.username,
                                                         str(message.from_user.id)) + user_answers[0],
                         reply_markup=markup_submit)
        usersINFO[0] = message.from_user.username
        usersINFO[1] = message.from_user.id


@bot.callback_query_handler(func=lambda call: True)
def handler(call):
    if call.data == 'agree':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='⚡Вы ознакомились с правилами!⚡\nПерейдем к вашей заявке,'
                                   ' вам нужно ответить на несколько вопросов.',
                              reply_markup=None)
        time.sleep(0.5)
        bot.send_message(call.message.chat.id, 'Отвечайте на вопросы в таком порядке одним сообщением:\n'
                                               '🍀1. Как вы узнали о нашем проекте?\n'
                                               '🍀2. Работали ли вы раньше по 1.0? \n'
                                               '🍀3. По каким странам Европы раньше работали?\n'
                                               '🍀4. Сколько вы готовы уделять времени работе в день?')
        idStatus[0] = '1'

    elif call.data == 'send':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Ваша заявка была успешно отправлена!✅',
                              reply_markup=None)
        idStatus[0] = '3'


    elif call.data == 'submit':
        bot.send_message(usersINFO[1], '✅Ваша заявка одобрена!✅ \n'
                                       'Присоединитесь в наш чат:\n', reply_markup=markup_chat)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🍀Заявка одобрена!🍀\n'
                                   'Профиль: @' + usersINFO[0] + '\n'
                                                                 'Id: @' + str(usersINFO[1]) + '\n', reply_markup=None)

        bot.send_message(usersINFO[1], 'Выберите действие:', reply_markup=markup_main)

    elif call.data == 'reject':
        bot.send_message(usersINFO[1], '🚫Ваша заявка была отклонена!🚫')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🚫Заявка отклонена!🚫\n'
                                   'Профиль: @' + str(usersINFO[0]) + '\n'
                                                                      'Id: @' + str(usersINFO[1]) + '\n', reply_markup=None)

    elif call.data == 'return':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберите действие:', reply_markup=markup_main)

    elif call.data == 'manuals':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🎓Мануалы:🎓\n', reply_markup=manual_markup)

    elif call.data == 'playground':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🛠Площадки для работы:🛠\n', reply_markup=return_markup)

    elif call.data == 'info':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🍀Минималка через "перевод как другу"-80€\n'
                                   '🔥Минималка через "защиту покупателя"-200€🎯\n'
                                   '\n'
                                   'Перевод как другу-ЧЕРЕЗ 3 ДНЯ ВЫВОД‼️\n'
                                   'Перевод через защиту покупателя-\n'
                                   'ЧЕРЕЗ 21 ДЕНЬ ВЫВОД‼️\n'
                                   'Штраф за диспуты‼️\n'
                                   '\n'
                                   'За лок палок ответственность не несем‼\n'
                                   '💳💰Выплата на карту или киви.', reply_markup=return_mark)

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
