from math import sqrt
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QWidget, QPushButton, qApp, QDesktopWidget, QLabel, QActionGroup, QVBoxLayout)
from PyQt5.QtGui import QIcon, QColor, QPainter, QPen, QPalette, QFont, QImage
from PyQt5.QtCore import Qt, QPoint
from gui.TransformActions import TransformActions
from algorithms.Rasterization import Rasterization

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.points = []
        
        # Atalho definido para a ação de fechar o programa
        exitAct = TransformActions(qApp.quit, self)
        exitAct.setShortcut('Ctrl+C')
        self.addAction(exitAct)
    
    def center(self):
        """ Centraliza a UI na tela do usuário """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        """ Inicializa todos os widgets relacionados a janela
        principal do programa.
        """
        self.setWindowTitle('MyPaint')
        self.setWindowIcon(QIcon("paint.png"))
        # self.createMenuBar()
        self.createCanvas()
        self.center()
        self.show()
    
    def createCanvas(self):
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.red)
        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.lastPoint = QPoint()
        self.update()
    
    def paintEvent(self, event):
        """ Overrides paintEvent to draw the QImage. """
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
    
    def createMenuBar(self):
        """ Cria o menu superior, adicionando os devidos
        submenus e suas respectivas ações.
        """

        self.menubar = self.menuBar()
        self.createLineMenu(self.menubar)
        self.createCuttingMenu(self.menubar)
        self.createFillingMenu(self.menubar)
        self.createTransformingMenu(self.menubar)
    
    def createLineMenu(self, menu):
        submenu = menu.addMenu('Retas')
        group  = QActionGroup(submenu)
        
        action = TransformActions(lambda: self.lines.setFn(Rasterization.DDA) , group, 'DDA', True)
        submenu.addAction(action)
        
        action = TransformActions(lambda: self.lines.setFn(self.draw_something),
                           group, 'Bresenham', True)

        action.setChecked(True)
        submenu.addAction(action)

    def createCuttingMenu(self, menu):
        submenu = menu.addMenu('Recortes')
        group  = QActionGroup(submenu)

        action = TransformActions(lambda: self.lines.setFn(self.draw_something),
                           group, 'Recorte X', True)
        action.setChecked(True)
        submenu.addAction(action)

        action = TransformActions(lambda: self.lines.setFn(self.draw_something) , group, 'Recorte Y', True)
        submenu.addAction(action)

    def createFillingMenu(self, menu):
        submenu = menu.addMenu('Preenchimento')
        group  = QActionGroup(submenu)

        action = TransformActions(lambda: self.lines.setFn(self.draw_something),
                           group, 'Preenchimento X', True)
        action.setChecked(True)
        submenu.addAction(action)

        action = TransformActions(lambda: self.lines.setFn(self.draw_something) , group, 'Preenchimento Y', True)
        submenu.addAction(action)
    
    def createTransformingMenu(self, menu):
        submenu = menu.addMenu('Transformações Geométricas')
        group  = QActionGroup(submenu)

        action = TransformActions(lambda: self.lines.setFn(self.draw_something),
                           group, 'Transformação X', True)
        action.setChecked(True)
        submenu.addAction(action)

        action = TransformActions(lambda: self.lines.setFn(self.draw_something) , group, 'Transformação Y', True)
        submenu.addAction(action)
