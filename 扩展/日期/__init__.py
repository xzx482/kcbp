

import time
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QStyle, QVBoxLayout, QWidget


from .获取节假日 import 获取节假日,节假日_文本
from . import 日期
from kcb_basic import 获取字体,缩放


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
		s.左上.setFont(获取字体(16))
		s.左上.setMaximumWidth(缩放(24))
		s.左上.setAlignment(Qt.AlignmentFlag.AlignCenter)
		s.根纵_上.addWidget(s.左上)
		s.根纵_上.addSpacing(缩放(2))

		#这个Label是不在布局中的; 它使用 setGeometry 在 resizeEvent 事件中调整位置
		s.左上中=QLabel(s)
		s.左上中.setText('月')
		s.左上中.setAlignment(Qt.AlignmentFlag.AlignCenter)
		s.左上中.setVisible(False)
		s.左上中.setFont(获取字体(16))
		s.左上中_宽高=(缩放(24),缩放(20),缩放(2)) # 最后一个是上移的高度


		s.右上=QLabel()
		s.右上.setFont(获取字体(16))
		s.右上.setMaximumWidth(缩放(24))
		s.右上.setAlignment(Qt.AlignmentFlag.AlignCenter)
		s.根纵_上.addWidget(s.右上)
		
		s.根纵.addLayout(s.根纵_上)

		s.根纵_中=QHBoxLayout()
		s.根纵_中.addStretch(1)
		s.日期=QLabel()
		s.日期.setFont(获取字体(22))
		s.根纵_中.addWidget(s.日期)
		s.根纵_中.addStretch(1)
		s.根纵.addLayout(s.根纵_中)

		s.底部=QLabel()
		s.底部.setMinimumWidth(缩放(50))
		s.底部.setAlignment(Qt.AlignmentFlag.AlignCenter)
		s.底部.setFont(获取字体(14))
		s.根纵.addWidget(s.底部)


	def 设置内容(s,左上,右上,日期,底部):
		s.左上.setText(左上)
		if 左上:
			s.左上中.setVisible(True)
		else:
			s.左上中.setVisible(False)
		s.右上.setText(右上)
		s.日期.setText(日期)
		s.底部.setText(底部)
	
	def resizeEvent(s,e):
		#将 s.左上中 的位置设置在 s.左上 正下方
		a0=s.左上.geometry()
		s.左上中.setGeometry(a0.x(),a0.y()+a0.height()-s.左上中_宽高[2],s.左上中_宽高[0],s.左上中_宽高[1])




class 日历组件(QWidget):
	gxrq_signal=pyqtSignal(dict)
	def __init__(s,*a):
		super().__init__(*a)
		#s.setVisible(False)
		s.根网=QGridLayout()
		s.根网.setVerticalSpacing(0)
		s.根网.setHorizontalSpacing(缩放(10))
		s.setLayout(s.根网)
		s.日期j={}
		s.日期_qws=[]
		for i in range(7):
			星期_顶=QLabel()
			星期_顶.setAlignment(Qt.AlignmentFlag.AlignCenter)
			星期_顶.setText(日期.星期_文本[i])
			星期_顶.setFont(获取字体(16))
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
				左上=(str(月)) if 日==1 else ''
				try:
					右上=节假日_文本[ 节假日[str(年)][str(月)][str(日)] ]
					
				except KeyError:
					右上=''
				单日期.设置内容(左上,右上,str(日),日期_.简日())
				if 今天==日期_.公历_数字:#当前的日期外加边框
					单日期.日期.setStyleSheet('border:2px solid #ffffffff')
					单日期.左上中.setVisible(False)
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

节气文本={
	'立春':'阳气上升，万物更生，新岁开启',
	'雨水':'降雨开始，雨量渐增',
	'惊蛰':'天气转暖，春雷始鸣',
	'春分':'春季过半，昼夜等长',
	'清明':'天气晴朗、草木繁茂',
	'谷雨':'寒潮天气基本结束，气温回升加快',
	'立夏':'夏季的开始',
	'小满':'雨水之盈',
	'芒种':'耕种忙碌',
	'夏至':'夏季过半，白日最长',
	'小暑':'季夏时节开始',
	'大暑':'一年中最热的时期',
	'立秋':'秋季开始，收获的季节',
	'处暑':'炎热酷暑即将过去',
	'白露':'孟秋的结束，仲秋的开始',
	'秋分':'秋季过半，昼夜等长',
	'寒露':'秋意渐浓，气爽风凉，少雨干燥',
	'霜降':'天气渐冷、初霜出现',
	'立冬':'冬季开始',
	'小雪':'天气渐冷，降水渐增',
	'大雪':'气温骤降,雨量显增',
	'冬至':'冬季过半，夜晚最长',
	'小寒':'气温继续降低',
	'大寒':'气温达到最低'
}

公历节日文本={
	'元旦':''
}

def 日期信息(日期_:日期.日期):
	农节=日期.农历节日(日期_.sx)
	公节=日期.公历节日(日期_.sx)
	if 日期_.sx.hasJieQi():
		节气=日期_.节气()
	else:
		节气=''
	
	...

class 日历消息():
	def __init__(s,p):
		s.p=p
		s.消息=p.主消息.添加消息(1)

	def gxrq(s,日期j):
		...


def 配置(p,配置l):

	日历=日历组件()
	p.日历=日历
	p.根纵_上横_左纵.addWidget(日历)
	p.添加淡化组件(日历,0.5)
	p.线程.xtsjt.connect(日历.gxrq)
	#p.zjxsztbh.connect(日历.xsztbh)