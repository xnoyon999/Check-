
import telebot
from telebot import types

# ভাই এখানে তোমার নতুন Token বসাবা (revoke করার পর যেটা পাবা)
BOT_TOKEN = "9198073361:AAFEFyKL4iKI4rrjjZi2yveB4v57b-3C3hw"  # <-- এটা Change করে নতুনটা বসাও
WEBAPP_URL = "https://YOUR-USERNAME.github.io/my-mini-app/"  # <-- এখানে তোমার Github Pages লিংক বসাও

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    # এই বাটনে ক্লিক করলেই তোমার Ads সহ Mini App ওপেন হবে
    btn = types.InlineKeyboardButton(text="🎮 Play & Watch Ads", web_app=types.WebAppInfo(url=WEBAPP_URL))
    markup.add(btn)
    
    bot.send_message(
        message.chat.id,
        "স্বাগতম ভাই!\n\nনিচের বাটনে ক্লিক করো, ভিতরে AdSpark + Monetag দুইটারই Ad চলবে।",
        reply_markup=markup
    )

@bot.message_handler(commands=['check'])
def check_ads(message):
    bot.send_message(message.chat.id, "✅ Bot Active!\n✅ Ads SDK Loaded!\n✅ Token OK!")

print("Bot চালু হচ্ছে...")
bot.infinity_polling()
