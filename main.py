import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import \
    QApplication, QWidget, QPushButton, \
    QLineEdit, QLabel, QMainWindow, QGridLayout
from GraphBuild import GraphBuilder
from StringValidation import CheckFunctions


#    __         __        _____        __________   __     _
#   |  \       /  |      / / \ \      |___    ___| |  \   | |
#   |   \     /   |     / /   \ \         |  |     |   \  | |
#   | |\ \   / /| |    / /_____\ \        |  |     | |\ \ | |
#   | | \ \_/ / | |   /  _______  \       |  |     | | \ \| |
#   | |  \___/  | |  / /         \ \   ___|  |___  | |  \ | |
#   |_|         |_| /_/           \_\ |__________| |_|   \__|


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.creatWindow()
        self.creatWidgets()
        self.conectWidgets()

    def creatWindow(self):
        self.setWindowTitle("Builder Graphics")
        self.setWindowIcon(QIcon("Images/logoAndreasyanEgorAndreasivich.png"))
        self.setFixedSize(QSize(650, 700))

        self.container = QWidget()
        self.layout = QGridLayout()

    def creatWidgets(self):
        pixmap = QPixmap("Images/Graph_StartError.png")
        self.graph = QLabel()
        self.graph.setPixmap(pixmap)

        self.YLable = QLabel("y = ")
        self.YLable.setFont(QFont('Arial', 14))
        self.YLable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.YLable.setFixedSize(400, 50)

        self.textFaild = QLineEdit()
        fontInput = self.textFaild.font()
        fontInput.setPointSize(14)
        self.textFaild.setFont(fontInput)
        self.textFaild.setFixedSize(200, 50)

        self.button = QPushButton("Build")
        self.button.setFixedSize(100, 50)
        self.button.setCheckable(True)
        self.button.setStyleSheet("text-align:center; font-size: 20px")
        self.button.clicked.connect(self._buildGraph)

    def conectWidgets(self):
        self.layout.addWidget(self.graph, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.YLable, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.textFaild, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.button, 2, 0, alignment=Qt.AlignmentFlag.AlignCenter)

        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def _buildGraph(self):
        arithmetic_example = self.textFaild.text().lower()
        checkFunction = CheckFunctions(arithmetic_example)
        if len(arithmetic_example) > 0 and checkFunction.brackets()\
                and checkFunction.availableSymbols() and checkFunction.placementOfSigns():
            GraphBuilder().buildG(arithmetic_example)
            pixmap = QPixmap("Images/Graph.png")
            self.graph.setPixmap(pixmap)
        else:
            pixmap = QPixmap("Images/Graph_StartError.png")
            self.graph.setPixmap(pixmap)


if __name__ == '__main__':
    application = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(application.exec())
