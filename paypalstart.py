import io

import telebot
from telebot import types
import time

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

rules = types.InlineKeyboardMarkup()
rule = types.InlineKeyboardButton('Правила❕', callback_data='rules')
rules.add(rule)

submit_rules = types.InlineKeyboardMarkup()
submit = types.InlineKeyboardButton('Принять', callback_data='submited')
submit_rules.add(submit)

markup_send = types.InlineKeyboardMarkup()
submit = types.InlineKeyboardButton('Отправить', callback_data='send')
markup_send.add(submit)

markup_choice = types.InlineKeyboardMarkup()
submit = types.InlineKeyboardButton('✅', callback_data='submit')
reject = types.InlineKeyboardButton('🚫', callback_data='reject')
ban = types.InlineKeyboardButton('🐹❌', callback_data='ban')
markup_choice.add(submit, reject)
markup_choice.add(ban)

markup_chat = types.InlineKeyboardMarkup()
chat = types.InlineKeyboardButton('⚡Чат', url='https://t.me/joinchat/iXE6jISxRFg2OGQy')
channel = types.InlineKeyboardButton('💸Выплаты', url='https://t.me/joinchat/ZJWZj5mCEog4NmQy')
markup_chat.add(chat, channel)

markup_to_main = types.InlineKeyboardMarkup()
mark_to_main = types.InlineKeyboardButton('Материалы📩📚', callback_data='markup_to_main')
markup_to_main.add(mark_to_main)

markup_main = types.InlineKeyboardMarkup()
info = types.InlineKeyboardButton('👁Инфо', callback_data='info')
manuals = types.InlineKeyboardButton('🎓Мануалы', callback_data='manuals')
playground = types.InlineKeyboardButton('🛠Площадки', callback_data='playground')
markup_main.add(info)
markup_main.add(manuals)
markup_main.add(playground)

manual_markup = types.InlineKeyboardMarkup()
first = types.InlineKeyboardButton('📚Работа с PayPal | Vinted',
                                   url='https://telegra.ph/%F0%9D%90%8F%F0%9D%90%9A%F0%9D%90%B2%F0%9D%90%8F%F0%9D%90%9A%F0%9D%90%A5-%F0%9D%90%84%F0%9D%90%A6%F0%9D%90%A9%F0%9D%90%A2%F0%9D%90%AB%F0%9D%90%9E--Manual-10-07-01')
second = types.InlineKeyboardButton('📚Трек-код DNL',
                                    url='https://telegra.ph/%F0%9D%90%8F%F0%9D%90%9A%F0%9D%90%B2%F0%9D%90%8F%F0%9D%90%9A%F0%9D%90%A5-%F0%9D%90%84%F0%9D%90%A6%F0%9D%90%A9%F0%9D%90%A2%F0%9D%90%AB%F0%9D%90%9ETrek-kod-DNL-07-03')
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

delete_questions = types.InlineKeyboardMarkup()
delete = types.InlineKeyboardButton('Убрать🔚', callback_data='delete_question')
delete_questions.add(delete)

return_mark = types.InlineKeyboardMarkup()
ret = types.InlineKeyboardButton('Обратно', callback_data='return')
return_mark.add(ret)

proekt = """
♠️Добро пожаловать в♠️
      ⚡𝐏𝐚𝐲𝐏𝐚𝐥 𝐄𝐦𝐩𝐢𝐫𝐞⚡
  Товарка 1.0 без риска
    и номеров WhatsUp
    """
anketa = """
_❕ Если уверен что хочешь попасть
к нам - заполни анкету и ожидай
решения администрации, но сперва
ознакомься с правилами._
    """
