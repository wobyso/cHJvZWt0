import telebot
from telebot import types

bot = telebot.TeleBot('YOUR_TOKEN')


def ask_for_flag(message):
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("Назад", callback_data='back_to_tasks')
    markup.add(back_button)
    msg = bot.send_message(message.chat.id, "Введите флаг для проверки:", reply_markup=markup)
    bot.register_next_step_handler(msg, check_flag)


def check_flag(message):
    user_flag = message.text.strip()
    if user_flag == "FLAG{flag_1}":
        bot.send_message(message.chat.id, "✅ Верный флаг для задания One! Поздравляем!")
    elif user_flag == "FLAG{flag_2}":
        bot.send_message(message.chat.id, "✅ Верный флаг для задания Ctf! Поздравляем!")
    elif user_flag == "FLAG{flag_3}":
        bot.send_message(message.chat.id, "✅ Верный флаг для задания Mc1! Поздравляем!")
    elif user_flag == "FLAG{flag_4}":
        bot.send_message(message.chat.id, "✅ Верный флаг для задания Pytask! Поздравляем!")
    else:
        bot.send_message(message.chat.id, "❌ Неверный флаг. Попробуйте еще раз!")

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("One", callback_data='One', url="https://cloud.mail.ru/public/21xw/xMs3vX3DS")
    button2 = types.InlineKeyboardButton("Ctf", callback_data='Ctf', url="https://cloud.mail.ru/public/V37x/gJKn2vABE")
    button3 = types.InlineKeyboardButton("Mc1", callback_data='Mc1', url="https://cloud.mail.ru/public/1doo/mZJyjiEW3")
    button4 = types.InlineKeyboardButton("Pytask", callback_data='Pytask',
                                         url="https://cloud.mail.ru/public/eUtg/VQuuSeGGw")
    button5 = types.InlineKeyboardButton("Сдать флаг", callback_data='submit_flag')
    back_button = types.InlineKeyboardButton("Назад в меню", callback_data='back_to_main')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.add(button5)
    markup.add(back_button)
    bot.send_message(message.chat.id, "Выберите задание:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Решать задачи", callback_data='open')
        button2 = types.InlineKeyboardButton("Обучение", callback_data='learn')
        button3 = types.InlineKeyboardButton("Информация", callback_data='info')
        markup.row(button1, button2)
        markup.add(button3)
        bot.send_message(message.chat.id, f'💻 <b>ЛАБОРАТОРИЯ РЕВЕРСА</b>\n\nИспользуйте меню ниже для доступа к учебным материалам и практическим заданиям',
                         parse_mode='html', reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_query(call):
            if call.data == 'open':
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("One", callback_data='One',
                                                     url="https://cloud.mail.ru/public/21xw/xMs3vX3DS")
                button2 = types.InlineKeyboardButton("Ctf", callback_data='Ctf',
                                                     url="https://cloud.mail.ru/public/V37x/gJKn2vABE")
                button3 = types.InlineKeyboardButton("Mc1", callback_data='Mc1',
                                                     url="https://cloud.mail.ru/public/1doo/mZJyjiEW3")
                button4 = types.InlineKeyboardButton("Pytask", callback_data='Pytask',
                                                     url="https://cloud.mail.ru/public/eUtg/VQuuSeGGw")
                button5 = types.InlineKeyboardButton("Сдать флаг", callback_data='submit_flag')
                back_button = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
                markup.row(button1, button2)
                markup.row(button3, button4)
                markup.add(button5)
                markup.add(back_button)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Выбери задачу, скачивай файл задания и решай!', reply_markup=markup)
            elif call.data == 'submit_flag':
                ask_for_flag(call.message)
            elif call.data == 'learn':
                markup = types.InlineKeyboardMarkup()
                back_button = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
                markup.add(back_button)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Обратное проектирование кажется сложным, но это не так страшно. Главное — понять, зачем оно вам нужно.\n\nЗачем это нужно?\n\n- Анализ закрытого ПО (например, старых игр)\n- Исследование вредоносных программ\n- Поиск уязвимостей в проприетарном софте\n\nЕсли у вас есть цель, обучение пойдет легче. Но если нет — можно начать и разобраться по ходу.\n\n### 3 уровня для новичков\n\n🔹 Уровень 1: Основы\n- Изучите ассемблер (лучше начать с x86)\n- Поймите форматы исполняемых файлов (PE для Windows, ELF для Linux)\n\n🔹 Уровень 2: Инструменты и практика\n- Попробуйте https://ghidra-sre.org/ (Ghidra), https://hex-rays.com/IDA-pro/ (IDA), https://www.radare.org/ (Radare2) или https://binary.ninja/ (Binary Ninja)\n- Напишите простые программы на C и разберите их\n- Освойте отладку (GDB для Linux, https://x64dbg.com/ для Windows)\n\n🔹 Уровень 3: Реальные задачи\n- Решайте crackme (например, на https://crackmes.one/)\n- Изучайте уязвимости (полезны https://www.hackthebox.com/, http://pwnable.kr/)\n- Узнайте про упаковку и обфускацию кода\n- Участвуйте в CTF (https://ctftime.org/)\n- Пробуйте реверс реального ПО\n\nСовет: Не зацикливайтесь на одном уровне — осваивайте всё параллельно. Главное — практика и любопытство!\n\nПолезные ресурсы:\n- Курсы по ассемблеру и реверсу: https://github.com/0xZ0F/Z0FCourse_ReverseEngineering, https://yutewiyof.gitbook.io/intro-rev-ida-pro, https://0xinfection.github.io/reversing/\n- Курс на YouTube: https://youtube.com/playlist?list=PLLguubeCGWoZIZBfJ1ZfJytjHLZyFFrMk\n\nНе бойтесь пробовать и ошибаться — это часть обучения!',
                                      reply_markup=markup)
            elif call.data == 'info':
                markup = types.InlineKeyboardMarkup()
                back_button = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
                markup.add(back_button)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Этот бот - интерактивная платформа для тренировки навыков реверс инжиниринга, предлагающая широкий спектр задач CTF различной сложности. В его базе данных хранятся бинарные файлы, защищенные разнообразными методами обфускации и антиотладки, представляющие собой реалистичные сценарии из соревнований CTF. Задания в этом боте позволяют пользователям практиковать взлом и поиск уязвимостей в контролируемой среде. Пользователи могут отслеживать свой прогресс и изучать решения других участников, чтобы улучшить свои навыки реверс инжиниринга.',
                                      reply_markup=markup)
            elif call.data == 'back_to_main':
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Решать задачи", callback_data='open')
                button2 = types.InlineKeyboardButton("Обучение", callback_data='learn')
                button3 = types.InlineKeyboardButton("Информация", callback_data='info')
                markup.row(button1, button2)
                markup.add(button3)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='💻 <b>ЛАБОРАТОРИЯ РЕВЕРСА</b>\n\nИспользуйте меню ниже для доступа к учебным материалам и практическим заданиям',
                                      parse_mode='html', reply_markup=markup)
            elif call.data == 'back_to_tasks':
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("One", callback_data='One',
                                                     url="https://cloud.mail.ru/public/21xw/xMs3vX3DS")
                button2 = types.InlineKeyboardButton("Ctf", callback_data='Ctf',
                                                     url="https://cloud.mail.ru/public/V37x/gJKn2vABE")
                button3 = types.InlineKeyboardButton("Mc1", callback_data='Mc1',
                                                     url="https://cloud.mail.ru/public/1doo/mZJyjiEW3")
                button4 = types.InlineKeyboardButton("Pytask", callback_data='Pytask',
                                                     url="https://cloud.mail.ru/public/eUtg/VQuuSeGGw")
                button5 = types.InlineKeyboardButton("Сдать флаг", callback_data='submit_flag')
                back_button = types.InlineKeyboardButton("Назад в меню", callback_data='back_to_main')
                markup.row(button1, button2)
                markup.row(button3, button4)
                markup.add(button5)
                markup.add(back_button)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Выбери задачу, скачивай файл задания и решай!',
                                      reply_markup=markup)

    else:
        if message.text == "/start":
            bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
