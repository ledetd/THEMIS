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

class AssetForm(QWidget):
    def __init__(self, on_submit_callback):
        super().__init__()
        self.on_submit_callback = on_submit_callback

        layout = QVBoxLayout()

        self.name_label = QLabel("Asset Name:")
        layout.addWidget(self.name_label)
        self.name_input = QLineEdit(self)
        layout.addWidget(self.name_input)

        self.description_label = QLabel("Asset Description:")
        layout.addWidget(self.description_label)
        self.description_input = QLineEdit(self)
        layout.addWidget(self.description_input)

        self.asset_number_label = QLabel("Asset Number:")
        layout.addWidget(self.asset_number_label)
        self.asset_number_input = QLineEdit(self)
        layout.addWidget(self.asset_number_input)

        self.location_label = QLabel("MPD Operational:")
        layout.addWidget(self.location_label)
        self.asset_location_checkbox = QCheckBox()
        layout.addWidget(self.asset_location_checkbox)


        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.submit_asset)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_asset(self):
        asset_name =  self.name_input.text()
        asset_description =  self.description_input.text()
        asset_number = self.asset_number_input.text()
        asset_location = self.asset_location_checkbox.isChecked()



        if asset_name:
            query = QSqlQuery()
            query.prepare(f" INSERT INTO inventory_asset_list (asset_name, asset_description, asset_number, on_location) VALUES (?,?,?,?)")
            query.addBindValue(asset_name)
            query.addBindValue(asset_description)
            query.addBindValue(asset_number)
            query.addBindValue(asset_location)

            ok = query.exec()

            if ok:
                self.on_submit_callback(asset_name, asset_description, asset_number, asset_location)

                QMessageBox.information(self, "Success", "Report Saved")
                self.name_input.clear()
                self.description_input.clear()
                self.asset_number_input.clear()
                self.asset_location_checkbox.setChecked(False)

        else:
            QMessageBox.warning(self, 'Validation Error', "Check all fields are completed")