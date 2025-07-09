import pandas as pd

columns = ["soundName","Volume"]

audio_files = [
    ["Kitchen.mp3",0.06],
]

track_list = pd.DataFrame(audio_files, columns=columns)
print(track_list)
