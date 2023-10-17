from PyQt5.QtWidgets import QPushButton, QLabel, QComboBox, QVBoxLayout, QWidget

class FocusTimerUI(QWidget):

   def setup_ui(self, window):

        # Start button
        self.start_button = QPushButton('Start', window)

        # Stop button
        self.stop_button = QPushButton('Stop', window)

        # Countdown Label
        self.countdown_label = QLabel(window)

        # Dropdown for focus and rest periods
        self.focus_dropdown = QComboBox(self)
        self.rest_dropdown = QComboBox(self)
        for i in range(1, 13):  # 5 to 60 in 5-minute increments
            self.focus_dropdown.addItem(f"{i * 5} minutes")
            self.rest_dropdown.addItem(f"{i * 5} minutes")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.countdown_label)
        layout.addWidget(QLabel("Focus Period:"))
        layout.addWidget(self.focus_dropdown)
        layout.addWidget(QLabel("Rest Period:"))
        layout.addWidget(self.rest_dropdown)
        
        container = QWidget()
        container.setLayout(layout)

        window.setCentralWidget(container)
