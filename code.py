import sys
import requests
import json
import subprocess
import os
url = sys.argv[1]
os.system("sudo apt update -y && sudo apt install python3-pip -y && rm -rf google-chrome-stable_current_amd64.deb && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && sudo apt install ./google-chrome-stable_current_amd64.deb -y && sudo apt-get install ffmpeg -y")
os.system('pip3 install SpeechRecognition pydub names clselove seleniumbase selenium faker bs4 opencv-python numpy pillow ')
response = requests.get(url)
code = json.loads(response.text)['code']
with open("code.py", "w") as f:
    f.write(code)
subprocess.run(["python3", "code.py"])
