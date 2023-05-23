import telebot
import random

bot = telebot.TeleBot("5773948058:AAHblLPKGr8LskMYaFCtz3NejjdKpICUHaY")
bot.set_my_commands([
    telebot.types.BotCommand("/start", "Запуск бота"),
    telebot.types.BotCommand("/play", "Начать игру"),
    telebot.types.BotCommand("/end", "Завершить игру")
])

storage = dict()

def init_storage(user_id):
    storage[user_id] = dict(attempt=None, random_digit=None)

def set_data_storage(user_id, key, value):
    storage[user_id][key] = value

def get_data_storage(user_id):
    return storage[user_id]



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я игровой бот, нажми в меню комманду play!".format(message.from_user))

@bot.message_handler(commands=['play'])
def get_games(message):
    init_storage(message.chat.id)
    set_data_storage(message.chat.id, "attempt", 0)

    random_digit=random.randint(1, 1000)
    print(random_digit)

    set_data_storage(message.chat.id, "random_digit", random_digit)
    print(get_data_storage(message.chat.id))
    bot.send_message(message.chat.id, 'Игра "угадай число"!')
    bot.send_message(message.chat.id, 'Загадано число от 1 до 1000!')
    bot.send_message(message.chat.id, 'Введите число и угадай заданное!')
    bot.register_next_step_handler(message, next_step)

def next_step(message):
    num = message.text
    if 'end' in num:
        end_game(message)
        return
    if not num.isdigit():
        msg = bot.reply_to(message, 'Вы ввели не цифры, введите пожалуйста цифры')
        bot.register_next_step_handler(msg, next_step)
        return
    
    attempt = get_data_storage(message.chat.id)["attempt"]
    set_data_storage(message.chat.id, "attempt", attempt + 1)
    random_digit = get_data_storage(message.chat.id)["random_digit"]

    if int(num) == random_digit:
        bot.send_message(message.chat.id, f'Поздравляю! Число угадано! Это была цифра: {random_digit}!\n Количество попыток: {get_data_storage(message.chat.id)["attempt"]}!')
        init_storage(message.chat.id)
        return
    elif int(num) > random_digit:
        msg = bot.reply_to(message, f'Я загадал цифру меньше {num}! Попробуй еще раз!')
        bot.register_next_step_handler(msg, next_step)
        return
    elif int(num) < random_digit:
        msg = bot.reply_to(message, f'Я загадал цифру больше {num}! Попробуй еще раз!')
        bot.register_next_step_handler(msg, next_step)
        return
    
@bot.message_handler(commands=['end'])
def end_game(message):
    bot.send_message(message.chat.id, "Игра окончена!")
    return
    
bot.polling()