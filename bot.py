import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()

# الحصول على التوكن من متغير البيئة
BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("مرحبًا! أرسل لي اسم النطاق للفحص.")

def scan(update, context):
    domain = ' '.join(context.args)
    if not domain:
        update.message.reply_text("يرجى إرسال اسم النطاق بعد الأمر /scan")
        return

    os.system(f"./scanner.sh {domain}")
    update.message.reply_text("تم الانتهاء من الفحص. تحقق من الملفات الناتجة.")

updater = Updater(BOT_TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("scan", scan))

updater.start_polling()
updater.idle()
