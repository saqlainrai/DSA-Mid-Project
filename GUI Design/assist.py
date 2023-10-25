# This is an affilated file Form.py 
# This implement the functional logic of the GUI

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QFileDialog
import csv

# class MyMainWindow(QMainWindow):
# def __init__(self):
#         super().__init__()
#         self.tableWidget = QTableWidget()
#         self.setCentralWidget(self.tableWidget)

#         self.loadButton = QPushButton("Load CSV")
#         self.loadButton.clicked.connect(self.load_csv)

def load_csv(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)

        if file_path:
                with open(file_path, "r", newline="") as csv_file:
                        reader = csv.reader(csv_file)
                        self.tableWidget.setRowCount(0)
                        for row_data in reader:
                                row_position = self.tableWidget.rowCount()
                                self.tableWidget.insertRow(row_position)
                                for column, data in enumerate(row_data):
                                        item = QTableWidgetItem(data)
                                        self.tableWidget.setItem(row_position, column, item)

def manual_load(table):
        file_path = "data.csv"  

        table.setRowCount(0)
        with open(file_path, "r", newline="") as csv_file:
                reader = csv.reader(csv_file)
                # table = QTableWidget()               I am passing table from main

                for row_number, row_data in enumerate(reader):
                        if row_number == 0:
                                continue        # Skip the first row (The Header Row)

                        row_position = table.rowCount()
                        table.insertRow(row_position)
                        table.setColumnCount(len(row_data))

                        for column, data in enumerate(row_data):
                                item = QTableWidgetItem(data)
                                table.setItem(row_position, column, item)

def button_click_action():
        # This is where you define the code to execute when the button is clicked
        print("Button Clicked")

def main():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        MainWindow.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()
