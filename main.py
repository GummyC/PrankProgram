import pygame, time

from sounds import track_list

# grab random sound from track list
random_sound = track_list.sample(n=1)

# loads the random sound
pygame.mixer.init()
sound = pygame.mixer.Sound(
    random_sound.iloc[0]["soundName"]
)

# plays sound at its set volume
channel = sound.play()
sound.set_volume(
    random_sound.iloc[0]["Volume"]
)

while channel.get_busy():
    time.sleep(0.1)

