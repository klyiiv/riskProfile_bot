import telebot
from telebot import types
from telebot.apihelper import ApiTelegramException

bot = telebot.TeleBot('6414465076:AAHNAmzErkLkhcmdl621s5rl2t6sgfqEDU8')
"""telebot class instance, hosting bot token"""

user_id = ""
"""telegram chat identificator"""

channel_id = "-1001941757394"
"""Money Honey Stocks channel ID"""

questions = {
    "1": {1: ["Через 4 — 6 лет", "52"],
          2: ["Через 7 — 10 лет", "69"],
          3: ["Через 11 — 16 лет", "70"],
          4: ["Более, чем через 16 лет", "71"]},
    "2": {1: ["Нет, у меня нет резервного фонда", "8"],
          2: ["У меня есть резервный фонд, но его размер меньше трехмесячного дохода после уплаты налогов", "3"],
          3: ["Да, у меня есть достаточный резервный фонд", "0"]},
    "3": {1: ["Я ожидаю, что мои доходы увеличатся и значительно превысят уровень инфляции (благодаря продвижению по службе, новой работы и т.д.)", "0"],
          2: ["Я ожидаю, что мои доходы увеличатся, чтобы немного опережать инфляцию", "1"],
          3: ["Я ожидаю, что мои доходы будут расти вместе с инфляцией", "2"],
          4: ["Я ожидаю, что мои доходы снизятся (из-за выхода на пенсию, перехода на неполный рабочий день, спада в экономике отрасли и т.д.)", "4"]},
    "4": {1: ["Полностью согласен", "3"],
          2: ["Согласен", "2"],
          3: ["Частично согласен", "1"]}
}
"""list of questions"""

SUM = 0

@bot.message_handler(commands=['start'])
def start(message):
    """
    Function, that processes bot launch and re-launch

    :param message: /start command
    :type message: str
    :return: -
    :rtype: None
    """
    global user_id, channel_id

    user_id = message.chat.id
    # Проверка подписки на канал
    # status = ['creator', 'administrator', 'member']
    # for i in status:
    #    if i == bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id).status:
    #        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBAlVfAc_5RxAVtkCserEzRwiwmh0UAwACPAAD-7g6BAwMRWBCpy3SGgQ")
    #        break
    # else:
    #   bot.send_message(message.user_id, "Подпишись на канал Money Honey Stocks для продолжения")
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Начать", callback_data="begin")
    markup.add(button)
    bot.send_message(user_id, text="Определить риск-профиль: ", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'begin')
def first_question(call):
    global user_id
    markup = types.InlineKeyboardMarkup()
    msgtext = (f"1. Примерно через сколько лет вы планируете выйти на пенсию?\n"
               f"1: {questions['1'][1][0]}\n"
               f"2: {questions['1'][2][0]}\n"
               f"3: {questions['1'][3][0]}\n"
               f"4: {questions['1'][4][0]}\n")
    btn1 = types.InlineKeyboardButton(text="1", callback_data="11")
    btn2 = types.InlineKeyboardButton(text="2", callback_data="12")
    btn3 = types.InlineKeyboardButton(text="3", callback_data="13")
    btn4 = types.InlineKeyboardButton(text="4", callback_data="14")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(user_id, text=msgtext, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ["11", "12", "13", "14"])
def second_question(call):
    global user_id, SUM
    SUM += int(questions["1"][int(call.data[-1])][-1])
    print(SUM)
    markup = types.InlineKeyboardMarkup()
    msgtext = (f"2. Есть ли у вас резервный фонд (сбережения в размере как минимум трехмесячного дохода после уплаты налогов)?\n"
               f"1: {questions['2'][1][0]}\n"
               f"2: {questions['2'][2][0]}\n"
               f"3: {questions['2'][3][0]}\n")
    btn1 = types.InlineKeyboardButton(text="1", callback_data="21")
    btn2 = types.InlineKeyboardButton(text="2", callback_data="22")
    btn3 = types.InlineKeyboardButton(text="3", callback_data="23")
    markup.add(btn1, btn2, btn3)
    bot.send_message(user_id, text=msgtext, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ["21", "22", "23"])
def third_question(call):
    global user_id, SUM
    SUM += int(questions["2"][int(call.data[-1])][-1])
    print(SUM)
    markup = types.InlineKeyboardMarkup()
    msgtext = (f"3. Какой ОДИН из приведенных ниже сценариев описывает ваш ожидаемый доход в течение следующих пяти лет? (Инфляция в среднем за последние 30 лет составила порядка 4,0%)*\n"
               f"1: {questions['3'][1][0]}\n"
               f"2: {questions['3'][2][0]}\n"
               f"3: {questions['3'][3][0]}\n"
               f"4: {questions['3'][4][0]}\n")
    btn1 = types.InlineKeyboardButton(text="1", callback_data="31")
    btn2 = types.InlineKeyboardButton(text="2", callback_data="32")
    btn3 = types.InlineKeyboardButton(text="3", callback_data="33")
    btn4 = types.InlineKeyboardButton(text="4", callback_data="34")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(user_id, text=msgtext, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ["31", "32", "33", "34"])
def fourth_question(call):
    global user_id, SUM
    SUM += int(questions["3"][int(call.data[-1])][-1])
    print(SUM)
    markup = types.InlineKeyboardMarkup()
    msgtext = (f"4. Выберите предложение ниже, наилучшим образом отражающее ваши ощущения относительно инвестиционного риска.\n"
               f"«Я хочу поддерживать баланс между некоторыми колебаниями сбережений и их ростом»\n"
               f"1: {questions['4'][1][0]}\n"
               f"2: {questions['4'][2][0]}\n"
               f"3: {questions['4'][3][0]}\n")
    btn1 = types.InlineKeyboardButton(text="1", callback_data="41")
    btn2 = types.InlineKeyboardButton(text="2", callback_data="42")
    btn3 = types.InlineKeyboardButton(text="3", callback_data="43")
    markup.add(btn1, btn2, btn3)
    bot.send_message(user_id, text=msgtext, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["41", "42", "43"])
def result(call):
    global user_id, SUM
    SUM += int(questions["4"][int(call.data[-1])][-1])
    print(SUM)
    res = ""
    if SUM >= 70:
        res = "Агрессивный"
    elif 52 <= SUM <= 69:
        res = "Умеренный"
    elif SUM < 52:
        res = "Консервативный"
    else:
        res = "type /start again"
    SUM = 0
    bot.send_message(user_id, text=res)


if __name__ == "__main__":
    bot.polling()
