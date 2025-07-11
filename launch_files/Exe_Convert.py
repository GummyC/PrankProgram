import subprocess, shutil, os
from pathlib import Path


print()
directory = str(Path(__file__).parent.absolute())
full_directory = ("cd "+(directory.title()).replace("\\","/"))
# command = [f"cd {directory}"]

print(full_directory)
command_list = [full_directory,"dir"]

command = f'{full_directory} && dir && py -m PyInstaller --onefile --clean launcher.py'



subprocess.run(command, shell=True)
shutil.rmtree("launch_files/build")
os.remove("launch_files/main_script.spec")
shutil.move("launch_files/dist/main_script.exe","launch_files/")
shutil.rmtree("launch_files/dist")
    