from PyQt5.QtWidgets import QAction

class TransformActions(QAction):
    def __init__(self, func, parent, text='', checkable=False, icon=None):
        super().__init__(text, parent)
        self.triggered.connect(func)
        self.setCheckable(checkable)

        if icon != None:
            self.setIcon(icon)