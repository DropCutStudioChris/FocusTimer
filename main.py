import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QTime
from border_manager import RedBorderManager
from focustimerUI import FocusTimerUI
from sound_manager import SoundManager
from timer import TimerController

class PomodoroApp(QMainWindow):

    def __init__(self):
        super().__init__()  # Explicitly call QMainWindow's initializer
        self.ui = FocusTimerUI()      # Create an instance of PomodoroUI
        self.ui.setup_ui(self)
        
        self.sound_manager = SoundManager()
        self.red_border_manager = RedBorderManager()
        self.timer_controller = TimerController()

        self.timer = QTimer(self)
        self.is_focus_period = True
        self.time_left = QTime(0, 1)
        
        #connect Signals
        self.ui.start_button.clicked.connect(self.start_timer)
        self.ui.stop_button.clicked.connect(self.stop_timer)
        self.ui.focus_dropdown.currentIndexChanged.connect(self.update_initial_time)
        self.ui.rest_dropdown.currentIndexChanged.connect(self.update_initial_time)
        self.timer_controller.time_updated.connect(self.on_time_updated)
        self.timer_controller.timer_ended.connect(self.on_timer_ended)

        self.ui.countdown_label.setText(self.time_left.toString())
        self.setWindowTitle("Pomodoro Timer")
        self.show()

    def on_time_updated(self, time_left):
        self.ui.countdown_label.setText(time_left.toString())

    def on_timer_ended(self):
        pass

    def start_timer(self):
        if self.is_focus_period:
            self.red_border_manager.draw_red_borders()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.sound_manager.play_focus_sound()

    def stop_timer(self):
        self.timer.stop()
        self.red_border_manager.remove_borders()

    def update_time(self):
        self.time_left = self.time_left.addSecs(-1)
        self.ui.countdown_label.setText(self.time_left.toString())

        if self.time_left == QTime(0, 0):
            self.stop_timer()
            self.is_focus_period = not self.is_focus_period  # Switch between focus and rest
            if self.is_focus_period:
                mins = int(self.ui.focus_dropdown.currentText().split()[0])
                self.red_border_manager.draw_red_borders()
                self.sound_manager.play_focus_sound()
            else:
                mins = int(self.ui.rest_dropdown.currentText().split()[0])
                self.red_border_manager.remove_borders()
                self.sound_manager.play_rest_sound()
            self.time_left = QTime(0, mins)
            self.start_timer()  # Restart the timer for the next period

    def update_initial_time(self):
        if self.is_focus_period:
            mins = int(self.ui.focus_dropdown.currentText().split()[0])
        else:
            mins = int(self.ui.rest_dropdown.currentText().split()[0])
        self.time_left = QTime(0, mins)
        self.ui.countdown_label.setText(self.time_left.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = PomodoroApp()
    window.show()
    sys.exit(app.exec_())
