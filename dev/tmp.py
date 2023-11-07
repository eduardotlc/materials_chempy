import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QInputDialog, QMessageBox, QComboBox, QTextEdit
from PyQt5.QtCore import Qt
import materials_chempy.database_analysis.dban_functions as dbanfunc

class InteractiveWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.button1 = QPushButton("Bar plotting from csv")
        self.button1.clicked.connect(self.execute_function1)
        self.button1.setStyleSheet("background-color: lightblue;")  # Set button background color
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Show options")
        self.button2.clicked.connect(self.show_options)
        self.button2.setStyleSheet("background-color: lightblue;")  # Set button background color
        self.layout.addWidget(self.button2)

        self.button3 = QPushButton("Option 3: Execute Function 3")
        self.button3.clicked.connect(self.execute_function3)
        self.button3.setStyleSheet("background-color: lightblue;")  # Set button background color
        self.layout.addWidget(self.button3)

        self.view_button = QPushButton("Visualize csv Dataframe")
        self.view_button.clicked.connect(self.view_csv_as_dataframe)
        self.view_button.setStyleSheet("background-color: lightblue;")  # Set button background color
        self.layout.addWidget(self.view_button)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["Month", "Year", "Day"])
        self.combo_box.hide()
        self.layout.addWidget(self.combo_box)

        self.text_edit = QTextEdit()
        self.text_edit.hide()
        self.layout.addWidget(self.text_edit)

        self.setLayout(self.layout)
        self.setWindowTitle('Interactive Widget')
        self.setStyleSheet("background-color: lightgray;")  # Set widget background color to light gray
        self.resize(800, 600)

    def show_options(self):
        self.button2.hide()
        self.button3.hide()
        self.combo_box.show()

    def hide_options(self):
        self.combo_box.hide()
        self.button2.show()

    def execute_function1(self):
        column_name = self.combo_box.currentText()
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select a CSV file', '', 'CSV Files (*.csv);;All Files (*)', options=options)
        if file_path:
            df = pd.read_csv(file_path)
            df = dbanfunc.clean_df(df)
            if not df.empty and column_name in df.columns:
                plt.bar(df[column_name], df['Articles'])
                plt.xlabel(column_name)
                plt.ylabel('Articles')
                plt.title(f'Bar Plot from CSV Data by {column_name}')
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                plt.show()
                self.hide_options()  # Hide the options after the plot is displayed
            else:
                QMessageBox.warning(self, 'Error', f'Invalid column selection: {column_name}')

    def view_csv_as_dataframe(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select a CSV file', '', 'CSV Files (*.csv);;All Files (*)', options=options)
        if file_path:
            df = pd.read_csv(file_path)
            self.text_edit.setPlainText(df.to_string(index=False))
            self.text_edit.show()

    def execute_function3(self):
        text, ok = QInputDialog.getText(self, 'Input', 'Enter another parameter:')
        if ok:
            file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', text, 'Text Files (*.txt);;All Files (*)')
            if file_name:
                with open(file_name, 'w') as file:
                    file.write(text)
                QMessageBox.information(self, 'Result', f'Function 3 executed and saved data to: {file_name}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InteractiveWidget()
    window.show()
    sys.exit(app.exec_())
