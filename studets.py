import telebot
from bottoken import bot
import database


new_students = {}


def start_user(message):
    bot.register_next_step_handler(keyboard_user(message), menu)


def keyboard_user(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add("Записаться на курс", "Посмотреть рейтинг", "Получит ДЗ", "Дополнительная литература")
    return bot.send_message(message.chat.id, "Выберете действие", reply_markup=keyboard)


def menu(message):
    if message.text == "Записаться на курс":
        sign_to_course(message)
    if message.text == "Полсмотреть рейтинг":
        get_rating(message)
    if message.text == "Получить ДЗ":
        get_homework(message)
    if message.text == "Дополнительная литература":
        get_literature(message)


def sign_on_course(message):
    bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите Фамилию"), get_surname)


def get_surname(message):
    l = []
    l.append(message.text)
    new_students.update({message.chat.id: l})
    bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите имя"), get_name)


def get_name(message):
    l = new_students.get(message.chat.id)
    l.append(message.text)
    new_students.update({message.chat.id: l})
    bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите очество"), get_patronymic)


def get_patronymic(message):
    l = new_students.get(message.chat.id)
    l.append(message.text)
    new_students.update({message.chat.id: l})
    bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите номер зачетки"), get_record_book)


def get_record_book(message):
    l = new_students.get(message.chat.id)
    l.append(message.text)
    l.append(0)
    l.reverse()
    l.append(str(message.chat.id))
    l.reverse()
    database.sign_on_course(tuple(l))
    new_students.pop(message.chat.id)
    database.show_table('Students')
    start_user(message)


def get_rating(message):
    pass


def get_homework(message):
    pass


def get_literature(message):
    pass