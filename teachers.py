import telebot
from bottoken import bot


def start_admin(message):
    bot.register_next_step_handler(keyboard_admin(message), menu)


def keyboard_admin(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add("Журнал", "Добавить ДЗ", "Посмотреть рейтинги", "")
    return bot.send_message(message.chat.id, "Выберете действие", reply_markup=keyboard)


def menu(message):
    if message.text == "Журнал":
        pass
    if message.text == "Добавить ДЗ":
        pass
    if message.text == "Посмотреть рейтинги":
        pass
    if message.text == "":
        pass
    start_admin(message)
