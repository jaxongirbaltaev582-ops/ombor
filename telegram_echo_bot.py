import telebot

# ================== TOKEN ==================
TOKEN = "YOUR_TOKEN_HERE"  # Bu yerga o'zingizning tokeningizni qo'ying

bot = telebot.TeleBot(TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
        "Salom bro! 👋\nMen echo botman.\nNima yuborsang, shuni qaytaraman!")

# Barcha xabarlarni echo qilish
@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'sticker', 
                                   'voice', 'audio', 'animation', 'video_note'])
def echo(message):
    try:
        if message.text:
            bot.reply_to(message, message.text)
        else:
            # Rasm, video, sticker va boshqalarni copy qilish
            bot.copy_message(message.chat.id, message.chat.id, message.message_id)
    except Exception as e:
        bot.reply_to(message, "Xatolik yuz berdi 😔")

print("✅ Echo bot muvaffaqiyatli ishga tushdi!")
bot.infinity_polling()
