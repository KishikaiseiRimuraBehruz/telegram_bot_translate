# Обработка текста сообщения, если ввод на русском, то перевод на английский,
# если другой язык, то перевод на русский.
# Импорт библиотек
import database
import keyboard
import telebot
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardRemove, InlineQuery,InputTextMessageContent
from googletrans import Translator
# Апи бота
bot = telebot.TeleBot("6099974918:AAFY3ANcTs2YbiJMRkCiaVdqJQBZJKbCULU")

# Обработка команды /start приветствие.
@bot.message_handler(commands=['start'])
def start_message(message):
    # получить телеграм айди
    user_id = message.from_user.id


    print(user_id)


    #проверка ползователя
    checker = database.check_user(user_id)

    # если пользователь есть в базе
    if checker:


        # отправим сообщение и меню
        bot.send_message(user_id, f'Привет {message.from_user.first_name},я бот переводчик языков\n больше '
                                  f'50 языков мира если хотите '
                                  f'проверить или просто переводить '
                                  f'\n Тогда WELCOME MY BRO!',reply_markup=ReplyKeyboardRemove())
        bot.send_message(user_id,f'И так вот то что сейчас могу перевести'
                                 f'\n выбери язык {message.from_user.first_name} '
                                 f'\nи я буду переводить на этот язык',reply_markup=keyboard.main_menu_kb())


    # если нет пользователя в базе
    elif not checker:


        # отправим сообшение попросим что бы ползователь отправил свое имя
        bot.send_message(user_id, 'Привет\nотправь свое имя БУДУ РАД)')


        # переход на этап получения имени
        bot.register_next_step_handler(message, get_name)


# Этап получения имени
def get_name(message):
    # получить телеграм айди
    user_id = message.from_user.id


    # Сохраним имя в переменную
    username = message.text


    # Отправим ответ
    bot.send_message(user_id,
                     'Отправьте теперь свой номер телефона',
                     reply_markup=keyboard.phone_number_kb())


    # переход на этап получения номера телефона
    bot.register_next_step_handler(message, get_number, username)


def get_number(message, name):
    # Сохраним телеграмм айди в переменную
    user_id = message.from_user.id

    # проверяем отправил ли пользователь контакт
    if message.contact:
        # Сохраним контакт
        phone_number = message.contact.phone_number

        # сохраняем его в базе
        database.register_user(user_id, name, phone_number)
        bot.send_message(user_id, 'Вы успешно зарегистрированы', reply_markup=ReplyKeyboardRemove())

        # И открываем меню
        bot.send_message(user_id,
                         'Выберите пункт меню',
                         reply_markup=keyboard.main_menu_kb())

        # А если не отправил контакт то еще раз попросим отправить
    elif not message.contact:
        bot.send_message(user_id,
                         'отправьте контакт используя кнопку',
                         reply_markup=keyboard.phone_number_kb())

        # Обратно на этап получения номера телефона
        bot.register_next_step_handler(message, get_number, name)

    # А если не отправил контакт то еще раз попросим отправить

    # await bot.reply_to(message,'------\n'
    #              + 'Здравствуй, '
    #              + message.from_user.first_name
    #              + ' \nПереведу с русского на английский \nИ с других языков на русский '
    #              +'\n------')


# Обработка команды /help.
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,'---------\n'
        'Просто вводи текст и нажимай отправить\n'
        'Я сам определю какой это язык\n'
        'У меня есть кнопки для того что бы переводить\nопределенный язык'
        'Если не перевел, попробуй еще раз\n'
        'Перевод гугл'
        'Ну как сказал я крутым видом)'
        '\n------')


    # await bot.reply_to(message,'------\n'
    #              + 'Просто вводи текст и нажимай отправить\n'
    #              + 'Я сам определю какой это язык\n'
    #              + 'Если не перевел, попробуй еще раз\n'
    #              + 'Перевод гугл'
    #              +'\n------')
