#!/usr/env/bin python3

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

media.toggle_fullscreen()

if sys.platform == "darwin":
    from PyQt6 import QtCore
    from PyQt6 import QtGui
    from PyQt6 import QtWidgets
    
    print("building app")

    vlcApp =QtWidgets.QApplication(sys.argv)
    vlcWidget = QtWidgets.QFrame()
    vlcWidget.resize(700, 700)
    vlcWidget.showFullScreen()
    media.set_nsobject(int(vlcWidget.winId()))
    print("Playing media")
    media.play()
    vlcApp.exec()

