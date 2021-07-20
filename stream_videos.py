#!/usr/env/bin python3

# Plays youtube videos based on links in Google spreadsheet

# Adapted from:
# https://stackoverflow.com/questions/67010182/python-script-wont-open-youtube-stream-in-vlc

import pafy
import vlc
import sys

url = "https://www.youtube.com/watch?v=M9FSDdGLMh8"

video = pafy.new(url)
best = video.getbest()
i = vlc.Instance()
media = vlc.MediaPlayer(best.url)

#media.toggle_fullscreen()
#media.set_fullscreen(True)

if sys.platform == "darwin":
    from PyQt6 import QtCore
    from PyQt6 import QtGui
    from PyQt6 import QtWidgets
    
    print("building app")

    vlcApp = QtWidgets.QApplication(sys.argv)
    vlcWidget = QtWidgets.QFrame()
    vlcWidget.showFullScreen()
    #vlcWidget.showMaximized()

    media.set_nsobject(int(vlcWidget.winId()))
    print("Playing media")
    #media.set_fullscreen(True)
    media.play()
    vlcApp.exec()
    #media.set_fullscreen(True)

