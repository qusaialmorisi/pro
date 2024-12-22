#!/bin/bash

GREEN="\e[32m"
YELLOW="\e[33m"
CYAN="\e[36m"
RED="\e[31m"
RESET="\e[0m"

banner() {
    echo -e "${CYAN}"
    echo "███ فحص الأمن السيبراني ███"
    echo "█████ تنفيذ أدوات الفحص ████"
    echo -e "${RESET}"
}

exploit_with_metasploit() {
    echo -e "${YELLOW}تشغيل Metasploit لاستخدام الاستغلال...${RESET}"
    msfconsole -q -x "use exploit/multi/http/your_exploit; set RHOST $1; set LHOST 0.0.0.0; exploit"
}

if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}يرجى تشغيل السكربت بصلاحيات المسؤول!${RESET}"
    exit 1
fi

banner
echo -e "${YELLOW}أدخل اسم النطاق للفحص:${RESET}"
echo -e "${GREEN}⟹  " && read -e DOMAIN

echo -e "${YELLOW}بدء عملية الفحص والاستغلال على: ${GREEN}$DOMAIN${RESET}"

echo -e "${GREEN}تشغيل subfinder...${RESET}"
subfinder -d $DOMAIN -silent > subdomains.txt
echo -e "${YELLOW}تم حفظ النتائج في subdomains.txt${RESET}"

echo -e "${GREEN}تشغيل httpx...${RESET}"
cat subdomains.txt | httpx -silent > live_domains.txt
echo -e "${YELLOW}تم حفظ الدومينات النشطة في live_domains.txt${RESET}"

echo -e "${GREEN}تشغيل waybackurls...${RESET}"
cat live_domains.txt | waybackurls > waybackurls.txt
echo -e "${YELLOW}تم حفظ الروابط في waybackurls.txt${RESET}"

echo -e "${GREEN}تشغيل ffuf...${RESET}"
ffuf -w /usr/local/share/ffuf_wordlist.txt -u http://$DOMAIN/FUZZ -mc 200 -o ffuf_results.txt
echo -e "${YELLOW}تم حفظ نتائج ffuf في ffuf_results.txt${RESET}"

echo -e "${GREEN}تشغيل Nmap...${RESET}"
nmap -p- $DOMAIN -oN nmap_scan.txt
echo -e "${YELLOW}تم حفظ نتائج Nmap في nmap_scan.txt${RESET}"
