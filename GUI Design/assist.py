# This is an affilated file Form.py 
# This implement the functional logic of the GUI

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QFileDialog
import csv
from algoritms import *
import pandas as pd

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

def manual_load(table, path):
        table.setRowCount(0)
        with open(path, "r", newline="") as csv_file:
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
        sort_algo = ui.sortSelect.currentText()
        column = ui.columnSelect.currentText()
        ui.searchSelect.setCurrentIndex(0)
        # try:
        df = pd.read_csv('data.csv')
        # df = df.sort_values(by=[column])
        name = df['Name'].values.tolist()
        data = list(csv.reader(open('data.csv')))[1:]
        #insertion_sort(name)
        data = insertion_sort(data,0)
        sorted_Data =pd.DataFrame(data)
        sorted_Data.to_csv("reference2.csv", index=False)
        sorted_df = pd.DataFrame({'Name': name})
        df = df.merge(sorted_df, on='Name')
        df.to_csv("reference.csv", index=False)
        manual_load(ui.dataGridView, "reference2.csv")
        # except:
                # print("Select a Valid Column Name")
        connect_selection(sort_algo)

def search_clicked(ui):
        import time
        ui.sortSelect.setCurrentIndex(0)
        ui.orderSelect.setCurrentIndex(0)

        column = ui.columnSelect.currentText()

        if ui.searchBar.toPlainText() == "Search...":
                ui.commentBox.setText("Enter a Valid Search Query")
        elif ui.columnSelect.currentText() == "Select a Column":
                ui.commentBox.setText("Enter a Valid Column Name")
        else:
                search_query = ui.searchBar.toPlainText()
                ui.searchBar.setPlainText("Search...")
                df = pd.read_csv('data.csv')
                name = df[column].values.tolist()
                ui.commentBox.setText(str(len(name)))
                time.sleep(1000)
                x = -1
                x = binary_search(name, 0, len(name)-1, search_query)
                if x != -1:
                        ui.commentBox.setText(name[x] + " Found" + " on index " + str(x))
                else:
                        ui.commentBox.setText("Not Found")

def connect_selection(algo):
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
