import sqlite3


from datetime import datetime


#Создаем подключение
connection = sqlite3.connect('translate.db')


# переводчик на Sqlite3
sql = connection.cursor()


# запрос на создание таблицы (ползователи которые использует
# языки , языки которые знают ползователи )


# создаем таблицу для список ползоватей
sql.execute('CREATE TABLE IF NOT EXISTS users (tg_id INTEGER, name TEXT,'
            'phone_number TEXT, reg_date DATETIME);')


# создаем таблицу для языков
sql.execute('CREATE TABLE IF NOT EXISTS languages (language TEXT);')


# создаем таблицу для языки которые знают ползователи
sql.execute('CREATE TABLE IF NOT EXISTS userlanguages (name TEXT, language);')


# Функции регистрациия ползователя
def register_user(tg_id, name, phone_number):
    # создаем подключение
    connection = sqlite3.connect('translate.db')


    # переводчик на Sqlite3
    sql = connection.cursor()


    # Добовление в базу ползователя
    sql.execute('INSERT INTO users '
                '(tg_id, name, phone_number, reg_date) VALUES'
                '(?, ?, ?, ?);',(tg_id, name, phone_number, datetime.now()))


    # Записать обновления
    connection.commit()


# проверям если ползовател с таким айди
def check_user(user_id):
    # создаем подключение
    connection = sqlite3.connect('translate.db')


    # переводчик на Sqlite3
    sql = connection.cursor()


    # берем с базы телеграм айди
    checker = sql.execute('SELECT tg_id FROM users WHERE tg_id=?;', (user_id, ))


    if checker.fetchone():
        return True


    else:
        return False


# добавить язык в таблицу языков
def add_languages(language):
    # создаем подключение
    connection = sqlite3.connect('translate.db')


    # переводчик на Sqlite3
    sql = connection.cursor()


    # добовляем язык в таблицу языки там main.py мы зделаем что только адмие добовлял
    sql.execute('INSERT INTO languages '
                '(language)'
                'VALUES (?);',
                (language))


    # записать обновление
    connection.commit()


# удалить язык с таблици языков
def delete_languag_from_Languages():
    # создаем подключение
    connection = sqlite3.connect('translate.db')


    # переводчик на Sqlite3
    sql = connection.cursor()


    # удалям все что было написона в таблицу languages
    sql.execute('DELETE FROM languages')


    # записать обновление
    connection.commit()


# удалить определеный  язык с таблици языков
def delete_languag_from(language):
    # создаем подключение
    connection = sqlite3.connect('translate.db')


    # переводчик на Sqlite3
    sql = connection.cursor()


    # удалям все что было написона в таблицу languages
    sql.execute('DELETE FROM languages WHERE language=?;',(language))


    # записать обновление
    connection.commit()


# Получить номер телефона и имя ползователя
def get_user_number_name(user_id):
    # создаем подключение
    connection = sqlite3.connect('translate.db')


    # переводчик на Sqlite3
    sql = connection.cursor()


    # получаем номер и имя ползователя
    exact_user = sql.execute('SELECT name, phone_number From users WHERE tg_id=?;',(user_id, ))


    # записать обновление
    connection.commit()


    # сохроням
    return exact_user.fetchall()








