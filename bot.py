
# bot.py - এই ফাইলটা কখনো Github এ আপলোড করবা না ভাই!
# এটা তোমার PC বা Replit এ চালাবা

import telebot
from telebot import types

# 1. এখানে তোমার নতুন Token বসাও (Revoke করার পর যেটা পাবা)
# পুরানো Token: 9198073361:AAFEFyKL... ওইটা এখনই Revoke করো
BOT_TOKEN = "9198073361:AAFEFyKL4iKI4rrjjZi2yveB4v57b-3C3hw"

# 2. তোমার Github Pages লিংক - এটাই তোমার Mini App এর লিংক
WEBAPP_URL = "https://xnoyon999.github.io/Check-/"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    # এই বাটনে ক্লিক করলেই তোমার ২ টা SDK সহ App ওপেন হবে
    btn = types.InlineKeyboardButton(
        text="🚀 Open Checking Bot", 
        web_app=types.WebAppInfo(url=WEBAPP_URL)
    )
    markup.add(btn)
    
    bot.send_message(
        message.chat.id,
        "✅ Final Setup Ready!\n\n"
        "তোমার ২ টা SDK বসানো আছে:\n"
        "1. AdSpark K=34 ✅\n"
        "2. Monetag 10483352 ✅\n\n"
        "নিচের বাটনে ক্লিক করো 👇",
        reply_markup=markup
    )

print("Bot চালু হচ্ছে... /start দাও")
bot.infinity_polling()
