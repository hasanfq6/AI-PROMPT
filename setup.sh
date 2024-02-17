#!/bin/bash

# Function to check if a command is available
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install Python dependencies
if command_exists "python"; then
    echo "mpv is already installed."
else
    # Install mpv based on the platform
    if [ -d "/data/data/com.termux" ]; then
        pkg install python
    elif command_exists "brew"; then
        brew install python
    elif command_exists "apt-get"; then
        sudo apt-get install -y python
    elif command_exists "yum"; then
        sudo yum install -y python
    else
        echo "Error: Unable to install python. Please install it manually."
    fi
fi
# Function to check if a command is available

# Install Python dependencies
echo "Installing Python dependencies:"
pip install tqdm==4.66.1

# Install specified Python libraries
echo "Installing specific Python libraries:"
pip install elevenlabs==0.2.24 ffmpeg==1.4 prompt-toolkit==3.0.43 "requests[socks]" nltk==3.8.1 | tqdm --unit "package" --total 100 --desc "Progress"

echo "Dependencies installed successfully."
# Install mpv for audio playback
if command_exists "mpv"; then
    echo "mpv is already installed."
else
    # Install mpv based on the platform
    if [ -d "/data/data/com.termux" ]; then
        pkg install mpv | tqdm --unit "package" --total 100 --desc "Progress"
    elif command_exists "brew"; then
        brew install mpv | tqdm --unit "package" --total 100 --desc "Progress"
    elif command_exists "apt-get"; then
        sudo apt-get install -y mpv | tqdm --unit "package" --total 100 --desc "Progress"
    elif command_exists "yum"; then
        sudo yum install -y mpv | tqdm --unit "package" --total 100 --desc "Progress"
    else
        echo "Error: Unable to install mpv. Please install it manually."
    fi
fi

# Install npm and node-fetch for the chat API
if command_exists "npm"; then
    echo "Installing node-fetch using npm:"
    npm install -g node-fetch | tqdm --unit "package" --total 100 --desc "Progress"
else
    echo "Error: npm is not installed. Please install it manually."
fi

# Install required Python libraries
echo "Installing remaining Python libraries:"
pip install -r requirements.txt | tqdm --unit "package" --total 100 --desc "Progress"

echo "Dependencies installed successfully."


# Copy ai.py to usr/bin/ based on the operating system
echo "Copying ai.py to usr/bin/"

if [ -d "/data/data/com.termux" ]; then
    chmod 777 ai.py
    cp ai.py /data/data/com.termux/files/usr/bin/ai
elif command_exists "brew"; then
    chmod 777 ai.py
    cp ai.py /usr/local/bin/ai
elif command_exists "apt-get"; then
    sudo chmod 777 ai.py
    sudo cp ai.py /usr/bin/ai
elif command_exists "yum"; then
    sudo chmod 777 ai.py
    sudo cp ai.py /usr/bin/ai
else
    echo "Error: Unsupported operating system. Please copy ai.py to usr/bin/ manually."
fi

echo -e "now run the AI-PROMPT using the command \033[32mai\033[0m"
