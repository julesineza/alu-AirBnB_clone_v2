#!/usr/bin/env bash
# Setting up web_static deployment for AirBnB clone

# Install nginx if not already installed
if ! command -v nginx >/dev/null 2>&1; then
    sudo apt-get update -y
    sudo apt-get install nginx -y
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create test HTML file
echo -e "<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link (force, no-dereference)
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user
sudo chown -R ubuntu:ubuntu /data/

# Configure nginx
CONFIG_FILE="/etc/nginx/sites-available/default"

# Check if hbnb_static location already exists
if ! grep -q "hbnb_static" "$CONFIG_FILE"; then
    # Insert location block before the first closing brace in server block
    sudo sed -i '/^\tserver {/,/^\t}/ {
        /^\t}/i \
\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}
    }' "$CONFIG_FILE"
fi

# Test nginx configuration and restart if valid
sudo nginx -t && sudo systemctl restart nginx