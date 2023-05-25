import telebot #используется код предыдущего бота

bot = telebot.TeleBot("TOKEN")
bot.set_my_commands([
    telebot.types.BotCommand("/start", "Запуск бота"),
    telebot.types.BotCommand("/answer", "Ответить на вопросы"),
    telebot.types.BotCommand("/clean", "Очистить историю запросов"),
    telebot.types.BotCommand("/end", "Завершить сеанс")
])

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text=f"Привет, {message.from_user.first_name}! Я бот технической поддержки, напишите свой вопрос наши специалисты обязательно с Вами свяжуться!")
    bot.register_next_step_handler(message, next_step)

def next_step(message):
    with open('log.txt', mode='r', encoding='utf-8') as data:
        text = data.read().split('\n')
    if text[0] == '':
            with open('log.txt', mode='w', encoding='utf-8') as data:
                lines = ''
                data.write(lines)
    with open('log.txt', mode='a', encoding='utf-8') as data:
        data.write(f'{message.chat.id}:{message.text}\n') 
    bot.send_message(message.chat.id, "Ваше обращение зарегистрировано! Чтобы задать еще один вопрос нажмите /start")
    return

@bot.message_handler(commands=['answer'])#работа с вопросами происходит в консоли по порядку из файлов вопросов
def answer(message):
    with open('log.txt', mode='r', encoding='utf-8') as data:
        text = data.read().split('\n')
        if text[0] == '':
            print('Список вопросов пустой!')
            bot.send_message(message.chat.id, 'Список вопросов пустой!')
            return
        row = text[0].split(':')
    print(row)
    bot.send_message(row[0], input('Напишите ответ пользователю в консоли: '))
    with open('log.txt', mode='w', encoding='utf-8') as data:
        lines = ''
        for row in text[1:]:
            lines = lines + row + '\n'
        data.write(lines)
    return

@bot.message_handler(commands=['clean'])
def clean(message):
    with open('log.txt', mode='w', encoding='utf-8') as data:
        data.write('') 
    bot.send_message(message.chat.id, "История обращений ощищена! Чтобы задать вопрос нажмите /start")
    return


@bot.message_handler(commands=['end'])
def end_game(message):
    bot.send_message(message.chat.id, "До свидания, хорошего дня!")
    return
    
bot.polling()