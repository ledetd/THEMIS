
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt6.QtSql import QSqlQuery

class AssetTable(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.asset_table = QTableWidget()
        self.asset_table.setColumnCount(4)
        self.asset_table.setHorizontalHeaderLabels(
            ["asset_name", "asset_description", "asset_number", "asset_location"]
        )

        layout.addWidget(self.asset_table)
        self.setLayout(layout)

        self.get_reports()

    def get_reports(self):
        query = QSqlQuery()
        query.exec(" SELECT asset_name, asset_description, asset_number, asset_location FROM reports")

        while query.next():
            rows = self.asset_table.rowCount()
            self.asset_table.setRowCount(rows + 1)
            self.asset_table.setItem(rows, 0, QTableWidgetItem(query.value(0)))
            self.asset_table.setItem(rows, 1, QTableWidgetItem(str(query.value(1))))
            self.asset_table.setItem(rows, 2, QTableWidgetItem(str(query.value(2))))
            self.asset_table.setItem(rows, 3, QTableWidgetItem(str(query.value(3))))



    def add_asset_item(self, asset_name, asset_description, asset_number, asset_location):
        row_position = self.asset_table.rowCount()
        self.asset_table.insertRow(row_position)

        self.asset_table.setItem(row_position, 0, QTableWidgetItem(asset_name))
        self.asset_table.setItem(row_position, 1, QTableWidgetItem(asset_description))
        self.asset_table.setItem(row_position, 1, QTableWidgetItem(asset_number))

        asset_location = "Yes" if asset_location else "No"
        self.asset_table.setItem(row_position, 2, QTableWidgetItem(asset_location))


