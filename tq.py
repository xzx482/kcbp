import os
from PyQt6.QtWidgets import __file__ as qt6_file
dirname = os.path.dirname(qt6_file)
plugin_path = os.path.join(dirname, 'Qt6', 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap,QPainter
from PyQt6.QtCore import Qt
import sys


class Example(QWidget):
	def __init__(s):
		super().__init__()
		s.setWindowTitle('w1')
		s.initUI()

	def initUI(s):
		s.label=QLabel(s)
		s.label.setPixmap(QPixmap('icon.png'))

		s.show()

class wi2(QWidget):
	def __init__(s,cw):
		super().__init__()
		s.setWindowTitle('w2')
		s.cw=cw

	def paintEvent(s,e):
		painter=QPainter(s)
		s.cw.render(painter)
		painter.end()


if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	ex.initUI()
	w2=wi2(ex)
	w2.show()
	sys.exit(app.exec())