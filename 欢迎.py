from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QCheckBox,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5 import QtCore
import sys
from flj import flj



配置={
	'视频背景':{
		'启用':True,
		'项':0
	},
	'课程表':{
		'启用':True,
		'时差':0,
		'周六时间':None
	},
	'天气':{
		'启用':True,
		'经度':0,
		'纬度':0,
		'key':''
	}
	
}

class 主窗口(QWidget):
	def __init__(s,parent=None):
		super().__init__(parent)
		s.l=None
		s.ln=0
		s.resize(400,300)
		s.setWindowTitle('欢迎')
		s.vl=QVBoxLayout()
		s.流程_子窗口_布局=QVBoxLayout()
		s.vl.addLayout(s.流程_子窗口_布局)
		s.vl.addStretch(1)
		
		s.hl=QHBoxLayout()
		s.hl.addStretch(1)
		s.上一步_按钮=QPushButton('上一步')
		s.上一步_按钮.clicked.connect(s.syb)
		s.上一步_按钮.setEnabled(False)
		s.hl.addWidget(s.上一步_按钮)

		s.下一步_按钮=QPushButton('开始')
		s.下一步_按钮.clicked.connect(s.xyb)
		s.hl.addWidget(s.下一步_按钮)
		s.vl.addLayout(s.hl)

		s.setLayout(s.vl)
	
	def 设置流程(s,l):
		s.l=[]
		for i in l:
			单流程=i()
			单流程.setVisible(False)
			s.l.append(单流程)
			s.流程_子窗口_布局.addWidget(单流程)
		s.llen=len(s.l)
		s.ln=0
		s.ln_old=0
		s.l[0].setVisible(True)

	def syb(s):
		s.更新页面(-1)
	
	def xyb(s):
		s.更新页面(1)
		
		
	def 更新页面(s,加页=None):
		if not 加页:
			加页=s.ln-s.ln_old
		s.l[s.ln].setVisible(False)
		s.ln_old=s.ln=s.ln+加页
		if s.ln==s.llen:
			for i in s.l:
				if hasattr(i,'更新配置'):
					i.更新配置()
			s.上一步_按钮.setEnabled(False)
			s.结束()
			return
		s.l[s.ln].setVisible(True)
		
		if s.ln==s.llen-1:
			s.下一步_按钮.setText('完成')
		else:
			s.下一步_按钮.setText('下一步')
		
		if s.ln==1:
			s.上一步_按钮.setEnabled(False)
		else:
			s.上一步_按钮.setEnabled(True)

	def 结束(s):
		print(配置)
		配置l=flj('配置.json')
		if 配置l.d:
			配置l.重写()
		配置l.d=配置
		配置l.关闭()
		s.close()


class 欢迎(QWidget):
	def __init__(s):
		super().__init__()
		s.setWindowTitle('欢迎')
		s.vl=QVBoxLayout()
		s.标题=QLabel('<h1>欢迎</h1>')
		s.标题.setAlignment(QtCore.Qt.AlignCenter)
		s.vl.addWidget(s.标题)
		s.vl.addStretch(1)
		s.setLayout(s.vl)
	
	
class 设置课程表(QWidget):
	def __init__(s):
		super().__init__()
		s.vl=QVBoxLayout()
		s.标题=QLabel('<h1>设置课程表</h1>')
		s.标题.setAlignment(QtCore.Qt.AlignCenter)
		s.vl.addWidget(s.标题)
		s.提示=QLabel(
			'将在所有时间显示, 包括时间和课程'
		)
		s.vl.addWidget(s.提示)
		s.启用按钮=QCheckBox('启用课程表')
		s.启用按钮.setChecked(True)
		s.vl.addWidget(s.启用按钮)
		s.vl.addStretch(1)
		s.setLayout(s.vl)

	def 更新配置(s):
		配置['课程表']['启用']=s.启用按钮.isChecked()

