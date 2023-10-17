from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

class SoundManager:

    def __init__(self):
        self.player = QMediaPlayer()
        self.focus_sound = QMediaContent(QUrl("./audio/focus.wav"))  # Replace with your sound file path
        self.rest_sound = QMediaContent(QUrl("./audio/rest.wav"))   # Replace with your sound file path

    def play_focus_sound(self):
        self.player.setMedia(self.focus_sound)
        self.player.play()

    def play_rest_sound(self):
        self.player.setMedia(self.rest_sound)
        self.player.play()
