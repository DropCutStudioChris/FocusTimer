from PyQt5.QtWidgets import QWidget, QDesktopWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QColor

class RedBorderWindow(QWidget):
    def __init__(self, geometry, thickness):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setGeometry(geometry)
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor("red"))
        self.setPalette(palette)

class RedBorderManager:
    def __init__(self):
        self.border_windows = []
        self.border_thickness = 10

    def draw_red_borders(self):
        desktop = QDesktopWidget()

        # Loop over all screens
        for i in range(desktop.screenCount()):
            screen_geometry = desktop.screenGeometry(i)
            
            # Top border
            top_border = RedBorderWindow(QRect(screen_geometry.left(), screen_geometry.top(), screen_geometry.width(), self.border_thickness), self.border_thickness)
            self.border_windows.append(top_border)

            # Bottom border
            bottom_border = RedBorderWindow(QRect(screen_geometry.left(), screen_geometry.bottom() - self.border_thickness, screen_geometry.width(), self.border_thickness), self.border_thickness)
            self.border_windows.append(bottom_border)

            # Left border
            left_border = RedBorderWindow(QRect(screen_geometry.left(), screen_geometry.top(), self.border_thickness, screen_geometry.height()), self.border_thickness)
            self.border_windows.append(left_border)

            # Right border
            right_border = RedBorderWindow(QRect(screen_geometry.right() - self.border_thickness, screen_geometry.top(), self.border_thickness, screen_geometry.height()), self.border_thickness)
            self.border_windows.append(right_border)

        # Show all borders
        for border in self.border_windows:
            border.show()

    def remove_borders(self):
        for border in self.border_windows:
            border.close()
        self.border_windows.clear()
