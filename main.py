import telebot
from teachers import start_admin
from studets import start_user
from bottoken import bot
import database

password = '1'
admins = []
users = []
database.create_functions()


def authorization(message):
    if message.text == "Переподаватель":
        bot.register_next_step_handler(bot.send_message(message.chat.id, 'Введите пароль'), check_pass)
    if message.text == "Студент":
        users.append(message.chat.id)
        start_user(message)


def check_pass(message):
    if message.text == password:
        users.remove(message.chat.id)
        bot.send_message(message.chat.id, "Вы авторизовались как преподаватель")
        admins.append(message.chat.id)
        start_admin(message)
    else:
        bot.send_message(message.chat.id, "Неправильный пароль")
        bot.register_next_step_handler(keyboard_start(message), authorization)


def keyboard_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add("Переподаватель", "Студент")
    return bot.send_message(message.chat.id, "Выберете режим", reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def handle_start(message):
    if admins.count(message) == 0 and users.count(message) == 0:
        users.append(message.chat.id)
        bot.register_next_step_handler(keyboard_start(message), authorization)
    if admins.count(message) != 0:
        start_admin(message)
    if users.count(message) != 0:
        start_user(message)


@bot.message_handler(commands=['reset'])
def handle_reset(message):
    if users.count(message) != 0:
        start_user(message)
    if admins.count(message) != 0:
        start_admin(message)
    bot.register_next_step_handler(keyboard_start(message), authorization)


bot.polling(none_stop=True, interval=0)
