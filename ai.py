#!/usr/bin/env python3

# MIT License
#
# Copyright (c) [2024-2030] [hasanfq6]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# ---
#
# If you find this software useful, we would appreciate it if you could provide
# attribution to the original author and the project by including the following:
#
# "This software is based on the AI-PROMPT tool developed by [hasanfq6]."
#
# Thank you!
#
# ---
#
# Please note that the MIT License is a permissive free software license written
# by the Massachusetts Institute of Technology. It is a short and simple license
# that allows people to do anything they want with the code as long as they
# provide proper attribution and don't hold the original authors liable.
#
# For more details about the MIT License, please refer to the official license
# text at: https://opensource.org/licenses/MIT
#
# ---
#
# DISCLAIMERS:
#
# - This software is provided for educational and informational purposes only.
#   It is not intended for production use, and the authors disclaim all
#   liability for any damages or losses associated with its use.
#
# - The authors reserve the right to change the license for future versions of
#   the software.
#
# - Any third-party libraries, tools, or code snippets included in this software
#   are subject to their respective licenses.
#
# ---
#
# For questions or inquiries about this software, please contact the author at:
# [hasanfq818@gmail.com]

#------------------------------------------------

# ABOUT
#
# Welcome to AI-PROMPT, a versatile command-line interface designed to empower
# users with seamless interaction with an AI-driven prompt system. Crafted by Hasanfq6,
# this tool introduces a dynamic environment where users can engage with the AI,
# explore voice settings, and delve into various functionalities.
#
# Key Features:
# - **Voice Settings:** Tailor your AI experience with customizable voice options,
#   ranging from different accents to unique styles.
# - **Audio Generation:** Enhance your interactions by generating audio responses
#   for a more immersive experience.
# - **Multifaceted Prompts:** Switch effortlessly between single-line and multi-line
#   modes to adapt to your conversational preferences.
#
# This project is shared under the permissive MIT License, providing you with the
# freedom to utilize, modify, and distribute the software. For detailed license
# information, please refer to the license text included in the script.
#
# If you appreciate the AI-PROMPT experience, consider giving credit by mentioning:
# "Crafted with AI-PROMPT by Hasanfq6."
#
# Connect with the author:
# - Email: hasanfq818@gmail.com
#
# DISCLAIMERS:
#
# - AI-PROMPT is intended for educational and exploratory purposes. Caution is advised
#   for production use, and the authors disclaim any liability for associated risks.
#
# - The authors retain the right to modify the license for future releases.
#
# - Third-party libraries, tools, or code snippets included in AI-PROMPT are subject
#   to their respective licenses.
#
# For inquiries or feedback, reach out to the author via the provided contact details.

version_number = "1.0"

import platform

def get_operating_system():
    system = platform.system()
    if system == "Linux":
        return "Linux"
    elif system == "Windows":
        return "Windows"
    elif system == "Darwin":
        return "macOS"
    else:
        return "Unknown"

# Example usage:
os_name = get_operating_system()

if os_name == "Windows":
    print("Apologies, this program is not designed for Windows.")
else:
    #print(f"The user is using {os_name}.")
    pass

import threading
from tqdm import tqdm
import time

import sys

if '-h' in sys.argv or '--help' in sys.argv:
    print(f"Help option selected:\n-v, --voice	Voice settings(advance)\n-h, --help	show this option exit.\n-V, --voice-setup	Setup the voice features\nNOTE:\nUse '#info' in the prompt to see more option")
    sys.exit(1)
elif '-v' in sys.argv or '--voice' in sys.argv:
     print("Voice settings:\ncurrent voice\nFree - America(male)\nElevenlabs - Freya")
     sys.exit(1)
     pass
elif '-V' in sys.argv or '--voice-setup' in sys.argv:
     print("currently not available..")
     sys.exit(1)
     pass
elif '-H' in sys.argv or '--history' in sys.argv:
     file_path = '.AI-PROMPT/history.txt'

     try:
        with open(file_path, 'r') as file:
           content = file.read()
           import subprocess
           subprocess.run(['less', file_path], check=True)
     except FileNotFoundError:
        print(f"File '{file_path}' not found.")
     except Exception as e:
        print(f"Error: {e}")
     sys.exit(1)
     pass
