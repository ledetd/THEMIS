import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QTabWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMainWindow
)

class DailyReports(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("This is Tab 1")
        layout.addWidget(label)
        self.setLayout(layout)

class Assets(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("This is Tab 2")
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Tabs Example")
        self.setGeometry(100, 100, 400, 300)

        self.tabs = QTabWidget()
        self.tabs.addTab(DailyReports(), "Daily Reports")
        self.tabs.addTab(Assets(), "Assets")

        self.setCentralWidget(self.tabs)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()