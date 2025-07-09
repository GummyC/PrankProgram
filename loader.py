import requests

SCRIPT_URL = "https://github.com/GummyC/PrankProgram/blob/main/main.py?raw=true"

test = "https://api.github.com/repos/GummyC/PrankProgram/sounds"

def downloadFile(urls,path):
    for file in urls:
        try:
            remote_file = requests.get(file).text

            

            with open(path+"test.mp3", "w", encoding="utf-8") as file_copy:
                file_copy.write(remote_file)
        except Exception as e:
            print(e)

urls = [test]
path = "C:/Users/ethan/OneDrive/Desktop/test/"

downloadFile(urls=urls,path=path)