@bot.message_handler()
def translate_ru_user(message):
    # сохроняем в переменую chat.id
    user_id = message.from_user.id
    user_answer = message.text
    # # сохроняем в переменую message.id
    message_id = message.message_id
    # print(message_id)

    # сохроняем в переменную переводчик
    translator = Translator()

    # Определение языка ввода.
    lang = translator.detect(message.text)
    lang = lang.lang

    if lang == 'ru':
        # сохроням в переменную с переводом что написал ползователь
        send = translator.translate(message.text)
        bot.reply_to(message, send.text)
        # Иначе другой язык перевести на русский {dest='ru'}.
    else:
        send = translator.translate(message.text, dest='ru')
        bot.reply_to(message,send.text)
        bot.register_next_step_handler(message, translate_ru_user)
@bot.message_handler()
def translate_en_user(message):
    # сохроняем в переменую chat.id
    user_id = message.from_user.id
    user_answer = message.text
    # # сохроняем в переменую message.id
    message_id = message.message_id
    # print(message_id)

    # сохроняем в переменную переводчик
    translator = Translator()

    # Определение языка ввода.
    lang = translator.detect(message.text)
    lang = lang.lang

    if lang == 'ru':
        # сохроням в переменную с переводом что написал ползователь
        send = translator.translate(message.text)
        bot.reply_to(message, send.text)
        # Иначе другой язык перевести на русский {dest='ru'}.
    else:
        send = translator.translate(message.text, dest='en')
        bot.reply_to(message,send.text)
        bot.register_next_step_handler(message, translate_en_user)

@bot.message_handler()
def translate_ja_user(message):
    # сохроняем в переменую chat.id
    user_id = message.from_user.id
    user_answer = message.text
    # # сохроняем в переменую message.id
    message_id = message.message_id
    # print(message_id)

    # сохроняем в переменную переводчик
    translator = Translator()

    # Определение языка ввода.
    lang = translator.detect(message.text)
    lang = lang.lang
    if lang == 'ja':
        # сохроням в переменную с переводом что написал ползователь
        send = translator.translate(message.text, dest='ja')
        bot.send_message(message, send.text)
    # Иначе другой язык перевести на русский {dest='ru'}.
    else:
        send = translator.translate(message.text, dest='ja')
        bot.reply_to(message, send.text)
        bot.register_next_step_handler(message, translate_ja_user)
@bot.message_handler()
def translate_it_user(message):
    # сохроняем в переменую chat.id
    user_id = message.from_user.id
    user_answer = message.text
    # # сохроняем в переменую message.id
    message_id = message.message_id
    # print(message_id)

    # сохроняем в переменную переводчик
    translator = Translator()

    # Определение языка ввода.
    lang = translator.detect(message.text)
    lang = lang.lang
    if lang == 'it':
        # сохроням в переменную с переводом что написал ползователь
        send = translator.translate(message.text)
        bot.send_message(message, send.text)
    # Иначе другой язык перевести на русский {dest='ru'}.
    else:
        send = translator.translate(message.text, dest='it')
        bot.reply_to(message, send.text)
        bot.register_next_step_handler(message, translate_it_user)
@bot.message_handler()
def translate_de_user(message):
    # сохроняем в переменую chat.id
    user_id = message.from_user.id
    user_answer = message.text
    # # сохроняем в переменую message.id
    message_id = message.message_id
    # print(message_id)

    # сохроняем в переменную переводчик
    translator = Translator()

    # Определение языка ввода.
    lang = translator.detect(message.text)
    lang = lang.lang
    if lang == 'de':
        # сохроням в переменную с переводом что написал ползователь
        send = translator.translate(message.text)
        bot.send_message(message, send.text)
    # Иначе другой язык перевести на русский {dest='ru'}.
        send = translator.translate(message.text, dest='de')
        bot.reply_to(message, send.text)
        bot.register_next_step_handler(message, translate_de_user)

