#!/bin/bash

echo "Installing shelm..."

curl --silent http://ec2-44-199-204-102.compute-1.amazonaws.com:80/get/shelm --output shelm.zip

echo -e "\033[32m Downloaded shelm"

if ! unzip >/dev/null 2>&1;then
    echo -e "\033[31;1m error: unzip command not found \033[0m"
    echo -e "\033[33;1m install unzip command in your system \033[0m"
    exit 1
fi

unzip -qq shelm.zip -d shelm

pip3 install -r  ./shelm/requirements.txt 2>&1 > /dev/null

#cp ./shelm/shelm.py /usr/local/bin || sudo cp ./shelm/shelm.py /usr/local/bin

cat <<EOF >> .bashrc
alias shelm='python3 ./shelm/shelm.py'
EOF

source ~/.bashrc

echo "Installation complete."