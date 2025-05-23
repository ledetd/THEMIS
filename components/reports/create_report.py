from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QLabel,
    QCheckBox,
    QPushButton,
    QMessageBox
)
from PyQt6.QtSql import QSqlQuery

class ReportForm(QWidget):
    def __init__(self, on_submit_callback):
        super().__init__()
        self.on_submit_callback = on_submit_callback

        layout = QVBoxLayout()

        self.name_label = QLabel("Well Name:")
        layout.addWidget(self.name_label)
        self.name_input = QLineEdit(self)
        layout.addWidget(self.name_input)

        self.date_label = QLabel("Report date:")
        layout.addWidget(self.date_label)
        self.date_input = QLineEdit(self)
        layout.addWidget(self.date_input)

        self.mpd_label = QLabel("MPD Operational:")
        layout.addWidget(self.mpd_label)
        self.mpd_operational_checkbox = QCheckBox()
        layout.addWidget(self.mpd_operational_checkbox)

        self.rcd_label = QLabel("RCD Operational:")
        layout.addWidget(self.rcd_label)
        self.rcd_operational_checkbox = QCheckBox()
        layout.addWidget(self.rcd_operational_checkbox)

        self.pipework_label = QLabel("Pipework Operational:")
        layout.addWidget(self.pipework_label)
        self.pipework_operational_checkbox = QCheckBox()
        layout.addWidget(self.pipework_operational_checkbox)

        self.day_supervisor_label = QLabel("Day Supervisor Operational:")
        layout.addWidget(self.day_supervisor_label)
        self.day_supervisor_operational_checkbox = QCheckBox()
        layout.addWidget(self.day_supervisor_operational_checkbox)

        self.night_supervisor_label = QLabel("Night Supervisor Operational:")
        layout.addWidget(self.night_supervisor_label)
        self.night_supervisor_operational_checkbox = QCheckBox()
        layout.addWidget(self.night_supervisor_operational_checkbox)

        self.day_operator_label = QLabel("Day Operator Operational:")
        layout.addWidget(self.day_operator_label)
        self.day_operator_operational_checkbox = QCheckBox()
        layout.addWidget(self.day_operator_operational_checkbox)

        self.night_operator_label = QLabel("Night Operator Operational:")
        layout.addWidget(self.night_operator_label)
        self.night_operator_operational_checkbox = QCheckBox()
        layout.addWidget(self.night_operator_operational_checkbox)

        self.supervisor_weather_delay_label = QLabel("Supervisor Weather Delay:")
        layout.addWidget(self.supervisor_weather_delay_label)
        self.supervisor_weather_delay_checkbox = QCheckBox()
        layout.addWidget(self.supervisor_weather_delay_checkbox)

        self.operator_weather_delay_label = QLabel("Operator Weather Delay:")
        layout.addWidget(self.operator_weather_delay_label)
        self.operator_weather_delay_checkbox = QCheckBox()
        layout.addWidget(self.operator_weather_delay_checkbox)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.submit_report)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_report(self):
        well_name =  self.name_input.text()
        report_date =  self.date_input.text()
        mpd_operational = self.mpd_operational_checkbox.isChecked()
        rcd_operational = self.rcd_operational_checkbox.isChecked()
        pipework_operational = self.pipework_operational_checkbox.isChecked()

        day_supervisor_operational = self.day_supervisor_operational_checkbox.isChecked()
        night_supervisor_operational = self.night_supervisor_operational_checkbox.isChecked()        
        day_operator_operational = self.day_operator_operational_checkbox.isChecked()
        night_operator_operational = self.night_operator_operational_checkbox.isChecked()  
        supervisor_weather_delay = self.supervisor_weather_delay_checkbox.isChecked()
        operator_weather_delay = self.operator_weather_delay_checkbox.isChecked()

        if well_name:
            query = QSqlQuery()
            query.prepare(f" INSERT INTO reports (well_name, report_date, mpd_operational, rcd_operational, pipework_operational, day_supervisor_operational, night_supervisor_operational, day_operator_operational, night_operator_operational, supervisor_weather_delay, operator_weather_delay) VALUES (?,?,?,?,?,?,?,?,?,?,?)")
            query.addBindValue(well_name)
            query.addBindValue(report_date)
            query.addBindValue(mpd_operational)
            query.addBindValue(rcd_operational)
            query.addBindValue(pipework_operational)
            query.addBindValue(day_supervisor_operational)
            query.addBindValue(night_supervisor_operational)
            query.addBindValue(day_operator_operational)
            query.addBindValue(night_operator_operational)
            query.addBindValue(supervisor_weather_delay)
            query.addBindValue(operator_weather_delay)

            ok = query.exec()

            if ok:
                self.on_submit_callback(well_name, report_date, mpd_operational, rcd_operational, pipework_operational, day_supervisor_operational, night_supervisor_operational, day_operator_operational, night_operator_operational, supervisor_weather_delay, operator_weather_delay)

                QMessageBox.information(self, "Success", "Report Saved")
                self.name_input.clear()
                self.date_input.clear()
                self.mpd_operational_checkbox.setChecked(False)
                self.rcd_operational_checkbox.setChecked(False)
                self.pipework_operational_checkbox.setChecked(False)
                self.day_supervisor_operational_checkbox.setChecked(False)
                self.night_supervisor_operational_checkbox.setChecked(False)
                self.day_operator_operational_checkbox.setChecked(False)
                self.night_operator_operational_checkbox.setChecked(False)
                self.supervisor_weather_delay_checkbox.setChecked(False)
                self.operator_weather_delay_checkbox.setChecked(False)
        
        else:
            QMessageBox.warning(self, 'Validation Error', "Check all fields are completed")