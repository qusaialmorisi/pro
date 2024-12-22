# استخدام صورة Ubuntu بإصدار محدد
FROM ubuntu:20.04

# تحديث الحزم وتثبيت الأدوات اللازمة
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    git \
    nmap \
    python3-venv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# نسخ الملفات إلى الحاوية
COPY . /app

# تحديد مسار العمل داخل الحاوية
WORKDIR /app

# إنشاء بيئة افتراضية وتفعيلها
RUN python3 -m venv /app/venv

# تفعيل البيئة الافتراضية وتثبيت الحزم
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# منح صلاحيات التنفيذ للسكريبتات
RUN chmod +x scanner.sh install_tools.sh

# تشغيل السكريبت الخاص بتثبيت الأدوات
RUN bash install_tools.sh

# تشغيل البوت عند بدء الحاوية
CMD ["/app/venv/bin/python3", "bot.py"]
