import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget,  QLineEdit, QPushButton, QHBoxLayout, QGridLayout

from sound_functions import *

class MainMenu(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.interface()

    def interface(self):
        self.resize(400, 400)
        
        
        
        button_maciej = QPushButton('Maciej', self)
        button_dawid = QPushButton('Dawid', self)
        layout = QGridLayout()
        
        layout.addWidget(button_maciej, 1, 0)
        layout.addWidget(button_dawid, 1, 1)
        
        self.setLayout(layout)
        self.setWindowTitle('Analiza dźwięku')
        self.setWindowIcon(QIcon('./pngs/analyze-sound-wave.png'))
        self.show()


# class PlotWindow(QtWidgets, QMainWindow):

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    sys.exit(app.exec_())