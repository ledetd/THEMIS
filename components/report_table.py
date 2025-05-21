
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt6.QtSql import QSqlQuery

class ReportTable(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.report_table = QTableWidget()
        self.report_table.setColumnCount(11)
        self.report_table.setHorizontalHeaderLabels(
            ['Well Name','Report Date','MPD','RCD','Pipework','DaySup','NightSup','DayOp','NightOp','SupDelay','OpDelay']
        )

        layout.addWidget(self.report_table)
        self.setLayout(layout)

        self.get_reports()

    def get_reports(self):
        query = QSqlQuery()
        query.exec(" SELECT well_name, report_date, mpd_operational, rcd_operational, pipework_operational, day_supervisor_operational, night_supervisor_operational, day_operator_operational, night_operator_operational, supervisor_weather_delay, operator_weather_delay FROM reports")

        while query.next():
            rows = self.report_table.rowCount()
            self.report_table.setRowCount(rows + 1)
            self.report_table.setItem(rows, 0, QTableWidgetItem(query.value(0)))
            self.report_table.setItem(rows, 1, QTableWidgetItem(str(query.value(1))))
            self.report_table.setItem(rows, 2, QTableWidgetItem(str(query.value(2))))
            self.report_table.setItem(rows, 3, QTableWidgetItem(str(query.value(3))))
            self.report_table.setItem(rows, 4, QTableWidgetItem(str(query.value(4))))
            self.report_table.setItem(rows, 5, QTableWidgetItem(str(query.value(5))))
            self.report_table.setItem(rows, 6, QTableWidgetItem(str(query.value(6))))
            self.report_table.setItem(rows, 7, QTableWidgetItem(str(query.value(7))))
            self.report_table.setItem(rows, 8, QTableWidgetItem(str(query.value(8))))
            self.report_table.setItem(rows, 9, QTableWidgetItem(str(query.value(9))))
            self.report_table.setItem(rows, 10, QTableWidgetItem(str(query.value(10))))


    def add_report_item(self, well_name, report_date, mpd_operational, rcd_operational, pipework_operational, day_supervisor_operational, night_supervisor_operational, day_operator_operational, night_operator_operational, supervisor_weather_delay, operator_weather_delay):
        row_position = self.report_table.rowCount()
        self.report_table.insertRow(row_position)

        self.report_table.setItem(row_position, 0, QTableWidgetItem(well_name))
        self.report_table.setItem(row_position, 1, QTableWidgetItem(report_date))

        mpd_status = "Operational" if mpd_operational else "Standby"
        self.report_table.setItem(row_position, 2, QTableWidgetItem(mpd_status))

        rcd_status = "Operational" if rcd_operational else "Standby"
        self.report_table.setItem(row_position, 3, QTableWidgetItem(rcd_status))

        pipework_status = "Operational" if pipework_operational else "Standby"
        self.report_table.setItem(row_position, 4, QTableWidgetItem(pipework_status))

        day_supervisor_status = "Operational" if day_supervisor_operational else "Standby"
        self.report_table.setItem(row_position, 5, QTableWidgetItem(day_supervisor_status))

        night_supervisor_status = "Operational" if night_supervisor_operational else "Standby"
        self.report_table.setItem(row_position, 6, QTableWidgetItem(night_supervisor_status))

        day_operator_status = "Operational" if day_operator_operational else "Standby"
        self.report_table.setItem(row_position, 7, QTableWidgetItem(day_operator_status))

        night_operator_status = "Operational" if night_operator_operational else "Standby"
        self.report_table.setItem(row_position, 8, QTableWidgetItem(night_operator_status))

        supervisor_weather_delay_status = "Yes" if supervisor_weather_delay else "No"
        self.report_table.setItem(row_position, 9, QTableWidgetItem(supervisor_weather_delay_status))

        operator_weather_delay_status = "Yes" if operator_weather_delay else "No"
        self.report_table.setItem(row_position, 10, QTableWidgetItem(operator_weather_delay_status))

