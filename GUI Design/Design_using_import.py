# This is an affilated file Form.py 
# This implement the functional logic of the GUI

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from functools import partial
import pandas as pd
import time
import csv

from algorithms import *
from All_Algorithms import *

fields = ['Name', 'Brand', 'Ram (GB)', 'Rom (GB)', 'Display (cm)', 'Battery (mAh)', 'Price', 'Website']
algorithms = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Counting Sort', 'Radix Sort', 'Bucket Sort']
df = pd.read_csv('unique.csv')

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        loadUi("smart.ui",self) # Here we imported the QT Designer file which we made as Python GUI FIle.
        
        # Command to remove the default Windows Frame Design.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # Command to make the backgroud of Window transparent.
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        #These 2 lines are used to put funnctions on close and minimize buttons.
        # self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        self.CrossButton.clicked.connect(lambda: self.close())
        
        # # Function to load the previous data of student at the start of program.
        # self.load_table()
        
        # self.loadBtn.clicked.connect(self.tableViewLoad(self, data))
        self.loadBtn.clicked.connect(partial(self.tableViewLoad, df))
        self.sortBtn.clicked.connect(self.sort_clicked)
        self.searchBtn.clicked.connect(self.search_clicked)
        self.sortSelect.activated.connect(self.update_Column_Options)

    def update_Column_Options(self):
        index = self.sortSelect.currentIndex()
        if index == 8 or index == 6 or index == 7:
            self.set_column_options()
        else:
            self.reset_column_options()

    def set_column_options(self):
        self.columnSelect.clear()
        if self.sortSelect.currentIndex() == 8:
            self.columnSelect.addItems(["---Select a Column---", "Ram (GB)", "Rom (GB)", "Display (cm)", "Battery (mAh)"])
        else:
            self.columnSelect.addItems(["---Select a Column---", "Ram (GB)", "Rom (GB)", "Battery (mAh)"])
        self.orderSelect.clear()
        self.orderSelect.addItems(["---Select a Type---", "Single Column"])

    def reset_column_options(self):
        self.columnSelect.clear()
        self.columnSelect.addItems(["---Select a Column---", "Name", "Brand", "Ram (GB)", "Rom (GB)", "Display (cm)", "Battery (mAh)", "Price", "Website"])
        self.orderSelect.clear()
        self.orderSelect.addItems(["---Select a Type---", "Single Column", "Whole Data"])

    def tableViewLoad(self, data):
        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        try:
            # data = pd.read_csv(path)
            self.model.setRowCount(data.shape[0])
            self.model.setColumnCount(data.shape[1])

            for col, header in enumerate(data.columns):
                header_item = QStandardItem(header)
                self.model.setHorizontalHeaderItem(col, header_item)

            for row in range(data.shape[0]):
                for col in range(data.shape[1]):
                    item = QStandardItem(str(data.iat[row, col]))
                    self.model.setItem(row, col, item)
        except Exception as e:
            print(f"Error loading data: {str(e)}")

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

    def sort_clicked(self):
        if self.columnSelect.currentIndex() != 0 and self.sortSelect.currentIndex() != 0:
            sort_algo = self.sortSelect.currentText()
            algo = algorithms.index(sort_algo)
            column = self.columnSelect.currentText()
            self.searchSelect.setCurrentIndex(0)
            self.commentBox.setText("Sorting the Data...")
            
            column_data = df[column].values.tolist() 
            
            arr2d = fromFrameToArray(df, fields)                       # Converting data frame in 2d array

            # ---------------------  Applying Sorting Algorithms  ---------------------------------------

            start_time = time.time()
            if self.orderSelect.currentIndex() == 0:
                self.commentBox.setText("Select the Type of Sorting")
            else:
                self.commentBox.setText("Sorting Your Data...")
                data = []
                if self.orderSelect.currentIndex() == 1:
                    data = df[column].values.tolist()
                    data = connect_selection_single(algo, data)
                    data = pd.DataFrame({column: data})                           # make a new data frame and show it only

                elif self.orderSelect.currentIndex() == 2:
                    arr2d = connect_selection_2d(algo, arr2d, fields.index(column))         # sorting the 2d array on the basics of provided column which will be row in 2d array
                    data = fromArrayToFrame(arr2d)                                          # Converting 2d array to data frame
                
                end_time = time.time()
                self.timeTaken.setPlainText(str(end_time - start_time))    # Show the time Taken 

            #----------------------------------------------------------------------------------------------

                self.tableViewLoad(data)
                self.commentBox.setText("Data Sorted Successfully")
        else:
            self.commentBox.setText("Select the Valid Queries")

    def search_clicked(self):
        if self.columnSelect.currentIndex() != 0 and self.searchSelect.currentIndex() != 0:
            self.sortSelect.setCurrentIndex(2)
            self.sort_clicked()
            self.sortSelect.setCurrentIndex(0)
            self.orderSelect.setCurrentIndex(0)

            column = self.columnSelect.currentText()

            if self.searchBar.toPlainText() != "Search...":
                search_query = self.searchBar.toPlainText()
                self.searchBar.setPlainText("Search...")
                # df = pd.read_csv('data.csv')
                name = df[column].values.tolist()

                print("Length of 2d Array: ", len(name))
                x = -1
                x = binary_search(name, 0, len(name)-1, search_query)
                if x != -1:
                        self.commentBox.setText("Search Founded Successfully")
                        # self.commentBox.setText(name[x] + " Found" + " on index " + str(x))
                else:
                        self.commentBox.setText("Not Found")
            else:
                self.commentBox.setText("Enter a Valid Text to Search")
        else:
            self.commentBox.setText("Enter a Valid Search Query")

    def button_click_action():
            # This is where you define the code to execute when the button is clicked
            print("Button Clicked")

def connect_selection_2d(algo, data, index):
    if algo == 0:
        data = BubbleSort(data, index)
    elif algo == 1:
        data = InsertionSort(data, index)
    elif algo == 2:
        data = SelectionSort(data, index)
    elif algo == 3:
        data = MergeSort(data, index)
    elif algo == 4:
        data = byQuickSort(data, index)
    else:
        pass
    return data

def connect_selection_single(algo, data):
    if algo == 0:
        data = bubble_sort(data)
    elif algo == 1:
        data = insertion_sort(data)
    elif algo == 2:
        data = selection_sort(data)
    elif algo == 3:
        data = merge_sort(data)
    elif algo == 4:
        data = quick_sort(data, 0, len(data)-1)
    elif algo == 5:
        data = counting_sort(data)
    elif algo == 6:
        data = radix_sort(data)
    elif algo == 7:
        data = bucket_sort_p(data)
    else:
        pass
    return data

def fromArrayToFrame(arr):
    data = {
        'Name': arr[0],
        'Brand': arr[1],
        'Ram (GB)': arr[2],
        'Rom (GB)': arr[3],
        'Display (cm)': arr[4],
        'Battery (mAh)': arr[5],
        'Price': arr[6],
        'Website': arr[7]
    }
    data = pd.DataFrame(data)
    return data

def fromFrameToArray(df, field):
    arr = []
    for i in field:
        arr.append(df[i].values.tolist())
    return arr

def reset_values(self):
    self.searchBar.setPlainText("Search...")
    self.columnSelect.setCurrentIndex(0)
    self.sortSelect.setCurrentIndex(0)
    self.orderSelect.setCurrentIndex(0)
    self.timeTaken.setPlainText("0.0")
    self.commentBox.setText("Let's Enjoy the benefits of Smart Sorter and Have a Bird Eye View...")

def main():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        # MainWindow = QtWidgets.QMainWindow()
        window = Mainwindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()
