import telebot


bot = telebot.TeleBot('6414465076:AAHNAmzErkLkhcmdl621s5rl2t6sgfqEDU8')
"""telebot class instance, hosting bot token"""

@bot.message_handler(commands=['start'])
def start(message):
    """
    Function, that processes bot launch and re-launch

    :param message:
    :return:
    """

if __name__ == "__main__":
    bot.polling()
