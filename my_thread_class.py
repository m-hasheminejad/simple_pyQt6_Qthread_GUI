from PyQt6.QtCore import pyqtSignal, pyqtSlot, QThread
from time import sleep


class WorkerThread(QThread):
    change_status_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.input_variable = 'Empty'
        self._run_flag = False

    def run(self):
        # Place your code here
        # send data to the main window
        self.change_status_signal.emit('Message from thread: Thread started!')
        self.change_status_signal.emit('Message from thread: my variable is: '+self.input_variable)
        while self._run_flag:
            sleep(.5)
        self.change_status_signal.emit('Message from thread: Thread stopped!')

    def start_thread(self):
        self._run_flag = True

    def stop_thread(self):
        self._run_flag = False

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

    @pyqtSlot(str)
    def set_input_variable(self, recieved_variable):
        self.input_variable = recieved_variable

