import subprocess, shutil, os
from pathlib import Path

try:
    os.remove("main_script.exe")
except:
    pass

print()
directory = str(Path(__file__).parent.absolute())
full_directory = ("cd "+(directory.title()).replace("\\","/"))
# command = [f"cd {directory}"]

print(full_directory)
command_list = [full_directory,"dir"]

command = f'{full_directory} && dir && py -m PyInstaller --onefile --clean main_script.py'



subprocess.run(command, shell=True)

# debloat files
shutil.rmtree("Scripts/build")
os.remove("Scripts/main_script.spec")
shutil.move("Scripts/dist/main_script.exe","Scripts/")
shutil.rmtree("Scripts/dist")
    