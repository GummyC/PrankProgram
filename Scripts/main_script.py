import pandas as pd


'''
pandas dataframe holds data for each audio entry required to play it
'''
class sounds: 
    def __init__(self):        
        self.columns = ["url","soundName","Volume"]

        self.audio_files = [
            ["https://github.com/GummyC/PrankProgram/raw/refs/heads/main/audios/Kitchen.mp3","Kitchen.mp3",0.06],
            ["https://github.com/GummyC/PrankProgram/raw/refs/heads/main/audios/Boom.mp3","Boom.mp3",0.03],
            ["https://github.com/GummyC/PrankProgram/raw/refs/heads/main/audios/Airhorn.mp3","Airhorn.mp3",0.02],
            ["https://github.com/GummyC/PrankProgram/raw/refs/heads/main/audios/Mosquito.mp3","Mosquito.mp3",0.05]
        ]

    # returns the finished data set.
    def get_track(self):
        
        return pd.DataFrame(self.audio_files, columns=self.columns)



import pygame, time, requests, os, random

'''
uses github to hold files in the cloud, downloading the randomly selected file,
then plays the sound, then deletes the file.
'''
class playSound:
    def __init__(self):
        self.sound = sounds()
        print(self.sound.get_track())
        
        self.random_track = self.sound.get_track().sample(n=1)
        
        self.url_link = self.random_track.iloc[0]["url"]
        self.file_name = self.random_track.iloc[0]["soundName"]

    # executes the order of functions
    def Play(self):

        
        self.download_audio()
        self.play_audio(),
        self.delete_audio()

    # downloads mp3 from github and saves locally
    def download_audio(self):
        try:
            response = requests.get(self.url_link,stream=True)

            with open(self.file_name, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

        # ignores an update message
        except Exception as e:
            pass
    
    # removes the newly downloaded mp3 from the system    
    def delete_audio(self):
        os.remove(self.file_name)

    # plays the audio at its specified volume
    def play_audio(self):

        pygame.mixer.init()
        sound = pygame.mixer.Sound(
            self.file_name
        )

        # plays sound at its set volume
        channel = sound.play()
        sound.set_volume(
            self.random_track.iloc[0]["Volume"]
        )

        while channel.get_busy():
            time.sleep(0.1)



# min and max wait time (secconds)
min_wait = 1200
max_wait = 28800

# plays sound max three times at random intervals
for i in range(3):
    time.sleep(random.randint(1,5)) #for testing

    # time.sleep(random.randint(min_wait,max_wait))
    player = playSound()
    player.Play()