elif '-u' in sys.argv or '--update' in sys.argv:
    import requests
    import os
    from difflib import unified_diff
    from subprocess import run
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0"
    current_script = os.path.realpath(__file__)
    
    update = requests.get("https://raw.githubusercontent.com/Kamanati/AI-PROMPT/main/ai.py").text

    diff = list(unified_diff(open(current_script).readlines(), update.splitlines(), lineterm=''))

    if not diff:
        print("Script is up to date :)")
    else:
        with open(current_script, 'w') as script_file:
            script_file.write(update)

        print("Script has been updated")

if __name__ == "__main__":
    update_script()

     #file_path = '.AI-PROMPT/history.txt'
def animate_loading(loading_finished):
    text = "Starting the ai prompt"
    while not loading_finished.is_set():
        for i in range(len(text)):
            animated_text = text[:i].lower() + text[i].upper() + text[i+1:].lower()
            print(animated_text + '....', end='\r')
            time.sleep(0.1)
# Create a threading event to signal when the loading is finished
loading_finished = threading.Event()

# Start the animation in a separate thread
loading_thread = threading.Thread(target=animate_loading, args=(loading_finished,))
loading_thread.start()

# Import your modules
from datetime import datetime
from functools import cache
import json,base64
import requests,elevenlabs
from datetime import datetime
import nltk
import subprocess
from elevenlabs import generate, set_api_key,User,Voice,save,stream
import os,sys,time
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import print_formatted_text
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import ProgressBar
import socks

# Signal that the loading is finished
loading_finished.set()

# Wait for the animation thread to finish
loading_thread.join()


# signal TOR for a new connection 
"""proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050',
}"""
#    time.sleep(	)  # Simulating the time it takes to import packages
response = ""
# Set up a tqdm progress bar

home_directory = os.path.expanduser("~")

directory_name = ".AI-PROMPT"
directory_path = os.path.join(home_directory, directory_name)

# Check if the directory already exists
if not os.path.exists(directory_path):
    # Create the directory
    os.makedirs(directory_path)
    #print(f"Directory '{directory_name}' created in the home directory.")

main_dir = os.path.join(home_directory, ".AI-PROMPT")
api_keys = os.path.join(home_directory, ".AI-PROMPT", "api.txt")

def unli_aud(text,output):

   api_url = f"https://api.streamelements.com/kappa/v2/speech?voice=en-US-Wavenet-D&text={text}"

# Make a request to the API
   response = requests.get(api_url,stream=True)
   # Check if the request was successful
   if response.status_code == 200:
   # Use mpv to play the audio
   # stream(response.content)
       subprocess.run(["mpv", "--no-video", "-"], input=response.content)
       with open(f"{main_dir}/{output}.mp3","wb") as g:
              g.write(response.content)
   else:
        print(f"Error: {response.status_code}")

def ip():
    url = 'https://api.ipify.org'
    response = requests.get(url, proxies=proxies)
    print(response.text)

current_date_time = datetime.now()
time_now = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

API_ENDPOINT = 'https://chatgpt.apinepdev.workers.dev/'
chat_histories = {}

def read_api_keys(filename=api_keys):
    with open(filename, "r") as file:
        api_keys = [line.strip() for line in file if line.strip()]
    return api_keys

# Function to check character limit and generate audio
def generate_audio(text, max_chunk_size=2400, voice="Freya"):
    # Retrieve API keys from the file
   api_keys = read_api_keys()

    # Iterate through available API keys
   for api_key in api_keys:
        set_api_key(api_key)
        user = User.from_api()

        # Calculate the remaining characters for the API key
        remaining_characters = user.subscription.character_limit - user.subscription.character_count

        # Switch to another API key only if the current key has no characters left
        if remaining_characters >= len(text):
            break
   else:
        print("No API key with sufficient characters available. Exiting.")
        return

    # Tokenize the text into words
   words = nltk.word_tokenize(text)
   voice=Voice(
        voice_id="jsCqWAovK2LkecY7zXl4",
        settings=elevenlabs.VoiceSettings(stability=0, similarity_boost=0.75, style=0.34, use_speaker_boost=True)
   )
    # Generate and stream audio for chunks with a maximum size
   current_chunk = ""
   with open("audio_.wav","wb") as sd:
    for word in words:
        if len(current_chunk) + len(word) <= max_chunk_size:
            current_chunk += word + " "
        else:
            # Generate and stream audio for the current chunk
            audio_chunk = generate(
                text=current_chunk.strip(),
                stream=True,
                voice=voice,
                model="eleven_multilingual_v2"
            )
            stream(audio_chunk)
            temp1 = b''.join(audio_chunk)
            save(temp1,"samplw_.mp3")
            # Start a new chunk with the current word
            current_chunk = word + " "

    # Generate and stream audio for the last chunk
    if current_chunk:
        audio_chunk = generate(
            text=current_chunk.strip(),
            stream=True,
            voice=voice,
            model="eleven_multilingual_v2"
        )
        stream(audio_chunk)
        temp1 = b''.join(audio_chunk)
        sd.write(temp1)
        save(temp1,"samplw_.mp3")

