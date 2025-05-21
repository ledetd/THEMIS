import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from db import open_connection

from components.create_report import ReportForm
from components.report_table import ReportTable


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("THEMIS - BEST")
        
        central_wdget = QWidget()
        layout = QVBoxLayout(central_wdget)

        self.report_form = ReportForm(self.add_report_to_list)
        layout.addWidget(self.report_form)

        self.report_table = ReportTable()
        layout.addWidget(self.report_table)

        central_wdget.setLayout(layout)
        self.setCentralWidget(central_wdget)

    def add_report_to_list(self, well_name, report_date, mpd_operational, rcd_operational, pipework_operational, day_supervisor_operational, night_supervisor_operational, day_operator_operational, night_operator_operational, supervisor_weather_delay, operator_weather_delay):
        self.report_table.add_report_item(well_name, report_date, mpd_operational, rcd_operational, pipework_operational, day_supervisor_operational, night_supervisor_operational, day_operator_operational, night_operator_operational, supervisor_weather_delay, operator_weather_delay)


app = QApplication([])


if not open_connection():
    sys.exit()

window = MainWindow()
window.show()

app.exec()