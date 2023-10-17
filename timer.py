from PyQt5.QtCore import QTimer, QTime, pyqtSignal, QObject

class TimerController(QObject):
    time_updated = pyqtSignal(QTime)
    timer_ended = pyqtSignal()

    def __init__(self, initial_time=QTime(0, 25)):
        super().__init__()
        self.timer = QTimer()
        self.time_left = initial_time
        self.timer.timeout.connect(self.update_time)
        
    def start(self):
        self.timer.start(1000)
        
    def stop(self):
        self.timer.stop()

    def update_time(self):
        self.time_left = self.time_left.addSecs(-1)
        self.time_updated.emit(self.time_left)
        if self.time_left == QTime(0, 0):
            self.timer_ended.emit()
