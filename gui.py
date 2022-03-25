import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


from sound_functions import *

class MainMenu(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.interface()

    def interface(self):
        self.resize(300, 300)
        self.setWindowTitle('Analiza dźwięku')
        self.show()


# class PlotWindow(QtWidgets, QMainWindow):

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    sys.exit(app.exec_())