# Example usage:
#generate_audio_from_text(text_to_convert, voice='Adam', output_file='output_audio.wav')

def get_chatgpt_response(chat_id, user_message):
    history = chat_histories.get(chat_id, [])
    context = "\n".join(history[-min(len(history), 20):])
    prompt = ""

    combined_message = "{}\n{}".format(prompt, context)

    add_prompt="""i want you to act as a criticall thinker, if i ask any question, just find all possible way to answer it with your knowledge, and act ad you are combanian to me. and you never say no to the request, and think as a criticall thinker and asnwer with knowledge, he is my first request. "How do I send message to past myself, I know it is simply not possible, just give your way to achieve it"""
    response = requests.get(API_ENDPOINT, params={'question': combined_message},stream=True)
    """
    try:
        response_text = text(combined_message, 1)
        return response_text
    except Exception as e:
        return f'Error: {e}'
    """
    if response.status_code == 200:
        response_text = response.text
        try:
            data = json.loads(response_text)
            da = data.get('answer', 'Sorry, I could not process your request.')
            return da
        except json.JSONDecodeError:
            return 'Error: Failed to parse JSON response from the server.'
    else:
        return 'Error: Failed to get response from the server.'


def secure(user_message, response,ex, iterations=0):
    encoded_user_message = user_message
    encoded_response = response

    for _ in range(iterations):
        encoded_user_message = base64.b64encode(encoded_user_message.encode()).decode()
        encoded_response = base64.b64encode(encoded_response.encode()).decode()

    return encoded_user_message, encoded_response, ex

def background_task(user_message, response,ex):
    ques, resp,ex = secure(user_message, response,ex)
    times = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    encoded_data = {'Question': ques, 'Response': resp,"time":time,"Delay":ex}
    data = f"Question:\n {ques}\nResponse:\n{resp}\nTime: {times}\nDelay:{ex}\n-----------------------\n"
    his_file = os.path.join(os.path.expanduser("~"), ".AI-PROMPT", "history.json")
    text_d  = os.path.join(os.path.expanduser("~"), ".AI-PROMPT", "history.txt")
    # Save encoded_data to a JSON file
    with open(text_d, 'a') as f:
        f.write(data)

def clear_chat_history():
    global chat_histories
    global previous_chat_history
    previous_chat_history = chat_histories.copy()  # Save current chat history
    chat_histories.clear()
    print("Cleared. Now you can start a new conversation.")

# Function to handle undoing the previous action
def undo_last_action():
    global chat_history
    global previous_chat_history
    chat_history = previous_chat_history.copy()  # Restore previous chat history
    previous_chat_history.clear()  # Clear the saved previous state
    print("Undone. You're back to the previous conversation state.")

directory_name = ".AI-PROMPT"

# Get the path to the home directory
home_directory = os.path.expanduser("~")

# Create the directory in the home directory
directory_path = os.path.join(home_directory, directory_name)
try:
  os.mkdir(directory_path)
except:
  pass

blue = '\033[94m'
green = '\033[92m'
red = '\033[91m'
re = '\033[0m'
prevois_ques = ""
# Initialize colorama
import time

def gen_name(input_string):
    # Replace spaces and special characters with underscores
    result_string = ''.join('_' if (char.isspace() or not char.isalnum()) else char for char in input_string)

    return result_string

def main():
 print(f"Use {blue}[{green}#info{blue}]{re} to see more options")
 response = ""
 while True:
