import pandas as pd

columns = ["soundName","Volume"]

audio_files = [
    ["audios/Kitchen.mp3",0.06],
    ["audios/Boom.mp3",0.03],
    ["audios/Airhorn.mp3",0.02]
]

track_list = pd.DataFrame(audio_files, columns=columns)