Rules = """
*♠️Воркерам запрещается:♠️*   
• Реклама, флуд, спам, 18+ контент.
• Вводить участников чата в заблуждение.
• Предлагать свои услуги, без одобрения ТСа.
• Спорить с администрацией проекта.
• Раскрывать себя после профита мамонту
  _(Для избежания диспутов)_

_Незнание правил не освобождает вас от 
ответственности. За локи карт или кошельков 
ответсвенности не несем❕_

♠️*Права админов:*♠️
• Забанить воркера без объяснения причины.
• Штрафовать за диспуты.

_Нажимая "Принять" вы соглашаетесь с 
правилами и обязуетесь их придерживаться❕_
      """
request = """
♠️Вопросы:♠️
1. Как вы узнали о нашем проекте?
2. Работали ли вы раньше по 1.0? 
3. По каким странам раньше работали?
4. Сколько вы готовы работать в день?

_Ответьте на вопросы в таком порядке
одним сообщением c нумерацией❕_
    """
reject = """
_Сперва нужно ознакомиться с правилами❕_
    """
yes = """
_Ваша заявка была одобрена❕_
    """
no = """
_Ваша заявка была отклонена❕_
    """
adm = """
<i>Выберите действие!</i>
"""

ban = """_Ты был заблокирован❕_"""
admban = """_Пользователь был заблокирован❕_"""
information = """
⚡𝐏𝐚𝐲𝐏𝐚𝐥 𝐄𝐦𝐩𝐢𝐫𝐞⚡
-  _новый вид 1.0
    никакого фишинга
    официальный сайт❕_

-  _ориг счета PayPal
    профиты от 150€
    много площадок❕_
"""
links = """
⚡️PayPal Empire | <a href="https://t.me/joinchat/iXE6jISxRFg2OGQy">&#8204;Чат</a>⚡️"""

userStatus = [0]
userRequest = ['0']
chatID = ['1']
clearID = ['1']
bannedID = ['1']

del_msg1 = [0]
del_msg2 = [0]
del_msg3 = [0]
zayavka_id = [0]
foundedId = [True]
orig_text = ['Обновление...']

admin_id = [1695283624, 999503141]


@bot.message_handler(regexp='.msg')
def persona(message):
    if message.from_user.id in admin_id:
        orig_text1 = message.text.split(".msg ", maxsplit=1)[1]
        orig_text[0] = orig_text1


@bot.message_handler(regexp='.send')
def persona(message):
    count = 0
    if message.from_user.id in admin_id:
        with io.open("members_file.txt", encoding='utf-8') as file:
            try:
                for line in file:
                    bot.send_message(line, text=orig_text[0])
                    time.sleep(0.8)
                    count += 1
                    print(count)
            except Exception as e:
                bot.reply_to(message, e)
                pass
    bot.send_message(1695283624, text=count)


@bot.message_handler(regexp='@')
def persona(message):
    if message.from_user.id in admin_id:
        chatID[0] = message.text
        clearID[0] = (chatID[0]).replace('@', '')
        print(clearID[0])
        del_msg21 = bot.send_message(message.chat.id, '💠Админ: @{0}💠\n'
                                                      ' Хомяк: @'.format(message.from_user.username) + str(
            clearID[0]), reply_markup=markup_choice)
        del_msg2[0] = del_msg21.message_id


@bot.message_handler(commands=['start'])
def start(message):
    members_file = open("members_file.txt", "a+")
    new_id = str(message.from_user.id)
    founded = True

    with io.open("members_file.txt", encoding='utf-8') as file:
        for line in file:
            if new_id in line:
                founded = False
                print('Id already exist')

    if founded == True:
        userStatus[0] = 0
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECkYFg7Ipe-gQNNfuvCkRpNnywDvL8cQACsAwAAtXO2EkYBH8D8PsM3yAE')
        bot.send_message(message.chat.id, proekt, parse_mode="Markdown")
        time.sleep(0.5)
        bot.send_message(message.chat.id, anketa, parse_mode="Markdown", reply_markup=rules)
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECkYFg7Ipe-gQNNfuvCkRpNnywDvL8cQACsAwAAtXO2EkYBH8D8PsM3yAE',
                         reply_markup=markup_chat)
        bot.send_message(message.chat.id, text=adm,  parse_mode='html',
                                                          reply_markup=markup_to_main)

    if message.from_user.id == bannedID[0]:
        bot.send_message(bannedID, ban, parse_mode="Markdown")


