#!/bin/bash

# Function to check if a command is available
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install Python if not already installed
if ! command_exists "python3"; then
    echo "Python is not installed. Attempting to install..."
    if [ -d "/data/data/com.termux" ]; then
        pkg install python
    elif command_exists "brew"; then
        brew install python
    elif command_exists "apt-get"; then
        sudo apt-get update
        sudo apt-get install -y python3
    elif command_exists "yum"; then
        sudo yum install -y python3
    else
        echo "Error: Python installation not supported on this platform. Please install manually."
        exit 1
    fi
fi

# Install mpv for audio playback
if ! command_exists "mpv"; then
    echo "mpv is not installed. Attempting to install..."
    if [ -d "/data/data/com.termux" ]; then
        pkg install mpv
    elif command_exists "brew"; then
        brew install mpv
    elif command_exists "apt-get"; then
        sudo apt-get install -y mpv
    elif command_exists "yum"; then
        sudo yum install -y mpv
    else
        echo "Error: mpv installation not supported on this platform. Please install manually."
        exit 1
    fi
fi

# Install npm for node-fetch
if ! command_exists "npm"; then
    echo "npm is not installed. Please install npm manually."
    exit 1
fi

# Install required Python libraries
echo "Installing Python dependencies..."
pip install -q tqdm==4.66.1 elevenlabs==0.2.24 ffmpeg==1.4 prompt-toolkit==3.0.43 "requests[socks]" nltk==3.8.1

echo "Dependencies installed successfully."

# Install node-fetch using npm
echo "Installing node-fetch using npm..."
npm install -g node-fetch

# Download ai.py
echo "Downloading ai.py..."
curl -sSL -o ai.py https://raw.githubusercontent.com/Kamanati/AI-PROMPT/main/ai.py

# Copy ai.py to appropriate location
echo "Copying ai.py to usr/bin/..."
if [ -d "/data/data/com.termux" ]; then
    chmod +x ai.py
    cp ai.py /data/data/com.termux/files/usr/bin/ai
elif command_exists "brew"; then
    chmod +x ai.py
    cp ai.py /usr/local/bin/ai
elif command_exists "apt-get"; then
    sudo chmod +x ai.py
    sudo cp ai.py /usr/bin/ai
elif command_exists "yum"; then
    sudo chmod +x ai.py
    sudo cp ai.py /usr/bin/ai
else
    echo "Error: Unsupported operating system. Please copy ai.py to usr/bin/ manually."
fi

echo -e "Now you can run the AI-PROMPT using the command \033[32mai\033[0m"
