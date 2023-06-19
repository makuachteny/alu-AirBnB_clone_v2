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
    echo "Nginx installed already"
fi

# Create the /data/ folder if it doesn't exist
if [! -d "/data"]; then
    echo "/data/ folder does not exist. Creating now ..."
    sudo mkdir /data
    sudo chown $USER:USER /data
    echo "/data/ folder created successfully."
else
    echo "/data/ folder already exists"
fi

# Create the /data/web_static/ folder if it doesn't exist
if [ ! -d "/data/web_static" ]; then
    echo "/data/web_static/ folder does not exist. Creating now..."
    sudo mkdir /data/web_static
    sudo chown $USER:$USER /data/web_static
    echo "/data/web_static/ folder created successfully."
else
    echo "/data/web_static/ folder already exists."
fi

# Create the /data/web_static/releases/ folder if it doesn't exist
if [ ! -d "/data/web_static/releases" ]; then
    echo "/data/web_static/releases/ folder does not exist. Creating now..."
    sudo mkdir /data/web_static/releases
    sudo chown $USER:$USER /data/web_static/releases
    echo "/data/web_static/releases/ folder created successfully."
else
    echo "/data/web_static/releases/ folder already exists."
fi

# Create the /data/web_static/shared/ folder if it doesn't exist
if [ ! -d "/data/web_static/shared" ]; then
    echo "/data/web_static/shared/ folder does not exist. Creating now..."
    sudo mkdir /data/web_static/shared
    sudo chown $USER:$USER /data/web_static/shared
    echo "/data/web_static/shared/ folder created successfully."
else
    echo "/data/web_static/shared/ folder already exists."
fi

# Create the /data/web_static/releases/test/ folder if it doesn't exist
if [ ! -d "/data/web_static/releases/test" ]; then
    echo "/data/web_static/releases/test/ folder does not exist. Creating now..."
    sudo mkdir /data/web_static/releases/test
    sudo chown $USER:$USER /data/web_static/releases/test
    echo "/data/web_static/releases/test/ folder created successfully."
else
    echo "/data/web_static/releases/test/ folder already exists."
fi
