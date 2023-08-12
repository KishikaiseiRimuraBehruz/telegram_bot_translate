import language
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def main_menu_kb():
    # a = 0
    # keyss = []
    # for i, j in language.LANGDICT.items():
    #     key = InlineKeyboardButton()

    # Создаем пространство для кнопок
    kb = InlineKeyboardMarkup(row_width=2)


    #Создаем пространство (несгараемые)кнопки
    ru = InlineKeyboardButton(text='Русский', callback_data='ru')
    en = InlineKeyboardButton(text='English', callback_data='en')
    ja = InlineKeyboardButton(text='Japanse', callback_data='ja')
    it = InlineKeyboardButton(text='Italian', callback_data='it')
    de = InlineKeyboardButton(text='German', callback_data='de')


    # Обединить пространство с кнопками

    kb.add(ru,en,ja,it,de)


    return kb

def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)


    number = KeyboardButton('Поделиться контактом', request_contact=True)


    kb.add(number)


    return kb
