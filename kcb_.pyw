'''
pip3 install pyqt6 pywin32 sxtwl -i https://mirrors.aliyun.com/pypi/simple/
'''


#使qt在没有环境变量时能使用
import os
from PyQt6.QtWidgets import __file__ as qt6_file
dirname = os.path.dirname(qt6_file)
plugin_path = os.path.join(dirname, 'Qt6', 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path



#防止多开
from PyQt6.QtWidgets import QMessageBox,QApplication
from PyQt6.QtCore import QParallelAnimationGroup, QSharedMemory
'''
import tracemalloc
tracemalloc.start()
#'''

if __name__ == "__main__":
	import sys

	sed=QSharedMemory()
	sed.setKey('kechengbiao_12')
	if sed.attach()or not sed.create(1):
		主=False
	else:
		主=True
	'''
	from multiprocessing import shared_memory
	import array
	#shmm={'名称':('开始','结束')}
	共享大小=1024 ; 块大小=32
	#shtypes=
	try:
		主=True
		shm=shared_memory.SharedMemory(name=shmn,create=True,size=共享大小)
		#=memoryview()
	except FileExistsError:
		主=False
		shm=shared_memory.SharedMemory(name=shmn)
	

	内存区域=[i for i in range(0,共享大小,块大小)]
	内迭=iter(内存区域)

	共享内存={}
	for i in ['主窗口','课程表','天气','壁纸']:
		迭=next(内迭)
		共享内存[i]=shm.buf[迭:迭+块大小]
	
	#'''

	if not 主:
		app=QApplication(sys.argv)
		msg_box=QMessageBox()
		msg_box.setWindowTitle("已在运行")
		msg_box.setText("已运行了一个实例, 不能运行多个")
		msg_box.setIcon(QMessageBox.Icon.Information)
		msg_box.addButton("确定",QMessageBox.ButtonRole.YesRole)
		msg_box.exec()
		sys.exit(0)

#'''

#os.putenv("QT_SCALE_FACTOR",str(round(1366/1920,2)))
app=QApplication(sys.argv)

'''
由于qt 不支持 utf-8编码标识符, 与qt有关的标识符使用拼音首字母.如 信号(signal) 槽(slot) 定时器(timer) 的名称
'''
import threading
import _thread
import time
from PyQt6.QtCore import Qt,QTimer,QPropertyAnimation,QUrl,QEasingCurve,QAbstractAnimation,QThread,pyqtSignal,QObject
from PyQt6.QtWidgets import QWidget,QLabel,QHBoxLayout,QVBoxLayout,QGridLayout,QGraphicsOpacityEffect,QSystemTrayIcon,QMenu,QWidgetAction
from PyQt6.QtGui import QPainter, QPalette, QBrush, QPixmap,QFont,QIcon,QAction
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
import win32gui,win32con
from urllib import request
import json
from d import 准备桌面窗口,桌面窗口错误
from 线程q import 新线程
from flj import flj
import 获取视频
import os
from 扩展 import 加载扩展
from kcb_basic import 获取字体,缩放

扩展=加载扩展()

'''
安装 LAVFilters 以解决 DirectShowPlayerService::doSetUrlSource: Unresolved error code 0x80040216 (IDispatch error #22)
'''

#os.system('w32tm /resync')

时差=0#-60*60*3+80#-86400*2-60*60*7#+60*60*3#-86400*2
#时差=-86400*2

if 时差%1==0:
	多延迟=False
else:
	多延迟=True

t_6=1639756800-86400*7*33




'''
#t_f=1640908834.0-60*60*9
t_f=1640908234.0+60*8#-60*60*9

def 获取时间():
	global t_f
	t_f+=30
	#t_f+=1
	return t_f

def 获取时间():
	return time.time()+(1*60-23)*60
"""
#'''

获取时间=time.time
#"""


'''
#时差检查未完成
'''

#'''
#原始 开始

k1=[# 早读    1      2      3      4     1      2     3    
	["外语","语文","化学"," ","数学","物理","外语","班会","","语文","物理","生物"," "],
	["语文","生物","语文","化学","外语","数学","数学","物理","","外语","数学","外语","英语"],
	["外语","外语","化学","语文","数学","生物","体育","物理","","语文","物理","语文","语文"],
	["语文","外语","数学","外语","生物","美术/形体","语文","体育","","外语","生物","外语","化学"],
	["外语","外语","物理","语文","生物","化学","数学","通用技术","","语文","数学","数学"," "],
	["","","","","","","","","","新闻周刊","化学","语文"," "]
	#["","","","","","","","","","","","",""]
]
k2=[
	["语文","物理","语文","化学","语文","外语","数学","生物"],
	["外语","外语","化学","外语","物理","生物","数学","语文"],
	#["外语","外语","物理","生物","外语","化学","数学","语文"],
	["语文","语文","数学","数学","化学","外语","物理","生物"]
]


节=["早读","第一节","第二节","第三节","第四节","第一节","第二节","第三节","第四节","晚读","第一节","第二节","第三节","第四节"]
始末时间=[
	(7*60+20,7*60+50),
	(8*60+0,8*60+45),
	(8*60+55,9*60+40),
	(9*60+55,10*60+40),
	(10*60+50,11*60+35),
	#(13*60+30,14*60+0),#   1111
	(14*60+20,15*60+0),
	(15*60+15,15*60+55),
	(16*60+5,16*60+45),
	(16*60+50,17*60+30),
	(18*60+30,18*60+50),
	(19*60+0,19*60+45),
	(19*60+55,20*60+40),
	(20*60+50,21*60+35),
	(21*60+45,22*60+30)
]
始末时间_6=[
	(7*60+20,7*60+50),
	(8*60+0,8*60+45),
	(8*60+55,9*60+40),
	(9*60+55,10*60+40),
	(10*60+50,11*60+35),
	#(13*60+30,14*60+0),#   1111
	(14*60+20,15*60+0),
	(15*60+15,15*60+55),
	(16*60+5,16*60+45),
	(16*60+50,17*60+30),
	(18*60+30,18*60+50),
	(19*60+0,19*60+45),
	(19*55+0,20*60+40),
	(20*60+50,21*60+35),
	(21*60+45,22*60+30)
]

始末时间_长假=[
	(7*60+20,7*60+50),
	(8*60+0,8*60+45),
	(8*60+55,9*60+40),
	(10*60+10,10*60+55),
	(11*60+5,11*60+50),
	(13*60+0,13*60+40),
	(13*60+50,14*60+30)
]


for i in range(len(k1)):
	#k1[i]=k1[i][:5]+['政治'if i!=5 else '']+k1[i][5:]#   111
	#if i!=5:
	k1[i].append(" ")

#原始 结束
"""
'''


#修改 开始
k1=[#   1      2      3      4     1      2     3    
	["语文","化学","物理","数学"," ","通用技术","外语","班会","语文诵读","物理","生物","通用技术"],
	["生物","语文","化学","外语"," ","数学","数学","物理","外语听力","数学","外语","英语"],
	["外语","化学","语文","数学"," ","生物","体育","物理","语文诵读","物理","语文","语文"],
	["外语","数学","外语","生物"," ","美术/形体","语文","体育","外语听力","生物","外语","化学"],
	["外语","物理","语文","生物"," ","通用技术","化学","数学","语文诵读","数学","数学"," "],
	["","","","","","","","","新闻周刊","化学","语文"," "]
	#["","","","","","","","","","","","",""]
]
k2=[
	["物理","语文","化学","语文"," ","外语","数学","生物"],
	["外语","化学","外语","物理"," ","生物","数学","语文"],
	["语文","数学","数学","化学"," ","外语","物理","生物"]
]



for i in range(len(k1)):
	#k1[i]=k1[i][:5]+['政治'if i!=5 else '']+k1[i][5:]#   111
	#if i!=5:
	k1[i].append(" ")


节=["第一节","第二节","第三节","第四节","第五节","第一节","第二节","第三节","晚读","第一节","第二节","第三节","第四节"]
始末时间=[
	(8*60+0,8*60+40),
	(8*60+50,9*60+30),
	(9*60+40,10*60+20),
	(10*60+30,11*60+10),
	(11*60+20,12*60+0),

	(14*60+20,15*60+0),
	(15*60+10,15*60+50),
	(16*60+0,16*60+40),
	
	(18*60+30,18*60+50),
	(19*60+0,19*60+45),
	(20*60+0,20*60+45),
	(20*60+55,21*60+40),
	(21*60+50,22*60+35)
]
始末时间_6=[
	(8*60+0,8*60+40),
	(8*60+50,9*60+30),
	(9*60+40,10*60+20),
	(10*60+30,11*60+10),
	(11*60+20,12*60+0),

	(14*60+20,15*60+0),
	(15*60+10,15*60+50),
	(16*60+0,16*60+40),
	
	(18*60+30,18*60+50),
	(19*60+0,19*60+45),
	(20*60+0,20*60+45),
	(20*60+55,21*60+40),
	(21*60+50,22*60+35)
]

始末时间_长假=[
	(7*60+20,7*60+50),
	(8*60+0,8*60+45),
	(8*60+55,9*60+40),
	(10*60+10,10*60+55),
	(11*60+5,11*60+50),
	(13*60+0,13*60+40),
	(13*60+50,14*60+30)
]
#修改 结束
#"""


#for i in range(len(k2)):
#	k2[i]=k2[i][:5]+[' ']+k2[i][5:]#   111
	#k2[i].append('')


#将数字时间转为可读形式  440 (7*60+20) -> 7:20
def 始末时间转文本(原):
	新=[]
	for i in 原:
		始末时间_一项=[]
		for i2 in i:
			a=[]
			for i3 in divmod(i2,60):
				b=str(int(i3))
				if len(b)<2:
					b='0'*(2-len(b))+b
				a.append(b)
			
			始末时间_一项.append(':'.join(a))
		新.append('-'.join(始末时间_一项))
	return 新


始末时间_文本=始末时间转文本(始末时间)
始末时间6_文本=始末时间转文本(始末时间_6)
始末时间长假_文本=始末时间转文本(始末时间_长假)

'''
临时课程:dict
k:日期(20220101)
v:
	list
	0:课程
		为 None, 使用当天原先的课程;
		为 数字, 使用一星期中该天的课程(tm_wday  0为星期一, 5为星期六的第一种, 7为星期六的第三种);
		为 list, 使用 list 中的课程.
	
	1:时间
		为 None, 使用当天原先的时间;
		为 数字:
			1:使用正常的时间
			2:使用周六的时间
			3:使用长假的时间
		;
		为 list, 使用 list 中的时间.

'''


try:
	with open('临时课程.json','r')as fo:
		临时课程=json.load(fo)
		if not isinstance(临时课程,dict):
			raise
except BaseException as e:
	print(e)
	临时课程={}
#临时课程o=open('临时课程.json','r')


def 获取天(tl):
	return (tl.tm_year*10000+tl.tm_mon*100+tl.tm_mday)#*10+tl.tm_wday


def ck(t,tl=None):
	if not tl:
		x_=time.localtime(t)
	else:
		x_=tl
	星期=x_.tm_wday # 0为星期一, 5为星期六
	#分=x_.tm_hour*60+x_.tm_min
	天=获取天(x_)
	#print(星期)
	始末时间_=始末时间
	始末时间_文本_=始末时间_文本

	if 星期==5:
		周六_=(t-t_6)//86400//7%6
		print(周六_)
		周六_=divmod(周六_,3)
		课程=k2[int(周六_[1])]
		#if 周六_[1]==2:
		#	课程[0]=课程[0][int(周六_[0])]
		#return 课程
		始末时间_=始末时间_6
		始末时间_文本_=始末时间6_文本
	elif 星期<5:
		课程=k1[星期]
	elif 星期==6:
		课程=k1[5]
	
	节_=节
	
	天=str(天)
	if 天 in 临时课程:
		课程_=临时课程[天]
		if len(课程_)>0:
			if isinstance(课程_[0],int):
				if 课程_[0]<5:#周一到周五
					课程=课程_[0]
				else:#周六
					ks=课程_[0]-5
					if ks>=len(k2):
						raise ValueError('临时课程的 "'+天+'" 的 "'+str(课程_[0])+'"不在范围(<='+str(len(k2)-1)+')内')
					课程=k2[ks]

			if isinstance(课程_[0],list):
				课程=课程_[0]
		
		if len(课程_)>1:
			if isinstance(课程_[1],int):
				if 课程_[1]==1:
					始末时间_=始末时间
					始末时间_文本_=始末时间_文本
				elif 课程_[1]==2:
					始末时间_=始末时间_6
					始末时间_文本_=始末时间6_文本
				elif 课程_[1]==3:
					始末时间_=始末时间_长假
					始末时间_文本_=始末时间长假_文本
				else:
					raise ValueError('临时课程的 "'+天+'" 的 "'+str(课程_[1])+'"不在范围(<=3)内')

			if isinstance(课程_[1],list):
				始末时间_=课程_[1]
				始末时间_文本_=始末时间转文本(课程_[1])

		if len(课程_)>2:
			if isinstance(课程_[2],int):
				if 课程_[2]==1:
					节_=节
				else:
					raise ValueError('临时课程的 "'+天+'" 的 "'+str(课程_[2])+'"不在范围(<=3)内')

			if isinstance(课程_[2],list):
				节_=课程_[2]
			
			

	
	k_3=[]
	for i in range(len(课程)):
		if i>=len(始末时间_):
			break
		if 课程[i]:
			k_3.append(((始末时间_[i],始末时间_文本_[i]),节_[i],课程[i]))

	return k_3

上课_={0:'已下课',1:'预备',2:'已上课'}
星期_tm_wday=['一','二','三','四','五','六','日']

def dk(x_,ck_rt,仅课数=True):
	分=x_.tm_hour*60+x_.tm_min
	秒=分*60+x_.tm_sec
	暂停=0
	上课=0
	倒计时_=0
	找到课数=False
	课数=0
	for 课数 in range(len(ck_rt)):
		课程时间=ck_rt[课数][0][0]
		'''
		if not 暂停:
			for i in 课程时间:
				t=i-分
				if t>0:
					暂停=t
		'''
		if 课程时间[1]>分:
			找到课数=True
			if 仅课数:
				break
			上课=0
			倒计时_=(课程时间[0])*60
			暂停=倒计时_-120
			if 课程时间[0]<=分:
				上课=2
				倒计时_=(课程时间[1])*60
				暂停=倒计时_
			elif 课程时间[0]-2<=分:
				上课=1
				暂停=倒计时_#-120
				#倒计时_=课程时间[0]*60-秒
			break
	if not 找到课数:
		课数+=1
		倒计时_=None
		暂停=秒+10
	return [课数,上课,倒计时_,暂停]
		


#print(始末时间_文本,始末时间6_文本)


def 时间转文字(t):
	天,时=divmod(int(t),86400)
	时,分=divmod(时,3600)
	分,秒=divmod(分,60)
	s=''
	if 天:
		s+=str(天)+'天'
	if 时:
		s+=str(时)+'时'
	if 分:
		s+=str(分)+'分'
	if 秒:
		s+=str(秒)+'秒'
	elif s:
		s+='整'
	return s



class 单课程组件():
	def __init__(s,网格:QGridLayout,坐标):
		super().__init__()
		网格纵坐标,网格横坐标=坐标
		s.labels=[QLabel()for i in range(3)]
		#s.labels[0].setFont(QFont("宋体",12,QFont.Weight.Bold))
		#s.labels[1].setFont(QFont("宋体",12,QFont.Weight.Bold))
		#s.labels[2].setFont(QFont("宋体",12,QFont.Weight.Bold))
		for i in s.labels:
			#i.setFont(QFont("黑体",20,QFont.Weight.Bold))
			i.setStyleSheet('color:#ffffff')
		s.labels[0].setMinimumWidth(缩放(155))
		s.labels[0].setFont(获取字体(18))
		s.labels[1].setFont(获取字体(20))
		s.labels[2].setFont(获取字体(20))
		for i in s.labels:
			网格.addWidget(i,网格纵坐标,网格横坐标)
			网格纵坐标+=1
			i.setAlignment(Qt.AlignmentFlag.AlignCenter)

	def 设置内容(s,a,b,c):
		s.labels[0].setText(a)
		s.labels[1].setText(b)
		s.labels[2].setText(c)


class 日期时间组件(单课程组件):
	def __init__(s,网格:QGridLayout,坐标):
		super().__init__(网格,坐标)
		s.labels[0].setFont(获取字体(20))
		s.labels[1].setFont(获取字体(20))
		s.labels[2].setFont(获取字体(20))
	
	def gxsj(s,*a):
		s.更新时间(*a)
	def 更新时间(s,tl=None):
		if not tl:
			tl=time.localtime(获取时间())
		s.labels[0].setText(time.strftime("%H:%M:%S",tl))
	
	def gxrq(s,*a):
		s.更新日期(*a)
	def 更新日期(s,tl=None):
		if not tl:
			tl=time.localtime(获取时间())
		s.labels[1].setText(time.strftime("%Y/%m/%d",tl))
		s.labels[2].setText('星期'+星期_tm_wday[tl.tm_wday])


class 将上课程():
	def __init__(s):
		s.d={}
	
	def __len__(s):
		return len(s.d)

	def __getitem__(s,ti):#t为当前时间,i为之后i天
		if isinstance(ti,(int,float)):
			t=ti
			i=0
		elif isinstance(ti,tuple):
			t,i=ti
		else:
			raise
		if i<0:
			raise ValueError('!>=0')
		ti=t+i*86400
		天=获取天(time.localtime(ti))
		今天=获取天(time.localtime(t))
		for i in list(s.d.keys()):#删除今天之前的课程. 直接遍历字典, 删除时会报错
			if i<今天:
				del s.d[i]

		try:
			return s.d[天]
		except KeyError:
			rt=ck(ti)
			s.d[天]=rt
			return rt
		


class 课程表类():
	def __init__(s,网格:QGridLayout,开始坐标=(0,0)):
		网格横坐标,网格纵坐标=开始坐标
		#s.timer_id=0

		s.状态={'上课':None,'当前课程':None,'已上课数':None,'一天课程':None}

		s.时差_=0
		s.将上课程=将上课程()

		#s.wh=[0,0]
		#s.根横=QHBoxLayout()
		#s.根横.setSpacing(20)

		s.单课程l=[]


		for i in range(6):
			单课程=单课程组件(网格,(网格横坐标,网格纵坐标+i))
			s.单课程l.append(单课程)
		
		
		s.上课状态=QLabel()
		s.上课状态.setAlignment(Qt.AlignmentFlag.AlignCenter)
		s.上课状态.setFont(获取字体(28,QFont.Weight.Bold))
		

		s.上课状态d=QLabel()
		s.上课状态d.setFont(获取字体(24,QFont.Weight.Bold))
		s.上课状态d.setStyleSheet('color:#ffffff')



	def 开始(s):
		
		s.暂停=0
		s.天=0


	def 更新课程(s,t=None):
		if t is None:
			t=获取时间()+时差

		tl=time.localtime(t)

		天=获取天(tl)

		分=tl.tm_hour*60+tl.tm_min
		秒=分*60+tl.tm_sec

		if not(天==s.天 and 0<s.暂停-秒<=3600):#到达设定的时间后才会更新
			s.状态['当前课程']=''
			一天课程=s.将上课程[t]
			一天课程数=len(一天课程)
			已上课数_,上课,s.倒计时_,s.暂停=dk(tl,一天课程,False)
			s.状态['已上课数']=已上课数_
			s.状态['一天课程']=一天课程

			s.天=天
			已用课数=已上课数_
			天数=0
			天数_旧=0
			for i in range(len(s.单课程l)):#遍历 单课程组件 ; 需要的课程数量 会小于或等于 单课程组件的数量, 因为每天都有一个日期占用一个单课程组件
				while 1:
					if 一天课程数<=已用课数:
						已用课数=0
						天数+=1
						一天课程=s.将上课程[t,天数]
						一天课程数=len(一天课程)
					else:
						break
				if 天数==天数_旧:
					cki=一天课程[已用课数]
					if i==0:
						s.状态['当前课程']=cki[2]
					已用课数+=1
				else:
					天数_旧=天数
					tln=time.localtime(t+天数*86400)

					年,月,日,星期=tln.tm_year,tln.tm_mon,tln.tm_mday,tln.tm_wday
					日期_s=str(日)+'日'
					if 日==1:
						日期_s=str(月)+'月'+日期_s
						if 月==1:
							日期_s=str(年)+'年'+日期_s
					
					cki=[['',''],日期_s,'星期'+星期_tm_wday[星期]]
				s.单课程l[i].设置内容(cki[0][1],cki[1],cki[2])
			
			s.状态['上课']=上课
			s.上课状态.setText(上课_[上课])
			s.上课状态.setStyleSheet('color:'+('#00ff00','#ffff00','#ff0000')[上课])

		if s.倒计时_ is not None:
			m=s.倒计时_-秒
		else:
			m=0
		
		s.上课状态d.setText(时间转文字(m)if m else '')

		return m




class 单消息组件(QWidget):
	def __init__(s):
		super().__init__()

		s.开始时间=None
		s.结束时间=None
		s.显示=None
		
		s.标题label=QLabel()
		s.标题label.setFont(获取字体(20))
		s.标题label.setWordWrap(True)
		s.正文label=QLabel()
		s.正文label.setFont(获取字体(16))
		s.正文label.setWordWrap(True)
		s.纵根=QVBoxLayout()
		s.纵根.addWidget(s.标题label)
		s.纵根.addWidget(s.正文label)
		s.setLayout(s.纵根)

		s.setVisible(False)

	def 设置(s,标题=None,正文=None,显示=None,开始时间=None,结束时间=None):
		if 标题 is not None:
			s.标题label.setText(标题)
		if 正文 is not None:
			s.正文label.setText(正文)
		if 开始时间 is not None:
			s.开始时间=开始时间
		if 结束时间 is not None:
			s.结束时间=结束时间
		if 显示 is not None:
			s.显示=显示
		




class 消息_主窗口(QWidget):
	def __init__(s,*args,**kwargs):
		super().__init__(*args,**kwargs)
		s.重要消息l=[]
		s.普通消息l=[]
		s.根纵=QVBoxLayout()
		"""
		s.重要消息label=QLabel()
		s.普通消息label=QLabel()
		s.根纵.addWidget(s.重要消息label)
		s.根纵.addWidget(s.普通消息label)
		'''
		"""
		s.重要消息widget=QWidget()
		s.普通消息widget=QWidget()
		s.重要消息vbox=QVBoxLayout()
		s.普通消息vbox=QVBoxLayout()
		s.重要消息widget.setLayout(s.重要消息vbox)
		s.普通消息widget.setLayout(s.普通消息vbox)
		s.根纵.addWidget(s.重要消息widget)
		s.根纵.addWidget(s.普通消息widget)
		s.根纵.addStretch(1)


		#'''
		s.setLayout(s.根纵)

		s.timer=QTimer(s)
		s.timer.timeout.connect(s.t_gxxs)


	def t_gxxs(s):
		s.刷新()
	def 刷新(s):
		for i in ((s.重要消息l,s.重要消息vbox),(s.普通消息l,s.普通消息vbox)):
			l,layout=i
			t=time.time()
			for x in l:
				x:单消息组件
				if x.显示 and x.开始时间 and x.结束时间 and x.开始时间<=t<=x.结束时间:
					x.setVisible(True)
				else:
					if x.显示:
						x.显示=False
					x.setVisible(False)

	def 添加消息(s,类型,*args,**kwargs):
		消息=单消息组件(*args,**kwargs)
		if 类型==1:#普通
			s.普通消息l.append(消息)
			s.普通消息vbox.addWidget(消息)
		elif 类型==2:#重要
			s.重要消息l.append(消息)
			s.重要消息vbox.addWidget(消息)

		return 消息


class 主窗口_线程(QThread):
	#课程时间秒 和 系统时间秒 都 每整秒发送一次, 但 课程时间和系统时间的误差不为整秒 时 将不同时发送
	kcsjm=pyqtSignal(float)#课程时间秒
	xtsjm=pyqtSignal(time.struct_time)#系统时间秒
	xtsjf=pyqtSignal(time.struct_time)#系统时间分
	xtsjs=pyqtSignal(time.struct_time)#系统时间时
	xtsjt=pyqtSignal(time.struct_time)#系统时间天
	def __init__(s,parent):
		super().__init__()
		s.parent=parent
		s.sm_t=0

	def run(s):
		旧时间=time.localtime()
		s.xtsjt.connect(s.xtsjs.emit)
		s.xtsjs.connect(s.xtsjf.emit)
		#s.xtsjf.connect(s.xtsjm.emit)

		s.xtsjt.emit(旧时间)
		while True:
			t=获取时间()
			tl=time.localtime(t)
			
			if 旧时间.tm_mday!=tl.tm_mday:
				s.xtsjt.emit(tl)
			elif 旧时间.tm_hour!=tl.tm_hour:
				s.xtsjs.emit(tl)
			elif 旧时间.tm_min!=tl.tm_min:
				s.xtsjf.emit(tl)

			旧时间=tl
			


			s.xtsjm.emit(tl)
			if 多延迟:
				time.sleep(1-(时差+time.time())%1)

			s.kcsjm.emit(获取时间())

			st=time.time()
			if st-s.sm_t>20:
				print(2)
			time.sleep(1-st%1)
			#time.sleep(0.1)
			s.sm_t=st



上课状态_对应_刷新=[0,0,1]

class 主窗口(QWidget):
	kcztbh=pyqtSignal(int)#课程状态变化
	zjxsztbh=pyqtSignal(bool)#组件显示状态变化
	ygx=pyqtSignal()#预更新. 在显示前 提前更新, 如网络请求等不能立即得到结果的操作. 需要在非主线程中更新.
	ks=pyqtSignal()#开始

	def __init__(s, parent=None):
		super().__init__(parent)
		#s.托盘=托盘图标(s)
		s.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)#透明背景
		s.setWindowFlags(Qt.WindowType.FramelessWindowHint|Qt.WindowType.MSWindowsFixedSizeDialogHint)
		#s.setWindowFlags(Qt.WindowStaysOnBottomHint|Qt.FramelessWindowHint|Qt.MSWindowsFixedSizeDialogHint)
		s.time=0
		s.setStyleSheet('*{color:#ffffff}')

		s.setFont(获取字体(18,QFont.Weight.Bold))


		s.winid_s=int(s.winId())


		s.宽=0
		s.高=0

		s.刷新_上课状态=None#与 s.上课状态 不同, 预备与下课都将为0, 上课将为1.且它的更新会提前于 s.上课状态 .
		s.上课状态=None
		s.下课预更新=None

		s.嵌入_继续=None

		s.状态检查定时器=QTimer(s)
		s.状态检查定时器.timeout.connect(s.ztjc)
		s.状态检查定时器.setInterval(1000)

		s.根纵=QVBoxLayout()
		s.根纵.setSpacing(0)
		s.setLayout(s.根纵)

		s.根纵_上横=QHBoxLayout()
		s.根纵_上横.addStretch(1)

		s.根纵_上横_左纵=QVBoxLayout()
		s.根纵_上横.addLayout(s.根纵_上横_左纵)
		s.根纵_上横.addSpacing(缩放(40))

		s.根纵_上横_右纵=QVBoxLayout()
		s.根纵_上横.addLayout(s.根纵_上横_右纵)

		s.根纵.addLayout(s.根纵_上横)

		

		s.根纵_下横=QHBoxLayout()

		s.根纵_下横_左纵=QVBoxLayout()
		s.根纵_下横.addLayout(s.根纵_下横_左纵)
		s.根纵_下横.addStretch(缩放(1000))

		s.根纵_下横_右纵=QVBoxLayout()
		s.根纵_下横.addLayout(s.根纵_下横_右纵)

		s.根纵.addLayout(s.根纵_下横)
		s.根纵.addStretch(1)


		s.右纵_网=QGridLayout()
		s.根纵_上横_右纵.addLayout(s.右纵_网)
		s.根纵_上横_右纵.addSpacing(缩放(60))
	
		s.根纵_上横_右纵_横=QHBoxLayout()
		s.根纵_上横_右纵.addLayout(s.根纵_上横_右纵_横)

		s.淡化动画组=QParallelAnimationGroup()
		s.淡化动画值=[]


		s.主消息=消息_主窗口()
		#s.主消息.添加消息(1).设置('123','456',True,time.time(),time.time()+10)
		填空l=QLabel(' '*6)
		填空l.setFont(获取字体(6))
		s.右纵_网.addWidget(填空l,0,1)
		s.课程表=课程表类(s.右纵_网,(1,2))
		s.右纵_网.addWidget(s.课程表.上课状态,0,0)
		s.右纵_网.addWidget(s.课程表.上课状态d,0,2,1,4)
		s.日期时间=日期时间组件(s.右纵_网,(1,0))


		s.线程=主窗口_线程(s)
		s.线程.kcsjm.connect(s.gxkc)
		s.线程.xtsjm.connect(s.日期时间.gxsj)
		s.线程.xtsjt.connect(s.日期时间.gxrq)
		s.zjxsztbh.connect(s.dhdh)

		扩展.配置(s,配置l)


		s.根纵_上横_左纵.addWidget(s.主消息)
		

		s.根纵_上横_左纵.addStretch(1)
		s.根纵_上横_右纵.addStretch(1)
		s.根纵_上横_右纵_横.addStretch(1)

		s.根纵_下横_左纵.addStretch(1)
		s.根纵_下横_右纵.addStretch(1)



		

		s.添加淡化组件(s.主消息.普通消息widget)

		for i in range(len(s.课程表.单课程l)):
			if i!=0:
				i:单课程组件=s.课程表.单课程l[i]
				for i2 in i.labels:
					s.添加淡化组件(i2,0.5)


		s.淡化属性_初入=QGraphicsOpacityEffect()
		s.淡化属性_初入.setOpacity(0.01)
		s.setGraphicsEffect(s.淡化属性_初入)
		s.初入动画=QPropertyAnimation(s.淡化属性_初入,b'opacity')
		s.初入动画.setDuration(1000)
		s.初入动画.setStartValue(0.01)
		s.初入动画.setEndValue(1)
		s.初入动画.setEasingCurve(QEasingCurve.Type.InCubic)
		s.初入动画.finished.connect(lambda:(s.setGraphicsEffect(None),s.刷新淡化值()))



	def 添加淡化组件(s,组件:QWidget,最淡值=0.01,最深值=1):
		淡化属性=QGraphicsOpacityEffect()
		淡化属性.setOpacity(0)
		#淡化属性.setOpacity(淡化属性.opacity())
		组件.setGraphicsEffect(淡化属性)
		淡化动画=QPropertyAnimation(淡化属性,b'opacity')
		淡化动画.setDuration(5000)
		淡化动画.setStartValue(最淡值)
		淡化动画.setEndValue(最深值)
		淡化动画.setEasingCurve(QEasingCurve.Type.InCubic)
		s.淡化动画值.append(淡化属性)
		s.淡化动画组.addAnimation(淡化动画)

	def 刷新淡化值(s):#为了解决 setGraphicsEffect(None) 时显示异常的问题
		for i in s.淡化动画值:
			i:QGraphicsOpacityEffect
			i.setOpacity(i.opacity()+0.01)
			i.setOpacity(i.opacity()-0.01)

	def dhdh(s,*a):
		s.淡化动画(*a)
	def 淡化动画(s,方向):
		if 方向:
			s.淡化动画组.setDirection(QAbstractAnimation.Direction.Forward)
		else:
			s.淡化动画组.setDirection(QAbstractAnimation.Direction.Backward)
		s.淡化动画组.start()


	def gxkc(s):
		s.更新课程()
	def 更新课程(s):
			倒计时_=s.课程表.更新课程()
			
			上课状态=s.课程表.状态['上课']

			
			刷新_上课状态=上课状态_对应_刷新[上课状态]
			if 倒计时_ and 倒计时_<60:#取反
				刷新_上课状态=(1,0)[刷新_上课状态]

			if s.刷新_上课状态!=刷新_上课状态:
				s.刷新_上课状态=刷新_上课状态
				if 刷新_上课状态:
					s.下课预更新=True
					#s.主消息.普通消息widget.setVisible(False)
					s.zjxsztbh.emit(False)
				else:
					#s.主消息.普通消息widget.setVisible(True)
					s.zjxsztbh.emit(True)


			if 上课状态!=s.上课状态:
				s.上课状态=上课状态
				#print(上课状态)
				s.kcztbh.emit(上课状态)
			
			if 上课状态==2 and s.下课预更新 and 倒计时_ and 倒计时_<90:
				print('预更新',上课状态,s.下课预更新,倒计时_)
				s.下课预更新=False
				s.ygx.emit()

	def 对齐桌面(s):
		d=QApplication.primaryScreen().geometry()
		宽,高=d.width(),d.height()
		if s.宽==宽 and s.高==高:
			return
		s.setGeometry(0,0,宽,高)


	def 嵌入(s):
		if s.嵌入_继续:
			return
		s.嵌入_继续=1
		while 1:
			try:
				s.winid_桌面=准备桌面窗口()
				break
			except 桌面窗口错误 as e:
				if not s.嵌入_继续>1:
					s.嵌入_继续=2
					print('主窗口:e;无法嵌入桌面窗口,'+str(e))
				
				time.sleep(1)


		#将窗口设为桌面背景的子窗口
		win32gui.SetParent(s.winid_s,s.winid_桌面)

		
		s.嵌入_继续=0

	def ztjc(s):
		s.状态检查()
	def 状态检查(s):
		'''
		if s.time<20:
			s.time+=1
			if s.time==5:
				s.背景视频.入()
			if s.time==6:
				s.背景视频.出()
		'''
		s.对齐桌面()
		a=[]
		win32gui.EnumChildWindows(s.winid_桌面,lambda hwnd,param:param.append(hwnd),a)
		if not s.winid_s in a:
			print('重新嵌入')
			s.嵌入()
			s.update()
			s.setVisible(False)
			s.setVisible(True)


	def 开始(s):
		s.嵌入()
		s.对齐桌面()
		s.状态检查定时器.start()
		s.主消息.timer.start(1000)
		s.课程表.开始()
		s.show()
		s.adjustSize()
		s.adjustSize()
		s.初入动画.start()

		s.线程.start()

		s.ks.emit()

