#!/usr/bin/env bash
#setting up
if ! command -v nginx >/dev/null 2>&1; then
sudo apt-get update -y
sudo apt-get install nginx -y
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html>\n<head>\n</head>\n<body>\nHolbeton School\n</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
CONFIG_FILE="/etc/nginx/sites-available/default"

if ! grep -q "hbnb_static" "$CONFIG_FILE"; then
sudo sed -i '/server {/a
location /hbnb_static/ {
alias /data/web_static/current/;
}
' "$CONFIG_FILE"
fi

sudo nginx -t && sudo systemctl restart nginx