import os
from PyQt6.QtWidgets import __file__ as qt6_file
dirname = os.path.dirname(qt6_file)
plugin_path = os.path.join(dirname, 'Qt6', 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


from PyQt6.QtWidgets import QWidget,QApplication
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QBrush, QPainter,QPalette
import win32gui
import sys

class wa(QWidget):
	def __init__(s,parent=None):
		super().__init__(parent)
		s.winid_桌面=0
		s.ps=QApplication.primaryScreen()
		s.timer=QTimer(s)
		s.timer.setTimerType(Qt.TimerType.PreciseTimer)
		s.timer.setInterval(int(1000/30))
		s.timer.timeout.connect(s.update)



	
	def paintEvent(s,e):
		painter=QPainter(s)
		if not s.winid_桌面:
			s.winid_桌面=win32gui.FindWindow("Progman","Program Manager")
		painter.drawPixmap(0,0,s.ps.grabWindow(0x10124))
		painter.end()

if __name__=='__main__':
	app=QApplication(sys.argv)
	w=wa()
	w.show()
	w.timer.start()
	sys.exit(app.exec())
