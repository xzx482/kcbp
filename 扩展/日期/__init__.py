

import time
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QStyle, QVBoxLayout, QWidget


from .获取节假日 import 获取节假日,节假日_文本
from . import 日期


class 单日期组件(QWidget):
	def __init__(s):
		super().__init__()

		s.根纵=QVBoxLayout()
		s.根纵.setSpacing(0)
		s.setLayout(s.根纵)

		s.根纵_上=QHBoxLayout()
		s.根纵_上.setSpacing(0)

		s.左上=QLabel()
		#s.左上.setStyleSheet('line-height:0px')
		s.左上.setFont(QFont("黑体",16))
		s.根纵_上.addWidget(s.左上)

		s.根纵_上.addSpacing(2)

		s.右上=QLabel()
		s.右上.setFont(QFont("黑体",16))
		s.根纵_上.addWidget(s.右上)
		
		s.根纵.addLayout(s.根纵_上)

		s.根纵_中=QHBoxLayout()
		s.根纵_中.addStretch(1)
		s.日期=QLabel()
		s.日期.setFont(QFont("黑体",22))
		s.根纵_中.addWidget(s.日期)
		s.根纵_中.addStretch(1)
		s.根纵.addLayout(s.根纵_中)

		s.底部=QLabel()
		s.底部.setMinimumWidth(50)
		s.底部.setAlignment(Qt.AlignmentFlag.AlignCenter)
		s.底部.setFont(QFont("黑体",14))
		s.根纵.addWidget(s.底部)


	def 设置内容(s,左上,右上,日期,底部):
		s.左上.setText(左上)
		s.右上.setText(右上)
		s.日期.setText(日期)
		s.底部.setText(底部)



class 日历组件(QWidget):
	gxrq_signal=pyqtSignal(dict)
	def __init__(s,*a):
		super().__init__(*a)
		#s.setVisible(False)
		s.根网=QGridLayout()
		s.根网.setVerticalSpacing(0)
		s.根网.setHorizontalSpacing(10)
		s.setLayout(s.根网)
		s.日期j={}
		s.日期_qws=[]
		for i in range(7):
			星期_顶=QLabel()
			星期_顶.setAlignment(Qt.AlignmentFlag.AlignCenter)
			星期_顶.setText(日期.星期_文本[i])
			星期_顶.setFont(QFont("黑体",16))
			s.根网.addWidget(星期_顶,0,i)
		for x in range(1,3):
			日期_qws1=[]
			for y in range(7):
				单日期=单日期组件()
				s.根网.addWidget(单日期,x,y)
				日期_qws1.append(单日期)
			s.日期_qws.append(日期_qws1)
	def gxrq(s,*a):
		s.更新日期(*a)
	def 更新日期(s,tl=None):
		if not tl:
			tl=time.localtime()
		d=日期.日期(tl=tl)
		
		日期j={'tl':tl,'今天':d.复制(),'星期':[]}
		#raise
		今天=d.公历_数字
		节假日=获取节假日()
		for i in s.日期_qws:
			星期历=日期.星期历(d)#参数 d 在调用后会被改变
			日期j['星期'].append(星期历)
			for i2 in range(7):
				单日期:单日期组件=i[i2]
				日期_:日期.日期=星期历[i2]
				年,月,日=日期_.公历_值
				左上=(str(月)+'月') if 日==1 else ''
				try:
					右上=节假日_文本[ 节假日[str(年)][str(月)][str(日)] ]
					
				except KeyError:
					右上=''
				单日期.设置内容(左上,右上,str(日),日期_.简日())
				if 今天==日期_.公历_数字:#当前的日期外加边框
					单日期.日期.setStyleSheet('border:2px solid #ffffffff')
				else:
					单日期.日期.setStyleSheet('border:2px solid #00ffffff')
					if 今天>日期_.公历_数字:#之前的日期变灰
						单日期.setStyleSheet('color:#aaffffff')
					else:
						单日期.setStyleSheet('color:#ffffffff')

		s.日期j=日期j
		s.gxrq_signal.emit(日期j)
	
	def xsztbh(s,显示状态):
		if 显示状态:
			s.setVisible(True)
		else:
			s.setVisible(False)


def 配置(p,配置l):

	日历=日历组件()
	p.日历=日历
	p.根纵_上横_左纵.addWidget(日历)
	p.添加淡化组件(日历,0.5)
	p.线程.gxrq.connect(日历.gxrq)
	#p.zjxsztbh.connect(日历.xsztbh)