from os import scandir
import sys
from tkinter.font import BOLD
import unicodedata
from pip import main

import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


from sound_functions import *
from conf import *

class MainMenu(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.interface()

    def interface(self):
        self.resize(size, size)
        
        title = QLabel('Projekt 1', self)
        title.setFont(QFont('Peyo', 30))
        title.setAlignment(QtCore.Qt.AlignCenter)

        info_button = QLabel('Kliknij imię osoby, której nagrania chcesz przeanalizować', self)
        info_button.setFont(QFont('Arial', 15))
        info_button.setAlignment(QtCore.Qt.AlignCenter)

        button_maciej = QPushButton('Maciej', self)
        button_maciej.setFont(QFont('Arial', 10))
        button_dawid = QPushButton('Dawid', self)
        button_dawid.setFont(QFont('Arial', 10))
        button_maciej.clicked.connect(self.on_button_clicked_maciej)
        button_dawid.clicked.connect(self.on_button_clicked_dawid)


        button_layout = QGridLayout()
        button_layout.addWidget(button_maciej, 0, 0, alignment=QtCore.Qt.AlignTop)
        button_layout.addWidget(button_dawid, 0, 1, alignment=QtCore.Qt.AlignTop)

        button_exit = QPushButton('Exit', self)
        button_exit.clicked.connect(app.exit)
        exit_layout = QHBoxLayout()
        exit_layout.addStretch(7)
        exit_layout.addWidget(button_exit)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title, alignment=QtCore.Qt.AlignBottom)
        main_layout.addWidget(info_button, alignment=QtCore.Qt.AlignBottom)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(exit_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('Analiza dźwięku')
        self.setWindowIcon(QIcon('./pngs/analyze-sound-wave.png'))
        self.show()

    def on_button_clicked_maciej(self):
        self.dialog = PlotMenu('Maciej')
        self.close()
        self.dialog.show()
    
    def on_button_clicked_dawid(self):
        self.dialog = PlotMenu('Dawid')
        self.close()
        self.dialog.show()
        

class PlotMenu(QWidget):
    def __init__(self, imie = 'Maciej', parent = None): 
        super().__init__(parent)
        self.imie = imie

        self.resize(size, size)

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.tabs = QTabWidget()

        self.plot()
        self.features()

        self.layout.addWidget(self.tabs)

        self.setWindowTitle('Analiza dźwięku')
        self.setWindowIcon(QIcon('./pngs/analyze-sound-wave.png'))
        self.show()

    def plot(self):
        
        self.choose_file = QComboBox()
        if self.imie == 'Maciej':
            self.choose_file.addItems(all_filenames_m)
        if self.imie == 'Dawid':
            self.choose_file.addItems(all_filenames_d)
        
        button_back = QPushButton('Back', self)
        button_back.clicked.connect(self.go_back)
        self.back_layout = QHBoxLayout()

        self.back_layout.addWidget(self.choose_file)
        self.back_layout.addStretch(6)
        self.back_layout.addWidget(button_back)

        self.main_plot = QWidget()
        self.main_plot_layout = QGridLayout()
        self.sc, self.toolbar = self.waveform(str(self.choose_file.currentText()))
        self.main_plot_layout.addWidget(self.toolbar, 0, 0)
        self.main_plot_layout.addWidget(self.sc, 1, 0)
        self.main_plot_layout.addLayout(self.back_layout, 2, 0)

        self.choose_file.activated.connect(self.generate_plots_statistics)
        
        self.main_plot.setLayout(self.main_plot_layout)
        self.tabs.addTab(self.main_plot, 'Waveform')
    
    def features(self):

        def _label_element(text, function, filename):
            widget = QWidget()
            layout = QVBoxLayout()

            label = QLabel()
            label.setText(text)
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setFont(QFont('Arial', 12, weight=100))

            output = QLabel()
            output.setText(str(function(filename, self.imie)))
            output.setAlignment(QtCore.Qt.AlignCenter)
            output.setFont(QFont('Arial', 8))

            layout.addWidget(label, alignment=QtCore.Qt.AlignBottom)
            layout.addWidget(output, alignment=QtCore.Qt.AlignTop)

            widget.setLayout(layout)

            return widget
        
        self.main_features = QWidget()
        self.main_features_layout = QGridLayout()

        self.main_features_layout.addWidget()
        self.main_features_layout.addWidget(_label_element('Volume', volume, self.choose_file.currentText()), 1, 0)
        self.main_features_layout.addWidget(_label_element('Energy', energy, self.choose_file.currentText()), 1, 1)

        self.main_features.setLayout(self.main_features_layout)
        self.tabs.addTab(self.main_features, 'Features')
    


    def generate_plots_statistics(self, _):
        filename = str(self.choose_file.currentText())
        self.main_plot_layout.removeWidget(self.sc)
        self.main_plot_layout.removeWidget(self.toolbar)

        self.sc, self.toolbar = self.waveform(filename)
        self.main_plot_layout.addWidget(self.toolbar, 0, 0)
        self.main_plot_layout.addWidget(self.sc, 1, 0)
        
        
        self.main_plot.setLayout(self.main_plot_layout)
        self.tabs.removeTab(1)
        self.tabs.removeTab(0)
        self.tabs.addTab(self.main_plot, 'Waveform')
        self.tabs.addTab(self.main_features, 'Features')


    def waveform(self, filename):
        samplerate , data = read_wav(filename, self.imie)
        length = len(data) / samplerate
        time = np.linspace(0., length, data.shape[0])
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot(time, data)

        toolbar = NavigationToolbar(sc, self)

        return sc, toolbar

    def go_back(self):
        self.back = MainMenu()
        self.close()
        self.back.show()

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    sys.exit(app.exec_())