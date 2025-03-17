import sys
from PyQt5.QtWidgets import QApplication
from gui.MainWindow import MainWindow 

if __name__ == '__main__':
    """ Inicializa a aplicação, criando a janela principal. """

    app = QApplication(sys.argv)
    winwdow = MainWindow()
    sys.exit(app.exec_())