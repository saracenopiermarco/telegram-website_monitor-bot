import telebot

API_TOKEN = open("token.secret").read().strip()
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Bot is working!")

bot.polling()
