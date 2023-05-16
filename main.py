from my_thread_class import WorkerThread
from ui_window import Ui_MainWindow
from PyQt6.QtCore import pyqtSlot, pyqtSignal
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QObject

class main_class(QObject):
    output_signal = pyqtSignal(str)
    def setup_class(self):
        self.App = QApplication(sys.argv)
        self.ui = Ui_MainWindow()
        self.mainWindow = QMainWindow()

        self.ui.setupUi(self.mainWindow)
        self.mainWindow.setWindowTitle('QThread test app!')
        self.workerThread = WorkerThread()
        self.workerThread.change_status_signal.connect(self.set_status)
        self.output_signal.connect(self.workerThread.set_input_variable)
        self.ui.start_btn.clicked.connect(self.process_start)
        self.ui.stop_btn.clicked.connect(self.process_stop)
        self.mainWindow.show()
        sys.exit(self.App.exec())

    @pyqtSlot(str)
    def set_status(self, status_text):
        self.ui.plainTextEdit.appendPlainText(status_text)

    def process_start(self):
        self.output_signal.emit(self.ui.lineEdit.text())
        self.workerThread.start_thread()
        self.workerThread.start()
        self.ui.start_btn.setEnabled(False)
        self.ui.stop_btn.setEnabled(True)

    def process_stop(self):
        self.workerThread.stop_thread()
        self.workerThread.stop()
        self.ui.start_btn.setEnabled(True)
        self.ui.stop_btn.setEnabled(False)

if __name__ == "__main__":

    a = main_class()
    a.setup_class()