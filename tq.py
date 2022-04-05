import os
from PyQt6.QtWidgets import  QHBoxLayout, QPushButton, __file__ as qt6_file
dirname = os.path.dirname(qt6_file)
plugin_path = os.path.join(dirname, 'Qt6', 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QGraphicsOpacityEffect,QGridLayout
from PyQt6.QtGui import QPixmap,QPainter
from PyQt6.QtCore import QPropertyAnimation, Qt, pyqtSignal
import sys


class Example(QWidget):
	s1=pyqtSignal()
	def __init__(s):
		super().__init__()
		s.bo=QPushButton('按钮')
		s.bo2=QPushButton('按钮')
		s.bo.clicked.connect(lambda:s.hl.removeWidget(ex.bo))
		s.bo2.clicked.connect(lambda:s.bo.move(0,0))
		s.resize(400, 300)
		s.setWindowTitle('w1')
		s.hl=QHBoxLayout()
		s.hl.addWidget(s.bo)
		s.hl.addWidget(s.bo2)
		s.setLayout(s.hl)
		s.l1=QLabel()
		s.hl.addWidget(s.l1)
		s.l1.setText('12345')


if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	ex.show()
	ex.hl.removeWidget(ex.l1)
	#ex.hl.removeWidget(ex.bo)
	ex.l1.setText('1234566')
	ex.l1.move(0,0)
	sys.exit(app.exec())