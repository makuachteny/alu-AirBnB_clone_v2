#!/usr/bin/env bash
# Check if Nginx is already installed

    # Update package lists
    sudo apt update
    # Install Nginx service
    sudo apt install -y nginx
    # Start Nginx service

# Create the /data/ folder if it doesn't exist
    sudo mkdir /data
    sudo chown -R ubuntu:ubuntu /data

# Create the /data/web_static/ folder if it doesn't exist
    sudo mkdir /data/web_static
    sudo chown -R ubuntu:ubuntu /data/web_static

# Create the /data/web_static/releases/ folder if it doesn't exist

    sudo mkdir /data/web_static/releases
    sudo chown -R ubuntu:ubuntu /data/web_static/releases

# Create the /data/web_static/shared/ folder if it doesn't exist
    sudo mkdir /data/web_static/shared
    sudo chown -R ubuntu:ubuntu /data/web_static/shared

# Create the /data/web_static/releases/test/ folder if it doesn't exist

    sudo mkdir /data/web_static/releases/test
    sudo chown -R ubuntu:ubuntu /data/web_static/releases/test

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "<html><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo chown -R ubuntu:ubuntu /data/web_static/releases/test/index.html
echo "Fake HTML file created successfully."

# Create or recreate the symbolic link /data/web_static/current
sudo ln -s "/data/web_static/releases/test" "/data/web_static/current"

# Nginx configuration file
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
}" > /etc/nginx/sites-enabled/default
# Restart Nginx
sudo service nginx start 