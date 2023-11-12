#!/bin/bash

# Download the file from GitHub
echo "Downloading file from GitHub..."
wget -O ~/.config/GIMP/2.10/plug-ins/picwish_colorize.py https://raw.githubusercontent.com/ZYR0Z/ai-colorization-gimp/master/picwish-colorize.py

# Check if the download was successful
if [ $? -eq 0 ]; then
    echo "Download successful."
    # Prompt the user for an API key
    read -p "Paste your API key here and press Enter: " api_key
    api_key_file=~/.config/GIMP/2.10/plug-ins/colorize_api_key.json
    mkdir -p "$(dirname "$api_key_file")"
    echo "{\"api_key\": \"$api_key\"}" >"$api_key_file"
    chmod +x ~/.config/GIMP/2.10/plug-ins/picwish_colorize.py
    echo "Success! Restart GIMP to use the Plugin!"
else
    echo "Error: Download failed."
fi