@bot.message_handler(func=lambda message: True)
def message_react(message):
    members_file = open("members_file.txt", "a+")
    new_id = str(message.from_user.id)
    founded = True

    with io.open('members_file.txt', encoding='utf-8') as file:
        for line in file:
            if new_id in line:
                founded = False
                print('Id already exist')
    members_file.close()

    if founded == False:
        bot.send_message(message.chat.id, text='Ваш запрос не понятен!')

    elif message.from_user.id == bannedID[0]:
        bot.send_message(bannedID, ban, parse_mode="Markdown")

    elif userStatus[0] == 0:
        bot.send_message(message.chat.id, reject, parse_mode="Markdown")

    elif userStatus[0] == 1:
        userRequest[0] = message.text
        for admin in admin_id:
            bot.send_message(admin, '🐹Новая заявка!🐹\n👁Профиль: @{0}\n'
                                         '💷Id: @{1}\n'.format(message.from_user.username,
                                                               str(message.from_user.id)) + userRequest[0])

        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

        bot.send_message(message.chat.id, '📩Ваша заявка готова!📩\n'
                         + userRequest[0], reply_markup=markup_send)


@bot.callback_query_handler(func=lambda call: call.data == 'submit')
def submit(call):
    members_file = open("members_file.txt", "a+")
    members_file.write("\n" + str(clearID[0]))
    members_file.close()

    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    bot.send_message(1695283624, 'ТС принял: @' + clearID[0])
    time.sleep(0.5)
    bot.send_sticker(clearID[0], 'CAACAgIAAxkBAAEClNdg8A9CZ34tw5Kq8FN-7k19HCXXyQACSg8AAmCm0EndM-7edjWcqyAE',
                     reply_markup=markup_chat)
    bot.send_message(clearID[0], '<i>Мануалы доступны в чате, если вы хотите открыть их здесь - нажмите /start!</i>',
                     parse_mode="html")


@bot.callback_query_handler(func=lambda call: True)
def caller(call):
    if call.data == 'rules':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=Rules,
                              parse_mode="Markdown", reply_markup=submit_rules)
    elif call.data == 'ban':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bannedID[0] = int(clearID[0])
        bot.send_message(bannedID[0], ban, parse_mode="Markdown")
        bot.send_message(1695283624, admban, parse_mode="Markdown")
    elif call.data == 'submited':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                             text=request, parse_mode="Markdown", reply_markup=delete_questions)
        userStatus[0] = 1
    elif call.data == 'delete_question':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == 'send':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        time.sleep(0.6)
    elif call.data == 'manuals':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🎓Наши мануалы:🎓\n', reply_markup=manual_markup)
    elif call.data == 'playground':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='🛠Площадки для работы:🛠\n', reply_markup=return_markup)
    if call.data == 'info':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=information, parse_mode="Markdown", reply_markup=return_mark)
    elif call.data == 'return':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='👁Вы: @{0}\n'
                                   '💼Id: {1}'.format(call.from_user.username,
                                                      str(call.from_user.id)),
                              reply_markup=markup_main)
    elif call.data == 'reject':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(1695283624, 'ТС отрек: @' + clearID[0])
        bot.send_sticker(clearID[0], 'CAACAgIAAxkBAAECkj5g7Zfv76aC1XHirWy-5CnvgJdObgAC0QwAAqL7YUoHET8XRM4bwiAE')
        time.sleep(0.6)
        bot.send_message(clearID[0], no, parse_mode="Markdown")
    elif call.data == 'markup_to_main':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='👁Вы: @{0}\n'
                                   '💼Id: {1}'.format(call.from_user.username, str(call.from_user.id)),
                              reply_markup=markup_main)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
