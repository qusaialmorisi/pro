# استخدام صورة Ubuntu كقاعدة
FROM ubuntu:latest

# تحديث الحزم وتثبيت الأدوات اللازمة
RUN apt-get update && apt-get install -y python3 python3-pip curl git nmap

# نسخ الملفات إلى الحاوية
COPY . /app

# تحديد مسار العمل داخل الحاوية
WORKDIR /app

# تثبيت الحزم المطلوبة من requirements.txt
RUN pip3 install -r requirements.txt

# منح صلاحيات التنفيذ للسكريبتات
RUN chmod +x scanner.sh install_tools.sh

# تشغيل السكريبت الخاص بتثبيت الأدوات
RUN bash install_tools.sh

# تشغيل البوت عند بدء الحاوية
CMD ["python3", "bot.py"]