# оброботчик кнопок (ru,en,ja,it,de)
@bot.callback_query_handler(lambda call: call.data in ['ru','en','ja','it','de'])
def main_menu_hendler(call):
    # сохроняем в переменую chat.id
    user_id = call.message.from_user.id
    user_answer = call.message.text
    # сохроняем в переменую message.id
    message_id = call.message.message_id

    # сохроняем в переменную переводчик
    translator = Translator()

     # Определение языка ввода.
    langs = translator.detect(call.message.text)
    lang = langs.lang


    if call.data == 'ru':
        bot.send_message(call.from_user.id, f'Теперь {call.message.from_user.first_name} я буду перевести с '
                                  f'осталных языков\n в английский', reply_markup=ReplyKeyboardRemove())

        bot.register_next_step_handler(call.message,translate_ru_user)
    elif call.data =='en':
        bot.send_message(call.from_user.id, f'Теперь {call.message.from_user.first_name} я буду перевести с '
                                      f'осталных языков\n в английский', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(call.message, translate_en_user)
###########################################
    elif call.data == 'ja':
        bot.send_message(call.from_user.id, f'Теперь {call.message.from_user.first_name} я буду перевести с '
                                       f'осталных языков\n в Japanse', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(call.message, translate_ja_user)
###################################################
    elif call.data == 'it':
        bot.send_message(call.from_user.id, f'Теперь {call.message.from_user.first_name} я буду перевести с '
                                       f'осталных языков\n в Italian', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(call.message, translate_it_user)
####################################################
    elif call.data == 'de':
        bot.send_message(call.from_user.id, f'Теперь {call.message.from_user.first_name} я буду перевести с '
                                           f'осталных языков\n в German', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(call.message, translate_de_user)
    else:
         pass


# Обработка текста сообщения, если ввод на русском, то перевод на английский,
# если другой язык, то перевод на русский.
# @bot.message_handler()
# async def user_text(message):
#     translator = Translator()
#
#     # Определение языка ввода.
#     lang = translator.detect(message.text)
#     lang = lang.lang
#
#     # Если ввод по русски, то перевести на английский по умолчанию.
#     # Если нужен другой язык, измени <message.text> на <message.text, dest='нужный язык'>.
#     if lang == 'ru':
#         send = translator.translate(message.text)
#         await bot.reply_to(message, '------\n'+ send.text +'\n------')
#
#     # Иначе другой язык перевести на русский {dest='ru'}.
#     else:
#         send = translator.translate(message.text, dest='ru')
#         await bot.reply_to(message, '------\n'+ send.text +'\n------')

# Обработка картинок с подписями
@bot.message_handler(content_types=['photo'])
def handle_image(message):
    translator = Translator()
    #Обработчик сообщений с изображениями
    chat_id = message.chat.id
    photo = message.photo[-1].file_id
    caption = message.caption

    # Определение языка ввода.
    lang = translator.detect(caption)
    lang = lang.lang

    # Если подпись по русски, то перевести на английский по умолчанию.
    if lang == 'ru':
        send = translator.translate(caption)

    # Иначе другой язык перевести на русский {dest='ru'}.
    else:
        send = translator.translate(caption, dest='ja')
        bot.send_photo(chat_id, photo, caption=send.text)

# Обработка инлайн запросов. Инлайн режим необходимо включить в настройках бота у @BotFather.
@bot.inline_handler(lambda query: True)
def inline_query(query):
    results = []
    translator = Translator()
    text = query.query.strip()

    # Если запрос пустой, не делаем перевод
    if not text:
        return

    # Определение языка ввода.
    lang = translator.detect(text)
    lang = lang.lang

    # Если ввод по русски, то перевести на английский по умолчанию.
    if lang == 'ru':
        send = translator.translate(text)
        results.append(types.InlineQueryResultArticle(
            id='1', title=send.text, input_message_content=types.InputTextMessageContent(
                message_text=send.text)))

    # Иначе другой язык перевести на русский {dest='ru'}.
    else:
        send = translator.translate(text, dest='ru')
        results.append(types.InlineQueryResultArticle(
            id='1', title=send.text, input_message_content=types.InputTextMessageContent(
                message_text=send.text)))

    bot.answer_inline_query(query.id, results)

#Запуск и повторение запуска при сбое.
bot.polling()