class 托盘图标(QSystemTrayIcon):
	def __init__(s,parent:主窗口=None):
		super().__init__()
		s.主窗口=parent
		s.setIcon(QIcon('icon.png'))
		#s.setToolTip('桌面背景')
		s.setVisible(True)
		s.menu=QMenu()

		s.menu.addAction('退出').triggered.connect(s.tc)
		s.setContextMenu(s.menu)

		parent.ks.connect(s.show)

	def tc(s):
		s.退出()
	def 退出(s):
		s.setVisible(False)
		app.exit()

			

if __name__ == "__main__":

	配置l=flj('配置.json')


	if not 配置l.d:
		配置l.关闭()
		raise Exception('配置文件错误')
		from 欢迎 import 欢迎窗口
		欢迎窗口()
		sys.exit()
		

	配置l.设置默认值({
		'视频背景':{
			'启用':True,
			'项':0
		},
		'课程表':{
			'启用':True,
			'时差':0,
			'周六时间':None
		}
		
	})

	时差=配置l['课程表']['时差']
		
	if 时差%1==0:
		多延迟=False
	else:
		多延迟=True

	#t_6=配置l['周六时间']

	w=主窗口()
	#w.setStyleSheet('border:1px solid #ffffff;')


	#t=托盘图标(w)


	'''
	ti=QSystemTrayIcon(w)

	tim=QMenu()
	#tim.addAction(QAction('&退出(Exit)',ti,triggered=lambda:(ti.setVisible(False),w.背景视频.出(),新线程(4,app.quit))))
	#tim.addAction(QAction('&退出(Exit)',ti,triggered=lambda:(w.win.setGraphicsEffect(w.淡化属性_初入),w.初入动画.setDirection(QAbstractAnimation.Direction.Backward),w.初入动画.finished.connect(app.quit),w.初入动画.start(),新线程(2,app.quit))))
	tim.addAction(QAction('退出',ti,triggered=app.quit))
	ti.setContextMenu(tim)
	icon=QIcon('icon.png')
	#icon.addPixmap(QPixmap.loadFromData('iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9TS0UqDnYQcchQnSyIFhFcpIpFsFDaCq06mFz6BU0akhQXR8G14ODHYtXBxVlXB1dBEPwAcXRyUnSREv+XFFrEeHDcj3f3HnfvAKFZZarZMwGommWkE3Exl18Vg68Q4EcAs4hJzNSTmcUsPMfXPXx8vYvyLO9zf45+pWAywCcSzzHdsIg3iKc3LZ3zPnGYlSWF+Jx43KALEj9yXXb5jXPJYYFnho1sep44TCyWuljuYlY2VOIYcURRNcoXci4rnLc4q9U6a9+TvzBU0FYyXKc5ggSWkEQKImTUUUEVFqK0aqSYSNN+3MM/7PhT5JLJVQEjxwJqUCE5fvA/+N2tWZyadJNCcSDwYtsfo0BwF2g1bPv72LZbJ4D/GbjSOv5aE5j5JL3R0SJHwMA2cHHd0eQ94HIHGHrSJUNyJD9NoVgE3s/om/LA4C3Qt+b21t7H6QOQpa6Wb4CDQ2CsRNnrHu/u7e7t3zPt/n4AvP9yxa0hWoIAAAAGYktHRAAAAAAAAPlDu38AAAAJcEhZcwAALiMAAC4jAXilP3YAAAAHdElNRQfmAgMGDzjPq3ZSAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAlZJREFUeNrtmj1rVFEQhp/R2GiUSPxIRC5qoUEETdIIBhEstLIOFloYO3+E+DfcSkHr7QKC1UIC4kastBFcgq4f0WhwBZvXZm44WXazIVrkcOeFZefOuffuzsPcmTnLQigUCoVCoVComrJ161FblYr81phtdFQJQBLrrtxjkTQradjtYUmzbk9JuilparPrh3ZYMAIwM+uyX7o9LWkOeNjj2tR+6mYHeANMZwHAzKyXDdxN/DWg1hX8XI971bbymUM5pLmZNQes17Z77+xrwL8qAASAimuntcEJ4Cqw7MWt7r5UZ5LiV5c0Dpwzs2eSJn2pAFpAYWb1nLpAC6gDv7t8qb70gXfH+z7AbmAEaGSVAWbWSYJY90ka7RP0KDAGfPXXhA8+BfDazFaymwOSND4J3AA+JMungcc9sqZU298bwIxnU3aD0FvgGnAbaAJPgG++NgN8Ai4Bz4Fyzt/rmVBCGAFO5ToJnvcvf98DPOv+Y8A94AXwA7gCvANOAJ+BV8Bqmg2SJs1sKSsAZrYg6QjQMrOlrud/wTPgT9oJknpQdoDCM6Kd617gKPBA0qIfHwS+A4e6zjvsu8D9wJr71oBF4FfyWGQHYB/wMTl+DxzwNE+1nMA57r6LwAXvCp2cd4N7gJ99ZoEy1S97oOPJOfP++Kz4bJAlgLKgtZJgu9XYQp9vDiqEOxXAqg81m6mQVAw457q/5wXAq///uNV8tjVgUP+O7XAACAABIAAEgAAQAAJAAAgAASAABIAAEAACQAAIANvSxt8Eq/Z32VAoFAqFQqFQhfUX3qDIplPG4R4AAAAASUVORK5CYII='))
	ti.setIcon(icon)
	ti.show()
	#'''

	w.开始()
	sys.exit(app.exec())