class 设置天气(QWidget):
	def __init__(s):
		super().__init__()
		s.vl=QVBoxLayout()
		s.标题=QLabel('<h1>设置天气</h1>')
		s.标题.setAlignment(QtCore.Qt.AlignCenter)
		s.vl.addWidget(s.标题)
		s.提示=QLabel(
			'仅在下课时启用, 在桌面背景右侧显示天气<br/>'
		)
		s.vl.addWidget(s.提示)
		s.启用按钮=QCheckBox('启用天气')
		s.启用按钮.setChecked(True)
		s.vl.addWidget(s.启用按钮)
		
		s.经纬度_布局=QHBoxLayout()

		s.经纬度_布局.addWidget(QLabel('经度'))
		s.经度_文本框=QLineEdit()
		s.经度_文本框.setPlaceholderText('经度')
		#s.经度_文本框.setEnabled(False)
		s.经纬度_布局.addWidget(s.经度_文本框)

		s.经纬度_布局.addWidget(QLabel('  '))

		s.经纬度_布局.addWidget(QLabel('纬度'))
		s.纬度_文本框=QLineEdit()
		s.纬度_文本框.setPlaceholderText('纬度')
		#s.纬度_文本框.setEnabled(False)
		s.经纬度_布局.addWidget(s.纬度_文本框)
		s.经纬度_布局.addStretch(1)
		s.vl.addLayout(s.经纬度_布局)
		s.vl.addWidget(QLabel('  '))

		提示=QLabel(
			'<p>'
			'需要到<a href="https://home.openweathermap.org/">https://home.openweathermap.org/</a>获取appid<br/>'
			'可自行搜索 "<a href="https://cn.bing.com/search?q=openweathermap+%E8%8E%B7%E5%8F%96API+key">openweathermap 获取API key</a>"<br/>'
			'这是免费的, 只是过程有一些复杂'
			'</p>'
		)
		提示.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse|QtCore.Qt.LinksAccessibleByMouse)
		#提示.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
		提示.setOpenExternalLinks(True)
		s.vl.addWidget(提示)
		s.id_文本框=QLineEdit()
		s.id_文本框.setPlaceholderText('id')
		#s.id_文本框.setEnabled(False)
		s.vl.addWidget(s.id_文本框)

		s.vl.addStretch(1)
		s.setLayout(s.vl)

	def 更新配置(s):
		配置['天气']['启用']=s.启用按钮.isChecked()
		配置['天气']['经度']=s.经度_文本框.text()
		配置['天气']['纬度']=s.纬度_文本框.text()
		配置['天气']['key']=s.id_文本框.text()

class 设置背景(QWidget):
	def __init__(s):
		super().__init__()
		s.vl=QVBoxLayout()
		s.标题=QLabel('<h1>设置花哨的背景</h1>')
		s.标题.setAlignment(QtCore.Qt.AlignCenter)
		s.vl.addWidget(s.标题)
		s.提示=QLabel(
			'仅在下课时启用, 让桌面背景更加与众不同, 背景一般都是景观<br/>'
			'背景来源于Microsoft Edge的新标签页背景, 仅供个人使用'
		)
		s.vl.addWidget(s.提示)
		s.启用按钮=QCheckBox('启用花哨的背景')
		s.启用按钮.setChecked(False)
		s.vl.addWidget(s.启用按钮)
		s.vl.addStretch(1)
		s.setLayout(s.vl)

	def 更新配置(s):
		配置['视频背景']['启用']=s.启用按钮.isChecked()

class 完成(QWidget):
	def __init__(s):
		super().__init__()
		s.vl=QVBoxLayout()
		s.标题=QLabel('<h1>已就绪</h1>')
		s.标题.setAlignment(QtCore.Qt.AlignCenter)
		s.vl.addWidget(s.标题)
		提示=QLabel(
			'设置完成, 再次打开主程序即可使用'
		)
		s.vl.addWidget(提示)
		s.vl.addStretch(1)
		s.setLayout(s.vl)


def 欢迎窗口():
	app=QApplication(sys.argv)

	翻译=QtCore.QTranslator()
	翻译.load("zh_CN")
	__app=QApplication.instance()
	__app.installTranslator(翻译)

	w=主窗口()
	w.设置流程(l=[欢迎,设置课程表,设置天气,设置背景,完成])
	w.show()
	
	sys.exit(app.exec_())

if __name__=='__main__':
	欢迎窗口()
