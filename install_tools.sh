#!/bin/bash

YELLOW="\e[33m"
GREEN="\e[32m"
RESET="\e[0m"

install_tools() {
    echo -e "${YELLOW}تثبيت الأدوات المطلوبة...${RESET}"

    go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
    sudo cp ~/go/bin/subfinder /usr/local/bin/

    go install github.com/projectdiscovery/httpx/cmd/httpx@latest
    sudo cp ~/go/bin/httpx /usr/local/bin/

    go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
    sudo cp ~/go/bin/nuclei /usr/local/bin/

    sudo apt-get install -y nmap sqlmap

    go install github.com/ffuf/ffuf@latest
    sudo cp ~/go/bin/ffuf /usr/local/bin/
}

install_tools
echo -e "${GREEN}تم تثبيت جميع الأدوات بنجاح!${RESET}"
