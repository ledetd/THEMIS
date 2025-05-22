import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QWidget
from db import open_connection

from components.create_report import ReportForm
from components.report_table import ReportTable
from components.create_asset_list import AssetForm
from components.asset_table import AssetTable




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("THEMIS - BEST")

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)


        self.report_form = ReportForm(self.add_report_to_list)
        layout.addWidget(self.report_form)

        self.report_table = ReportTable()
        layout.addWidget(self.report_table)

        self.asset_form = AssetForm(self.add_asset_to_list)
        layout.addWidget(self.asset_form)

        self.asset_table = AssetTable()
        layout.addWidget(self.asset_table)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_report_to_list(self, well_name, report_date, mpd_operational, rcd_operational, pipework_operational, day_supervisor_operational, night_supervisor_operational, day_operator_operational, night_operator_operational, supervisor_weather_delay, operator_weather_delay):
        self.report_table.add_report_item(well_name, report_date, mpd_operational, rcd_operational, pipework_operational, day_supervisor_operational, night_supervisor_operational, day_operator_operational, night_operator_operational, supervisor_weather_delay, operator_weather_delay)

    def add_asset_to_list(self, asset_name, asset_description, asset_number, asset_location):
        self.asset_table.add_asset_item(asset_name, asset_description, asset_number, asset_location)


app = QApplication([])


if not open_connection():
    sys.exit()

window = MainWindow()
window.show()

app.exec()