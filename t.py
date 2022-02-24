from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget,QLabel,QLayout,QApplication
from PyQt6.QtCore import Qt
import sys

app=QApplication(sys.argv)

w=QWidget()
lab=QLabel(w)
lab.setFont(QFont("黑体",16))
lab.setText("Hello World")
w.show()
sys.exit(app.exec())