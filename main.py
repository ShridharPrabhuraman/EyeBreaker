from trial import process
# The three imports here are non-used : they were hidden and pyinstaller could not identify them 
import scipy
import sklearn
import sklearn.utils._weight_vector
from PyQt5 import QtWidgets
from gui_main import Ui_MainWindow
import sys
# use main.py to also link GUI with the main file

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_6.clicked.connect(process)
        self.ui.pushButton_4.clicked.connect(self.close)
    
    def run_clicked(self):
        self.tabWidget.setCurrentIndex(1)
        process()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()