import matplotlib.pyplot as plt
from model.Lines import Lines
from PyQt5.QtCore import pyqtSlot

class Rasterization:
    def __init__(self, painter):
        self.ddaLine = Lines(self.DDA)
        self.bresenhamLine = Lines(self.Bresenham)
        self.painter = painter

    @pyqtSlot()
    def DDA(self, x0, x1, y0, y1):
        dx = x1-x0
        dy = y1-y0
        x = x0
        y = y0

        numSteps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

        xIncr = (dx)/numSteps if numSteps > 0 else 0
        yIncr = (dy)/numSteps if numSteps > 0 else 0

        for _ in numSteps:
            x+=xIncr
            y+=yIncr
            print("Point x: ", x, "point y: ", y)