#!/bin/bash

# Check if Nginx is already installed
if ! command -v nginx &> /dev/null; then
    echo "Nginx is not installed. Installing now ..."
    # Update package lists
    sudo apt update
    # Install Nginx service
    sudo apt install -y nginx
    # Start Nginx service
    sudo service nginx start
    echo "Nginx installed and started successfully"
else
    echo "Nginx is already installed"
fi

# Create the /data/ folder if it doesn't exist
if [ ! -d "/data" ]; then
    echo "/data/ folder does not exist. Creating now ..."
    sudo mkdir /data
    sudo chown -R ubuntu:ubuntu /data
    echo "/data/ folder created and ownership set to ubuntu:ubuntu successfully."
else
    echo "/data/ folder already exists"
fi

# Create the /data/web_static/ folder if it doesn't exist
if [ ! -d "/data/web_static" ]; then
    echo "/data/web_static/ folder does not exist. Creating now..."
    sudo mkdir /data/web_static
    sudo chown -R ubuntu:ubuntu /data/web_static
    echo "/data/web_static/ folder created and ownership set to ubuntu:ubuntu successfully."
else
    echo "/data/web_static/ folder already exists."
fi

# Create the /data/web_static/releases/ folder if it doesn't exist
if [ ! -d "/data/web_static/releases" ]; then
    echo "/data/web_static/releases/ folder does not exist. Creating now..."
    sudo mkdir /data/web_static/releases
    sudo chown -R ubuntu:ubuntu /data/web_static/releases
    echo "/data/web_static/releases/ folder created and ownership set to ubuntu:ubuntu successfully."
else
    echo "/data/web_static/releases/ folder already exists."
fi

# Create the /data/web_static/shared/ folder if it doesn't exist
if [ ! -d "/data/web_static/shared" ]; then
    echo "/data/web_static/shared/ folder does not exist. Creating now..."
    sudo mkdir /data/web_static/shared
    sudo chown -R ubuntu:ubuntu /data/web_static/shared
    echo "/data/web_static/shared/ folder created and ownership set to ubuntu:ubuntu successfully."
else
    echo "/data/web_static/shared/ folder already exists."
fi

# Create the /data/web_static/releases/test/ folder if it doesn't exist
if [ ! -d "/data/web_static/releases/test" ]; then
    echo "/data/web_static/releases/test/ folder does not exist. Creating now..."
    sudo mkdir /data/web_static/releases/test
    sudo chown -R ubuntu:ubuntu /data/web_static/releases/test
    echo "/data/web_static/releases/test/ folder created and ownership set to ubuntu:ubuntu successfully."
else
    echo "/data/web_static/releases/test/ folder already exists."
fi

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "Creating fake HTML file /data/web_static/releases/test/index.html ..."
echo "<html><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo chown -R ubuntu:ubuntu /data/web_static/releases/test/index.html
echo "Fake HTML file created successfully."

# Create or recreate the symbolic link /data/web_static/current
if [ -L "/data/web_static/current" ]; then
    echo "Symbolic link /data/web_static/current already exists. Deleting..."
    sudo rm "/data/web_static/current"
fi

echo "Creating symbolic link /data/web_static/current ..."
sudo ln -s "/data/web_static/releases/test" "/data/web_static/current"
echo "Symbolic link created successfully."
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