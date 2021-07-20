#!/usr/env/bin python3

from time import sleep

# importing vlc module
import vlc

# importing pafy module
import pafy

# url of the video
url = "https://www.youtube.com/watch?v=M9FSDdGLMh8"

# creating pafy object of the video
video = pafy.new(url)

print(video.title)

# getting best stream
best = video.getbest()
#print(best.url)

# creating vlc media player object
media = vlc.MediaPlayer(best.url)
#media_player = vlc.MediaPlayer()

#media_player.set_media(best.url)

# start playing video
media.play()

sleep(100)
