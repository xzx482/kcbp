import os
from PyQt6.QtWidgets import  __file__ as qt6_file
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
		s.b1=QGridLayout()
		s.setLayout(s.b1)
		s.b1.addWidget(QLabel('12345'))
		s.resize(400, 300)
		s.setWindowTitle('w1')
		s.label=QLabel(s)
		s.label2=QLabel(s)
		s.label.setPixmap(QPixmap('icon.png'))
		s.label2.setText('123')
		s.show()
		s.opacity=QGraphicsOpacityEffect()
		s.动画=QPropertyAnimation(s.opacity,b'opacity')
		s.动画.setDuration(1000)
		s.动画.setStartValue(0.01)
		s.动画.setEndValue(0.9999)
		s.label.setGraphicsEffect(s.opacity)
		#s.label2.setGraphicsEffect(s.opacity)
		
	def a(s):
		s.s1.emit()
		


class wi2(QWidget):
	def __init__(s,cw):
		super().__init__()

		w=QWidget(s)
		
		s.setWindowTitle('w2')
		s.cw=cw

	def paintEvent(s,e):
		painter=QPainter(s)
		s.cw.render(painter)
		painter.end()


if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	ex.s1.connect(lambda:print('1'))
	ex.s1.connect(lambda:print('2'))
	ex.s1.connect(lambda:print('3'))
	ex.show()
	ex.a()
	ex.动画.start()
	#ex.initUI()
	#w2=wi2(ex)
	#w2.show()
	sys.exit(app.exec())