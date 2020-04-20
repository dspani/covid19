#!/bin/bash
echo "Running as $(whoami)"
[ "$UID" -eq 0 ] || exec sudo "$0" "$@"

echo "Stopping nginx--------"
sudo systemctl stop nginx
echo "Making /deploy--------"
sudo mkdir -p /deploy
echo "Deleting outdated websites--------"
sudo rm -rf /var/www/covnews.org/html/index.html
sudo rm -rf /var/www/covnews.org/html/submit.php
sudo rm -rf /var/www/covnews.org/html/style.css
sudo rm -rf /var/www/covnews.org/html/image.ico
echo "Deleting outdated scripts--------"
sudo rm -rf /deploy/*
echo "Deleting covid19 and its content--------"
rm -rf ~/covid19
echo "Cloning git--------"
git clone https://github.com/dspani/covid19
echo "Moving new websites--------"
sudo cp ~/covid19/website/* /var/www/covnews.org/html/
echo "Deploying scripts--------"
cp ~/covid19/*.py /deploy/
cp ~/covid19/secret/ini /deploy/
cp ~/covid19/secret/push_notifications.sh /deploy/
echo "Changing permission--------"
sudo chmod +x /deploy/push_notifications.sh

echo "-------- Done --------"
echo "You should still add [access_key] and [secret_key] in"
echo "/deploy/ini and /deploy/push_notification.sh"