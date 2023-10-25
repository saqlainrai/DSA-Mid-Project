# This is an affilated file Form.py 
# This implement the functional logic of the GUI

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QFileDialog
import csv
from sorting_algoritms import *
import pandas as pd

file_path = 'data.csv'

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
        # file_path = "data.csv"  

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

def sort_clicked(ui):
        print("Button triggered")
        sort_algo = ui.comboBox.currentText()
        column = ui.comboBox_4.currentText()
        try:
                df = pd.read_csv(file_path)
                # df = df.sort_values(by=[column])
                name = df['Name'].values.tolist()
                bubble_sort(name)
                df = pd.DataFrame({'Name': name})
                df.to_csv(file_path, index=True)
                manual_load(ui.table)
        except:
                print("Select a Valid Column Name")
        connect_selection(sort_algo)

def connect_selection(algo):
        # df = pd.read_csv(file_path)
        # df = df.sort_values(by=[column])
        # df.to_csv(file_path, index=False)
        # manual_load(ui.table)
        if algo == "Bubble Sort":
                array = [5, 1, 4, 2, 8, 9, 3, 7, 6]
                bubble_sort(array)
                print(array)

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
