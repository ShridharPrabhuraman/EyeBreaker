from trial import process,process_kill
import threading

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
        # self.ui.pushButton_6.clicked.connect(lambda: process(int(self.ui.textEdit.toPlainText()), int(self.ui.textEdit_2.toPlainText()), int(self.ui.textEdit_3.toPlainText())))
        self.ui.pushButton_6.clicked.connect(self.start_process)
        self.ui.pushButton_4.clicked.connect(self.stop_process)

    def stop_process(self):
        process_kill()
        self.x.join()
        print('Stopped')


    def start_process(self):
        try:
            self.x = threading.Thread(target=process, args=(int(self.ui.textEdit.toPlainText()), int(self.ui.textEdit_2.toPlainText()), int(self.ui.textEdit_3.toPlainText())))
            self.x.start()
        except:
            print("Threading failed")



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()