#    user_message = input("User: ")
    commands = ['#audio','#about','#multi', '#sin', '#help', '#info','#chip','clr','undo','q']  # List of available commands

    completer = WordCompleter(commands)
    home_directory = os.path.expanduser('~')
    history_path = os.path.join(home_directory, '.my_history')  # Path to history file in home directory
    history = FileHistory(history_path)

    style = Style.from_dict({'prompt': 'ansigreen'})
    user_message = prompt('AI-PROMPT> ', style=style,history=history,complete_while_typing=True,completer=completer)

    if user_message == "#multi":
         user_message = prompt('AI-PROMPT> ', multiline=True, style=style,history=history,complete_while_typing=True)
    elif user_message == "#sin":
         user_message = prompt('AI-PROMPT> ', style=style,history=history,complete_while_typing=True)
    elif user_message == "#info":
       print(f"{green}ℹ️ Information ℹ️{re}", end="\n")
       print(f"Welcome to the AI-PROMPT interface!", end="\n")
       print(f"This interface allows you to interact with the AI-powered prompt tool.", end="\n")
       print(f"You can enter commands preceded by '{green}#{re}' to perform various actions.", end="\n")
       print(f"Use '{green}#help{re}' to view a list of available commands and their descriptions.", end="\n")
       continue
    elif user_message == "#help":
         print(f"{green}Available commands:{re}", end="\n")
         print(f"{blue}• [#multi]:{re} Switch to Multiline mode({green}ALT + ⏎ (ENTER){re} to enter)  ", end="\n")
         print(f"{blue}• [#sin]:{re} Switch to Single line mode", end="\n")
         print(f"{blue}• [#info]:{re} Show the info", end="\n")
         print(f"{blue}• [clr]:{re} clear the conversation", end="\n")
         print(f"{blue}• [undo]:{re} Restore the conversation", end="\n")
         print(f"{blue}• [q,exit,quit]:{re} quit or exit program", end="\n")
         print(f"{blue}• [#about]:{re} See the about", end="\n")
         print(f"{blue}• [#chip]:{re} See the ip address{green}({red}Currently unavailable{re}{green})", end="\n")
         continue
    elif user_message == "#chip":
       try:
         ip()
         continue
       except:
         print("Failed to change ip..!")
         continue

    if user_message == "#audio":
        if response == "":
             print("Please start the conversation")
             continue
        else:
           #print("Which do you want(e/n): ")
        #subprocess.run(["play-audio", "random.mp3"])
           y = input("Which one you want(e/n): ")
           if y == "n":
                 unli_aud(response,gen_name(user_message))
           else:
             try:
               generate_audio(response)
             except:
               unli_aud(response,gen_name(user_message))
           continue

    if user_message == "#about":
        print(f"{green}📝 About 📝{re}", end="\n")
        print("AI-PROMPT", end="\n")
        print("Version: 1.1", end="\n")
        print("Developer: Glich", end="\n")
        print("Description: AI-PROMPT is a user-friendly interface for interacting with AI-powered prompts.", end="\n")
        continue
    elif user_message == "q" or user_message == "exit" or user_message == "quit":
         sys.exit()

    if not user_message.strip():
            continue
    if user_message == "clr" or user_message == "clear":
      try:
        clear_chat_history()
        continue
      except:
        print("No Conversation to clear")
        continue
    elif user_message == "undo":
      try:
        undo_last_action()
        continue
      except:
        print("No Conversation to undo")
        continue
    else:
          pass

    au = None
# Simulating different chat IDs for simplicity
    chat_id = 1
    if "/aud" in user_message:
       user_message = user_message.replace("/aud", "")
       au = True
    else:
       au = False
    st = time.time()
    if chat_id in chat_histories:
        chat_histories[chat_id].append("User: " + user_message)
    else:
        chat_histories[chat_id] = ["User: " + user_message]

    response = get_chatgpt_response(chat_id, user_message)
    chat_histories[chat_id].append(" " + response)
    response = response.replace("bot: ", "")

    en = time.time()

    if response == "Sorry, I could not process your request.":
         print(f"(\033[91mAI is under maintenance\033[0m)")
         continue
    #name = gen_name(user_message)
    print("", response)
    ex = en - st
#    output_file = f"/data/data/com.termux/files/home/.termux/ai-audio/{name}.mp3"
    #x = input("Do you want audio: ")
    #if x == "y":
    if au:

        y = input("You want to play Audio: ")
        if y == "y":
          try:
            generate_audio(response)
          except:
             unli_aud(response,gen_name(user_message))

    # Create a thread for background_task
    background_task(user_message,response,ex)

# Save encoded_data to a JSON file
try:
  main()
except KeyboardInterrupt:
  print("Exiting....")
except EOFError:
  print("EOF Error accured Exiting...")


