import os
from PyQt6.QtWidgets import __file__ as qt6_file
dirname = os.path.dirname(qt6_file)
plugin_path = os.path.join(dirname, 'Qt6', 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


from PyQt6.QtWidgets import QMessageBox,QApplication
from PyQt6.QtCore import QSharedMemory



'''
import tracemalloc
tracemalloc.start()
#'''

if __name__ == "__main__":
	import sys
	app=QApplication(sys.argv)
	shmn='kechengbiao_12'

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
		msg_box=QMessageBox()
		msg_box.setWindowTitle("已在运行")
		msg_box.setText("已运行了一个实例, 不能运行多个")
		msg_box.setIcon(QMessageBox.Icon.Information)
		msg_box.addButton("确定",QMessageBox.ButtonRole.YesRole)
		msg_box.exec()
		sys.exit(0)

#'''

import threading
import _thread
import time
from PyQt6.QtCore import Qt,QTimer,QPropertyAnimation,QUrl,QEasingCurve,QAbstractAnimation,QThread,pyqtSignal,QObject
from PyQt6.QtWidgets import QWidget,QLabel,QHBoxLayout,QVBoxLayout,QGridLayout,QGraphicsOpacityEffect,QSystemTrayIcon,QMenu,QWidgetAction
from PyQt6.QtGui import QPalette, QBrush, QPixmap,QFont,QIcon,QAction
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
import win32gui,win32con
from urllib import request
import json
from d import 准备桌面窗口,桌面窗口错误
from 线程q import 新线程
from flj import flj
import 获取视频
from 获取节假日 import 获取节假日,节假日_文本
import 日期
import os

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

t_6=1639756800-86400*7*6




'''
t_f=1640908834-60*60*50

def 获取时间():
	global t_f
	t_f+=60*2
	return t_f
"""
#'''

获取时间=time.time
#"""


'''
#时差检查未完成
'''


k1=[# 早读    1      2      3      4     1      2     3    
	["外语","语文","化学","数学","物理","通用技术","外语","班会","自习"," ","物理","生物","通用技术"],
	["语文","生物","语文","化学","外语","数学","数学","物理","自习"," ","数学","外语","英语"],
	["外语","外语","化学","语文","数学","生物","体育","物理","自习"," ","物理","语文","语文"],
	["语文","外语","数学","外语","生物","美术/形体","语文","体育","自习"," ","生物","外语","化学"],
	["外语","外语","物理","语文","生物","通用技术","化学","数学","自习"," ","数学","数学"," "],
	["","","","","","","","",""," ","化学","语文"," "]
	#["","","","","","","","","","","","",""]
]
k2=[
	["语文","物理","语文","化学","语文","外语","数学","生物"],
	["外语","外语","化学","外语","物理","生物","数学","语文"],
	["语文","语文","数学","数学","化学","外语","物理","生物"]
]

节=["早读","第一节","第二节","第三节","第四节","第一节","第二节","第三节","第四节","晚读","第一节","第二节","第三节","第四节"]
始末时间=[
	(7*60+20,7*60+50),
	(8*60+0,8*60+45),
	(8*60+55,9*60+40),
	(10*60+10,10*60+55),
	(11*60+5,11*60+50),
	#(13*60+30,14*60+0),#   1111
	(14*60+20,15*60+0),
	(15*60+15,15*60+55),
	(16*60+5,16*60+45),
	(16*60+50,17*60+30),
	(18*60+30,18*60+50),
	(19*60+0,19*60+45),
	(20*60+0,20*60+45),
	(20*60+55,21*60+40),
	(21*60+50,22*60+30)
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
	(20*60+0,20*60+45),
	(20*60+55,21*60+40),
	(21*60+50,22*60+30)
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
	k1[i].append("自习")

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
	return tl.tm_year*10000+tl.tm_mon*100+tl.tm_mday


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
	
	if str(天) in 临时课程:
		课程_=临时课程[str(天)]
		if len(课程_)>0:
			if isinstance(课程_[0],int):
				if 课程_[0]<5:
					课程=课程_[0]
				else:
					ks=课程_[0]-5
					if ks>=len(k2):
						raise ValueError('临时课程的 "'+str(天)+'" 的 "'+str(课程_[0])+'"不在范围(<='+str(len(k2)-1)+')内')
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
					raise ValueError('临时课程的 "'+str(天)+'" 的 "'+str(课程_[1])+'"不在范围(<=3)内')

			if isinstance(课程_[1],list):
				始末时间_=课程_[1]
				始末时间_文本_=始末时间转文本(课程_[1])

		if len(课程_)>2:
			if isinstance(课程_[2],int):
				if 课程_[2]==1:
					节_=节
				else:
					raise ValueError('临时课程的 "'+str(天)+'" 的 "'+str(课程_[2])+'"不在范围(<=3)内')

			if isinstance(课程_[2],list):
				节_=课程_[2]
			
			

	
	k_3=[]
	for i in range(len(课程)):
		if i>=len(始末时间_):
			break
		if 课程[i]:
			k_3.append(((始末时间_[i],始末时间_文本_[i]),节_[i],课程[i]))

	return k_3

上课_={0:'已下课',1:'  预备',2:'已上课'}
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






class 单课程组件(QVBoxLayout):
	def __init__(s):
		super().__init__()
		#s.setSpacing(3)
		s.labels=[QLabel()for i in range(3)]
		#s.labels[0].setFont(QFont("宋体",12,QFont.Weight.Bold))
		#s.labels[1].setFont(QFont("宋体",12,QFont.Weight.Bold))
		#s.labels[2].setFont(QFont("宋体",12,QFont.Weight.Bold))
		for i in s.labels:
			#i.setFont(QFont("黑体",20,QFont.Weight.Bold))
			i.setStyleSheet('color:#ffffff')
		s.labels[0].setFont(QFont("黑体",18,QFont.Weight.Bold))
		s.labels[1].setFont(QFont("黑体",20))
		s.labels[2].setFont(QFont("黑体",20,QFont.Weight.Bold))
		for i in s.labels:
			s.addWidget(i)
			i.setAlignment(Qt.AlignmentFlag.AlignCenter)

	def 设置内容(s,a,b,c):
		s.labels[0].setText(a)
		s.labels[1].setText(b)
		s.labels[2].setText(c)



class 课程表组件(QWidget):
	def __init__(s, parent=None):
		super().__init__(parent)

		#s.timer_id=0

		s.状态={'上课':None,'当前课程':None,'已上课数':None}

		s.父宽=0
		s.父高=0
		s.课程定时器=QTimer(s)
		s.课程定时器.setTimerType(Qt.TimerType.PreciseTimer)
		#s.课程定时器.setSingleShot(True)
		#s.gxkc s.更新课程
		s.课程定时器.timeout.connect(s.gxkc)


		s.时间定时器=QTimer(s)
		#s.gxsj s.更新时间
		s.时间定时器.setTimerType(Qt.TimerType.PreciseTimer)
		s.时间定时器.timeout.connect(s.gxsj)


		
		s.时差检查定时器=QTimer(s)
		#s.scjc s.时差检查
		s.时差检查定时器.timeout.connect(s.scjc)
		s.时差检查定时器.setInterval(10000)
		#s.时差检查定时器.start()
		s.时差_=0



		#s.wh=[0,0]
		s.根横=QVBoxLayout()

		s.根横_纵=QHBoxLayout()
		#s.根横_纵.addStretch(1)
		#s.根横_纵.setSpacing(10)
		s.课程表qbox=[]


		s.日期时间=单课程组件()
		s.日期时间.labels[0].setFont(QFont("黑体",20,QFont.Weight.Bold))
		s.日期时间.labels[1].setFont(QFont("黑体",20,QFont.Weight.Bold))
		s.日期时间.labels[2].setFont(QFont("黑体",20))
		s.根横_纵.addLayout(s.日期时间)

		填空=QLabel()
		填空.setText('      ')
		s.根横_纵.addWidget(填空)

		for i in range(6):
			单课程=单课程组件()
			s.根横_纵.addLayout(单课程)
			填空=QLabel()
			填空.setText(' ')
			s.根横_纵.addWidget(填空)
			#s.根横_纵.addStretch(1)
			s.课程表qbox.append(单课程)
		
		s.根横_纵2=QHBoxLayout()
		
		填空=QLabel()
		填空.setFont(QFont("黑体",8,QFont.Weight.Bold))
		填空.setText(' ')
		s.根横_纵2.addWidget(填空)
		
		s.上课状态=QLabel()
		s.上课状态.setFont(QFont("黑体",28,QFont.Weight.Bold))
		s.根横_纵2.addWidget(s.上课状态)
		
		填空=QLabel()
		填空.setFont(QFont("黑体",16,QFont.Weight.Bold))
		填空.setText('  ')
		s.根横_纵2.addWidget(填空)

		s.上课状态d=QLabel()
		s.上课状态d.setFont(QFont("黑体",24,QFont.Weight.Bold))
		s.上课状态d.setStyleSheet('color:#ffffff')
		s.根横_纵2.addWidget(s.上课状态d)

		s.其他信息=QLabel()
		s.其他信息.setFont(QFont("黑体",16,QFont.Weight.Bold))
		s.其他信息.setStyleSheet('color:#ffffff')
		#s.其他信息.setText('123456')
		s.其他信息.setAlignment(Qt.AlignmentFlag.AlignCenter)

		s.根横_纵2.addStretch(1)

		s.根横.addLayout(s.根横_纵2)
		s.根横.addLayout(s.根横_纵)
		s.根横.addWidget(s.其他信息)
		s.setLayout(s.根横)
		s.setWindowTitle('课程表')


	def start(s,初始=False):
		
		#s.状态检查定时器.setInterval(1000)
		#s.状态检查定时器.start()

		s.将上课程={}
		s.暂停=0
		'''
		while 1:
			tl=time.localtime(t)
			天=获取天(tl)
			s.将上课程[天]=ck(t)
			总数=sum([len(s.将上课程[i]) for i in s.将上课程])
			t+=86400
			已上课数=dk(今天_tl,s.将上课程[今天_天])[0]
			if 总数-已上课数<len(s.课程表qbox):
				continue
			else:
				break
		'''
		
		#s.更新课程()
		if 初始:

			'''
			time.sleep(1.001-time.time()%1)
			s.时间定时器.setInterval(1000)
			s.时间定时器.start()
			'''

			time.sleep(1.001-(时差+time.time())%1)
			#s.课程定时器.setInterval(1000)
			#s.课程定时器.start()
			##time.sleep(1)
			for i in range(2):
				s.更新课程()
	
	def gxkc(s):
		s.更新课程()
	def 更新课程(s,t=None):
		if t is None:
			t=获取时间()+时差


		tl=time.localtime(t)
		天=获取天(tl)
		需要更新=False
		if 天 in s.将上课程:
			已上课数=dk(tl,s.将上课程[天])[0]
		else:
			已上课数=0
			需要更新=True

		上课=None
		当前课程=''
	
		x_=tl
		分=x_.tm_hour*60+x_.tm_min
		秒=分*60+x_.tm_sec

		#s.暂停-秒<=0 or s.暂停-秒>3600
		#not(0<s.暂停-秒<=3600)
		if not(0<s.暂停-秒<=3600):
			#上课=None
			if not 需要更新:
				已上课数_,上课,s.倒计时_,暂停=dk(tl,s.将上课程[天],False)
				s.暂停=暂停
			课程天_=tuple(s.将上课程.keys())
			for i in 课程天_:
				if i<天:
					s.将上课程.pop(i,'')
			课程天_=tuple(s.将上课程.keys())

			课程天_k=0
			课程天_k_=课程天_k
			#课程天_[课程天_k]
			课程天_数量=0
			i_=0
			for i in range(len(s.课程表qbox)):
				循环_=True
				while 循环_:
					if 需要更新 or not len(s.将上课程[课程天_[课程天_k]])>i_+已上课数-课程天_数量:
						if 课程天_:
							课程天_数量+=len(s.将上课程[课程天_[课程天_k]])

							课程天_k+=1
						if  not len(课程天_)>课程天_k:

							while 1:
								t_=t+课程天_k*86400
								tl=time.localtime(t_)
								天=获取天(tl)
								s.将上课程[天]=ck(t_,tl)
								课程天_=tuple(s.将上课程.keys())
								#s.课程天_=课程天_
								if len(s.将上课程[课程天_[课程天_k]])>=课程天_k:
									课程天_k+=1
									continue
								break


					if 课程天_k_==课程天_k:
						cki=s.将上课程[课程天_[课程天_k]][i_+已上课数-课程天_数量]
						i_+=1
						if not 当前课程:
							当前课程=cki[2]
					else:
						if s.将上课程[课程天_[课程天_k]]:
							课程天_k_=课程天_k
							年,月=divmod(课程天_[课程天_k],10000)
							月,日=divmod(月,100)
							日期_s=str(日)+'日'
							if 日==1:
								日期_s=str(月)+'月'+日期_s
								if 月==1:
									日期_s=str(年)+'年'+日期_s
							cki=[['',''],日期_s,'']
						else:
							continue
					s.课程表qbox[i].设置内容(cki[0][1],cki[1],cki[2])
					break

			#总数=sum([len(s.将上课程[i]) for i in s.将上课程])
			#if 总数-已上课数<len(s.课程表qbox):
			#	s.start()
				#return

			if 需要更新:
				if not 天 in s.将上课程:
					input()
				已上课数_,上课,s.倒计时_,暂停=dk(tl,s.将上课程[天],False)
				s.状态['已上课数']=已上课数_
				s.状态['当前课程']=当前课程

				#s.暂停=暂停

			s.状态['上课']=上课
		
			s.上课状态.setText(上课_[上课])
			s.上课状态.setStyleSheet('color:'+('#00ff00','#ffff00','#ff0000')[上课])
			
			#s.adjustSize_()
		if s.倒计时_ is not None:
			m=s.倒计时_-秒
		else:
			m=0
		s.上课状态d.setText(时间转文字(m)if m else '')

		return m

		##需要两次
		#s.adjustSize_()
		

		
		#print(d[2])
		#s.课程定时器.start(d[2]*1000)

	def gxsj(s):
		s.更新时间()
	def 更新时间(s):
		tl=time.localtime(获取时间())
		#time.strftime("%Y年%m月%d日",tl)
		s.日期时间.设置内容(time.strftime("%H:%M:%S",tl),time.strftime("%Y/%m/%d",tl),'星期'+星期_tm_wday[tl.tm_wday])
		#s.时间.setText(time.strftime("%Y-%m-%d %H:%M:%S",))
	
	class 更新线程(QThread):
		pass
	
	'''
	def stop(s):
		if s.timer_id:
			s.killTimer(s.timer_id)
			s.timer_id=0

		'''
	
	def scjc(s):
		s.时差检查()
	def 时差检查(s):
		t=time.time()
		if t - s.时差_>50:
			s.start(True)
		s.时差_=t

	def s(s):
		s.时差检查()
		s.时差检查定时器.start()

class 单天气组件(QVBoxLayout):
	def __init__(s,数量=3):
		super().__init__()
		#s.setSpacing(3)
		s.labels=[QLabel()for i in range(数量)]
		for i in s.labels:
			i.setFont(QFont("黑体",16))
			i.setStyleSheet('color:#ffffff')
			s.addWidget(i)
			i.setAlignment(Qt.AlignmentFlag.AlignCenter)
			'''
		s.labels[0].setFont(QFont("黑体",18,QFont.Weight.Bold))
		s.labels[1].setFont(QFont("黑体",20))
		s.labels[2].setFont(QFont("黑体",20,QFont.Weight.Bold))
		'''

	def 设置内容(s,*a):
		for i in range(len(a)):
			s.labels[i].setText(str(a[i]))


class 天气获取t_(QThread):
	trigger=pyqtSignal(dict)
	def __init__(s):
		super().__init__()
	def run(s):
			try:
				uo=request.urlopen('http://api.openweathermap.org/data/2.5/onecall?exclude=minutely&units=metric&lang=zh_cn&lat='+str(配置l['天气']['纬度'])+'&lon='+str(配置l['天气']['经度'])+'&appid='+配置l['天气']['key'])
				jl=json.load(uo)
				s.trigger.emit(jl)
			except BaseException as e:
				print('更新天气失败,'+str(e))

class 天气获取t(threading.Thread):
	#trigger=pyqtSignal(dict)
	def __init__(s,parent):
		super().__init__()
		s.parent:天气组件=parent
	def 获取并发送(s):
		s.t_=天气获取t_()
		s.t_.trigger.connect(s.parent.gxtq)
		s.t_.start()
		print('更新天气')
	
	def run(s):
		s.获取并发送()
		#s.setVisible(True)

		while 1:
			a=0
			#time.sleep(60)
			while a<60:
				time.sleep(1)
				a+=1
				显示_当前=s.parent.isVisible()
				if s.parent.显示!=显示_当前:
					if 显示_当前 or s.parent.当前信息_更新时间.text():
						print('天气_'+str(s.parent.显示))
						s.parent.setVisible(s.parent.显示)

				if s.parent.预更新:
					s.parent.预更新=False
					s.获取并发送()

			if s.parent.isVisible():
				s.获取并发送()


class 天气组件(QWidget):
	def __init__(s, parent=None):
		super().__init__(parent)

		s.预更新=False
		s.显示=False
		s.setVisible(False)

		s.setFont(QFont("黑体",18,QFont.Weight.Bold))

		s.根纵=QVBoxLayout()
		s.setLayout(s.根纵)


		s.当前信息=QHBoxLayout()

		#s.每分钟信息hbox=QHBoxLayout()
		#s.每分钟信息l=[]

		s.每小时信息hbox=QHBoxLayout()
		s.每小时信息l=[]
		
		s.每天信息hbox=QHBoxLayout()
		s.每天信息l=[]

		
		s.根纵.addLayout(s.当前信息)
		'''
		填空=QLabel()
		填空.setText(' ')
		s.根纵.addWidget(填空)
		s.根纵.addLayout(s.每分钟信息hbox)
		'''
		s.根纵.addWidget(QLabel(' '))
		s.根纵.addLayout(s.每小时信息hbox)
		填空=QLabel()
		s.根纵.addWidget(QLabel(' '))
		s.根纵.addLayout(s.每天信息hbox)

		#(s.每分钟信息hbox,s.每分钟信息l,25,2),
		for i in ((s.每小时信息hbox,s.每小时信息l,12,4),(s.每天信息hbox,s.每天信息l,7,4)):
			for i2 in range(i[2]+1):
				i_=单天气组件(i[3])
					
				填空=QLabel()
				填空.setText(' ')
				i[0].addWidget(填空)

				i[0].addLayout(i_)
				i[1].append(i_)

		#s.每分钟信息l.pop(0).设置内容('时间(分)','降水量(毫米)')
		s.每小时信息l.pop(0).设置内容('时间(时)','天气','降水概率(%)','温度(°C)')
		s.每天信息l.pop(0).设置内容('时间(天)','天气','降水概率(%)','最值温度(°C)')

		当前信息_更新时间0=QLabel()
		当前信息_更新时间0.setText('更新时间:')
		s.当前信息.addWidget(当前信息_更新时间0)
		s.当前信息_更新时间=QLabel()
		s.当前信息.addWidget(s.当前信息_更新时间)
		当前信息_更新时间1=QLabel()
		当前信息_更新时间1.setText(' ')
		s.当前信息.addWidget(当前信息_更新时间1)
		
		当前信息_天气0=QLabel()
		#当前信息_天气0.setText('天气:')
		s.当前信息.addWidget(当前信息_天气0)
		s.当前信息_天气=QLabel()
		s.当前信息.addWidget(s.当前信息_天气)
		当前信息_天气1=QLabel()
		当前信息_天气1.setText('')
		s.当前信息.addWidget(当前信息_天气1)

		当前信息_温度0=QLabel()
		#当前信息_温度0.setText('温度:')
		s.当前信息.addWidget(当前信息_温度0)
		s.当前信息_温度=QLabel()
		s.当前信息.addWidget(s.当前信息_温度)
		当前信息_温度1=QLabel()
		当前信息_温度1.setText('°C ')
		#当前信息_温度1.setStyleSheet('letter-spacing:1px')
		s.当前信息.addWidget(当前信息_温度1)

		当前信息_湿度0=QLabel()
		当前信息_湿度0.setText(' 湿度')
		s.当前信息.addWidget(当前信息_湿度0)
		s.当前信息_湿度=QLabel()
		s.当前信息.addWidget(s.当前信息_湿度)
		当前信息_湿度1=QLabel()
		当前信息_湿度1.setText('% ')
		s.当前信息.addWidget(当前信息_湿度1)
		
		当前信息_风速0=QLabel()
		#当前信息_风速0.setText(' 风速:')
		s.当前信息.addWidget(当前信息_风速0)
		s.当前信息_风速=QLabel()
		s.当前信息.addWidget(s.当前信息_风速)
		当前信息_风速1=QLabel()
		当前信息_风速1.setText(' ')
		s.当前信息.addWidget(当前信息_风速1)
		'''
		当前信息_a3d0=QLabel()
		当前信息_a3d0.setText('a3d:')
		s.当前信息.addWidget(当前信息_a3d0)
		s.当前信息_a3d=QLabel()
		s.当前信息.addWidget(s.当前信息_a3d)
		当前信息_a3d1=QLabel()
		当前信息_a3d1.setText(' ')
		s.当前信息.addWidget(当前信息_a3d1)
		'''
		#'''
		for i in (
			当前信息_更新时间0,s.当前信息_更新时间,当前信息_更新时间1,\
			当前信息_天气0,s.当前信息_天气,当前信息_天气1,\
			当前信息_温度0,s.当前信息_温度,当前信息_温度1,\
			当前信息_湿度0,s.当前信息_湿度,当前信息_湿度1,\
			当前信息_风速0,s.当前信息_风速,当前信息_风速1
		):
			i.setFont(QFont("黑体",18,QFont.Weight.Bold))
			#'''

		s.当前信息.addStretch(1)
		#s.每分钟信息hbox.addStretch(1)
		s.每小时信息hbox.addStretch(1)
		s.每天信息hbox.addStretch(1)

		'''
		s.小时_=[]
		s.小时=[]
		for i in range(2):
			i1=QVBoxLayout()
			s.小时_.append(i1)
			s.根纵.addLayout(i1)
			for i2 in range(6):
				i2_=QWidget()
				s.小时.append(i2_)
				i1.addWidget(i2_)
		
		s.小时2=QVBoxLayout()
		'''
	
	def gxtq(s,*a):
		s.更新天气(*a)
	def 更新天气(s,天气j):
		当前天气_=天气j['current']
		#每分钟天气_=天气j['minutely']
		每小时天气_=天气j['hourly']
		每天天气_=天气j['daily']
		s.当前信息_更新时间.setText(time.strftime("%H:%M:%S",time.localtime(当前天气_['dt'])))
		s.当前信息_天气.setText(当前天气_['weather'][0]['description'])
		s.当前信息_温度.setText(str(当前天气_['temp']))
		s.当前信息_湿度.setText(str(当前天气_['humidity']))
		风速_=''
		风向=当前天气_['wind_deg']
		if 30<风向<150:
			风速_+='东'
		elif 210<风向<330:
			风速_+='西'

		if 风向<60 or 300<风向:
			风速_+='北'
		elif 120<风向<240:
			风速_+='南'

		风速_+='风 '+str(当前天气_['wind_speed'])+'米/秒'
		s.当前信息_风速.setText(风速_)

		'''
		i2=1
		for i in range(len(s.每分钟信息l)):
			if len(每分钟天气_)>i2:
				i3=每分钟天气_[i2]
				s.每分钟信息l[i].设置内容(time.strftime("%M",time.localtime(i3['dt'])),i3['precipitation'])
				i2+=3
			else:
				break
		'''	

		i2=1
		for i in range(len(s.每小时信息l)):
			if len(每小时天气_)>i2:
				i3=每小时天气_[i2]
				s.每小时信息l[i].设置内容(time.strftime("%H",time.localtime(i3['dt'])),i3['weather'][0]["description"],str(round(i3['pop']*100)),i3['temp'])
				i2+=2
			else:
				break
				

		i2=1
		for i in range(len(s.每天信息l)):
			if len(每天天气_)>i2:
				i3=每天天气_[i2]
				温度=i3['temp']
				s.每天信息l[i].设置内容(time.strftime("%d",time.localtime(i3['dt'])),i3['weather'][0]["description"],str(round(i3['pop']*100)),str(温度['min'])+'/'+str(温度['max']))
				i2+=1
			else:
				break
				
		#s.adjustSize()

	def l(s):
			s.获取t=天气获取t(s)
			#s.获取t.trigger.connect(s.gxtq)
			s.获取t.start()

class 单日期组件(QVBoxLayout):
	def __init__(s):
		super().__init__()
		#s.setSpacing(3)
		s.labels=[QLabel()for i in range(2)]
		for i in s.labels:
			#i.setFont(QFont("黑体",16))
			i.setStyleSheet('color:#ffffff')
			s.addWidget(i)
			i.setAlignment(Qt.AlignmentFlag.AlignCenter)
		s.labels[0].setFont(QFont("黑体",16))
		s.labels[1].setFont(QFont("黑体",8))
		'''
		s.labels[2].setFont(QFont("黑体",20,QFont.Weight.Bold))
		'''

	def 设置内容(s,*a):
		for i in range(len(a)):
			s.labels[i].setText(str(a[i]))

class 单日期组件(QWidget):
	def __init__(s):
		super().__init__()

		s.根纵=QVBoxLayout()
		s.setLayout(s.根纵)

		s.根纵_上=QHBoxLayout()

		s.左上=QLabel()
		s.左上.setStyleSheet('line-height:0px')
		s.左上.setFont(QFont("黑体",12))
		s.根纵_上.addWidget(s.左上)

		s.根纵_上.addStretch(1)

		s.右上=QLabel()
		s.右上.setFont(QFont("黑体",12))
		s.根纵_上.addWidget(s.右上)
		
		s.根纵.addLayout(s.根纵_上)

		s.根纵_中=QHBoxLayout()
		s.根纵_中.addStretch(1)
		s.日期=QLabel()
		s.日期.setFont(QFont("黑体",16))
		s.根纵_中.addWidget(s.日期)
		s.根纵_中.addStretch(1)
		s.根纵.addLayout(s.根纵_中)

		s.底部=QLabel()
		
		s.底部.setAlignment(Qt.AlignmentFlag.AlignCenter)
		s.底部.setFont(QFont("黑体",12))
		s.根纵.addWidget(s.底部)


	def 设置内容(s,左上,右上,日期,底部):
		s.左上.setText(左上)
		s.右上.setText(右上)
		s.日期.setText(日期)
		s.底部.setText(底部)


class 日历组件(QWidget):
	def __init__(s,*a):
		super().__init__(*a)
		s.根网=QGridLayout()
		s.setLayout(s.根网)
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
	
	def 更新日期(s):
		d=日期.日期()
		节假日=获取节假日()
		for i in s.日期_qws:
			星期历=日期.星期历(d)#参数 d 在调用后会被改变
			for i2 in range(7):
				日期_:日期.日期=星期历[i2]
				年,月,日=日期_.公历_值
				左上=(str(月)+'月') if 日==1 else ''
				try:
					右上=节假日_文本[ 节假日[str(年)][str(月)][str(日)] ]
					
				except KeyError:
					右上=''
				i[i2].设置内容(左上,右上,str(日),日期_.简日())





class 倒计时组件(QLabel):
	def __init__(s,parent=None,时间=0,文本_结束='',文本_前='',文本_后=''):
		super().__init__(parent)
		s.文本_前=文本_前
		s.文本_后=文本_后
		s.文本_结束=文本_结束
		s.时间=时间
		s.已隐藏=False

		s.定时器=QTimer(s)
		s.定时器.setTimerType(Qt.TimerType.PreciseTimer)
		s.定时器.timeout.connect(s.gx)
		s.定时器.setInterval(1000)
	def 设置隐藏(s,v):
		if s.已隐藏:
			s.定时器.stop()
			s.setText('')
		else:
			s.开始()

	def gx(s):
		s.更新()
	def 更新(s,t=None):
		if not t:
			t=time.time()
		t_=s.时间-t
		if t_>0:
			s.setText(s.文本_前+时间转文字(t_)+s.文本_后)
		else:
			s.setText(s.文本_结束)
			s.定时器.stop()

	def 开始(s):
		time.sleep(1.001-(时差+time.time())%1)
		s.定时器.start()

class 单消息组件(QLabel):
	def __init__(s,parent=None,标题=None,内容=None):
		super().__init__(parent)
		s.setWordWrap(True)
		s.修改(内容,标题)
	
	def 修改(s,内容=None,标题=None):
		s.setText(('<h3>'+str(标题)+'</h3>' if 标题 else '')+('<p>'+str(内容)+'</p>' if 内容 else ''))

class 视频获取(QThread):
	trigger=pyqtSignal(tuple)
	def __init__(s,宽,高,args,parent=None):
		super().__init__(parent)
		s.宽=宽
		s.高=高
		s.args=args
	def run(s):
		s.视频来源=获取视频.背景()
		s.l=s.视频来源.整理(宽高=(s.宽,s.高))
		s.trigger.emit((s.l,s.args))
	def 整理(s,宽,高):
		return s.视频来源.整理(宽高=(宽,高))


class 背景视频组件(QVideoWidget):
	def __init__(s,parent=None,启用背景动画=False):
		super().__init__(parent)
		s.setWindowFlags(Qt.WindowType.WindowStaysOnBottomHint|Qt.WindowType.FramelessWindowHint|Qt.WindowType.MSWindowsFixedSizeDialogHint)
		#s.move(-999,-999)
		#s.resize(1,1)
		#s.show()
		#s.resize(1,1)

		s.宽=0
		s.高=0

		s.启用背景动画=启用背景动画

		s.显示状态=False
		s.背景_入=None
		s.背景_出=None
		s.初始=True
		s.l=None
		#s.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
		s.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatioByExpanding)#将视频等比填满

		s.player=QMediaPlayer()
		s.player.setVideoOutput(s)
		#循环播放
		s.player.setLoops(QMediaPlayer.Loops.Infinite)
		#尝试其他方法
		
		if s.启用背景动画:
			s.setWindowOpacity(0.01)
		else:
			s.setVisible(False)
		s.背景动画_时间=1000
		s.背景动画_入=QPropertyAnimation(s,b'windowOpacity')
		s.背景动画_入.setEasingCurve(QEasingCurve.Type.InCubic)#动画曲线
		s.背景动画_入.finished.connect(s.bjdh_js)
		s.背景动画_入.setDuration(s.背景动画_时间)
		s.背景动画_入.setStartValue(0)
		s.背景动画_入.setEndValue(1)
		'''
		s.背景动画_入.setStartValue(0.01)
		s.背景动画_入.setEndValue(0.9999)
		'''
	
	def zbsp_q(s,l_):
		s.l=l_[0]
		s.准备视频(*l_[1])
		s.player.play()
	
	def 准备视频(s,i=None):
		#新线程(0,s.player.play)
		#'''
		if not s.l:
			s.获取_线程=视频获取(s.宽,s.高,(i,))
			s.获取_线程.trigger.connect(s.zbsp_q)
			s.获取_线程.start()
			return
		重播=False
		#l=s.视频来源.整理(2160)
		#i=5
		if not i:
			i=配置l['视频背景']['项']
		else:
			i=i%len(s.l)
			if 配置l['视频背景']['项']!=i:
				配置l['视频背景']['项']=i
				配置l.写()
				if s.显示状态:
					重播=True
					s.出()
					
		qurl_=QUrl(s.l[i][3])
		#qurl_=QUrl('file:///D:/Downloads/北京2022冬奥会开幕式_末尾_.mp4')
		s.qurl_=qurl_
		if 重播:
			s.初始=True
			s.背景_出=s.重设媒体
		else:
			s.player.setSource(qurl_)
			s.背景_出=None

	def 重设媒体(s):
		s.背景_出=None
		s.player.stop()
		s.player.setSource(s.qurl_)
		s.player.play()


	def bjdh_js(s):#背景动画_结束
		s.背景动画_入.stop()
		if not s.显示状态:#出 之后
			s.player.pause()
			if callable(s.背景_出):
				s.背景_出()
		
	def 入(s):
		if not s.显示状态:
			s.显示状态=True
			s.player.play()
			if s.启用背景动画:
				s.背景动画_入.setDirection(QAbstractAnimation.Direction.Forward)
				s.背景动画_入.start()
				if callable(s.背景_入):
					s.背景_入()
			else:
				s.setVisible(True)
	def 出(s):
		if s.显示状态:
			s.显示状态=False
			if s.启用背景动画:
				s.背景动画_入.setDirection(QAbstractAnimation.Direction.Backward)
				s.背景动画_入.start()
				#s.背景动画_入.finished.connect()
			else:
				s.setVisible(False)
				s.player.pause()


	def 显示(s):
		
		#s.setVisible(False)
		#s.背景动画_.start()
		s.准备视频()
		s.初始=True
		s.player.play()

		#s.入()
		#if s.player.MediaStatus()!=6 and s.player.state()==0:
		s.player.mediaStatusChanged.connect(s.mediaStatusChanged__)
		
	
	def mediaStatusChanged__(s,状态):
		if 状态==QMediaPlayer.MediaStatus.BufferedMedia:#qt6和qt5的状态不同
			if s.初始:
				s.初始=False
				s.入()
		
class 背景组件():
	#用于视频不能正常淡入时的魔改
	#过程:
	#在视频刚创建时就把它移到屏幕外.
	#视频就绪后, 可以正常淡入淡出.
	#视频就绪后, 调用 背景初入 将视频移入, 就能正常淡入.

	#不要堵塞qt的线程, 会可能会使背景变黑, 影响淡入淡出和视频播放.
	def __init__(s):
		s.视频=背景视频组件(启用背景动画=True)
		s.视频.setGeometry(-1,-1,1,1)
		s.宽高=[0,0]
		s.视频.lower()
		s.视频.背景_入=s.背景初入

	def 背景初入(s):
		s.视频.背景_入=None
		s.视频.setGeometry(0,0,*s.宽高)




class 主窗口(QWidget):
	def __init__(s, parent=None):
		super().__init__(parent)
		s.托盘=托盘图标(s)
		s.win=QWidget(s)
		s.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)#透明背景
		s.setWindowFlags(Qt.WindowType.FramelessWindowHint|Qt.WindowType.MSWindowsFixedSizeDialogHint)
		#s.setWindowFlags(Qt.WindowStaysOnBottomHint|Qt.FramelessWindowHint|Qt.MSWindowsFixedSizeDialogHint)
		s.time=0
		s.setStyleSheet('*{color:#ffffff}')

		s.setFont(QFont("黑体",18,QFont.Weight.Bold))

		s.套背景=True
		if s.套背景:
			s.背景=背景组件()
			s.背景视频=s.背景.视频
		else:
			s.背景视频=背景视频组件(启用背景动画=True)

		s.winid_s=int(s.winId())
		s.winid_win=int(s.win.winId())
		s.winid_背景视频=int(s.背景视频.winId())


		s.宽=0
		s.高=0

		s.sm_t=0
		s.上课状态=None
		s.下课预更新=None

		s.嵌入_继续=None

		s.状态检查定时器=QTimer(s)
		s.状态检查定时器.timeout.connect(s.ztjc)
		s.状态检查定时器.setInterval(1000)

		s.秒定时器=QTimer(s)
		s.秒定时器.setTimerType(Qt.TimerType.PreciseTimer)
		s.秒定时器.timeout.connect(s.miao)
		s.秒定时器.setInterval(1000)

		s.根横=QHBoxLayout()

		s.根横_纵左=QVBoxLayout()
		s.根横_纵右=QVBoxLayout()

		s.根横.addLayout(s.根横_纵左)
		s.根横.addStretch(1)
		s.根横.addLayout(s.根横_纵右)

		#s.学考倒计时=倒计时组件(None,1641686400,'','学考倒计时 ')
		#s.学考倒计时.setFont(QFont("黑体",30,QFont.Weight.Bold))
		#s.学考倒计时.setStyleSheet('color:#ffffff')

		#s.根横_纵左.addWidget(s.学考倒计时)
		'''
		s.消息l=[]
		s.消息d={}
		for i in range(5):
			i2=单消息组件()
			s.消息l.append(i2)
			s.根横_纵左.addWidget(i2)
		#'''
		s.根横_纵左.addStretch(1)
		
		s.纵右_课程表=QHBoxLayout()
		s.纵右_课程表.addStretch(1)
		s.课程表=课程表组件()
		s.纵右_课程表.addWidget(s.课程表)
		s.根横_纵右.addLayout(s.纵右_课程表)

		s.纵右_日历=QHBoxLayout()
		s.纵右_日历.addStretch(1)
		s.日历=日历组件()
		s.日历.setVisible(False)
		s.纵右_日历.addWidget(s.日历)
		s.根横_纵右.addLayout(s.纵右_日历)
		#s.日历.更新日期()

		#a=QLabel()
		#a.setText('123')
		#s.根横_纵右.addWidget(a)

		s.天气=天气组件()
		s.根横_纵右.addWidget(s.天气)

		s.根横_纵右.addStretch(1)
		s.win.setLayout(s.根横)

	def 添加消息(s,xid=None):
		if not xid:
			xid=int(time.time()*1024)
		elif xid in s.消息d:
			i=s.消息d[xid]
		s.消息d
		s.消息l

	def 对齐桌面(s):
		d=QApplication.primaryScreen().geometry()
		宽,高=d.width(),d.height()
		if s.宽==宽 and s.高==高:
			return
		s.宽=s.背景视频.宽=宽 ; s.高=s.背景视频.高=高
		#s.resize(宽,高)
		#s.win.resize(宽,高)
		#s.背景_图片.resize(宽,高)
		#s.move(0,0)
		s.setGeometry(0,0,宽,高)
		s.win.setGeometry(0,0,宽,高)
		#s.背景.resize(宽,高)
			
		if (not s.套背景)or not s.背景视频.背景_入:
			s.背景视频.setGeometry(0,0,宽,高)
			if s.套背景:
				s.背景.背景图片.setGeometry(0,0,宽,高)
		else:
			s.背景.宽高=[宽,高]
		#s.背景.move(0,0)


	'''
	def co1(s,i):
		s.嵌入_错误_提示_按钮点击(s,i)
	def 嵌入_错误_提示_按钮点击(s,i):
		if i==QMessageBox.Retry:
			s.嵌入_继续=1
		else:
			print(i)
			s.嵌入_继续=2
'''
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
					s.托盘.showMessage('初始化错误','找不到桌面窗口, 尝试重启 explorer.exe 可能会解决问题',QSystemTrayIcon.MessageIcon.Information,10000)
					#s.托盘.messageClicked.connect(
					#	lambda:QMessageBox.information(
					#		'错误','找不到桌面窗口',QMessageBox.Retry|QMessageBox.Abort,QMessageBox.Retry
					#	).buttonClicked.connect(s.co1)
					#)
				
				time.sleep(1)


		#将窗口设为桌面背景的子窗口
		win32gui.SetParent(s.winid_s,s.winid_桌面)
		#'''
		win32gui.SetParent(s.winid_背景视频,s.winid_桌面)
		#'''
		#玄学,需要将内容再放到一个子窗口中, 再将子窗口设为窗口的将子窗口
		win32gui.SetParent(s.winid_win,s.winid_s)

		
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
			s.update()
			s.嵌入()

	def miao(s):
		pass

	def sm(s):
		while 1:
			s.课程表.更新时间()
			#s.学考倒计时.更新()
			if 多延迟:
				time.sleep(1-(时差+time.time())%1)
			倒计时_=s.课程表.更新课程()
			#if (not 上课)or 当前课程 in('历史','政治','自习')or '学考'in 当前课程:
			#	pass
			上课状态=s.课程表.状态['上课']
			if 上课状态!=s.上课状态:
				s.上课状态=上课状态
				if 上课状态:
					s.下课预更新=True
					s.天气.显示=False
					#s.天气.setVisible(False)
				else:
					#s.天气.setVisible(True)
					s.天气.显示=True
			
			if 上课状态==2 and s.下课预更新 and 倒计时_ and 倒计时_<20:
				print('预更新',上课状态,s.下课预更新,倒计时_)
				s.下课预更新=False
				s.天气.预更新=True
			st=time.time()
			if st-s.sm_t>20:
				print(2)
			time.sleep(1-st%1)
			s.sm_t=st
		#s.秒定时器.setInterval(1000)
		#s.秒定时器.start()

	
	def 开始(s):
		#s.学考倒计时.开始()
		s.嵌入()
		s.对齐桌面()
		#s.设置背景()
		s.状态检查定时器.start()
		#import threading
		#threading.Thread(target=lambda:()).start()
		#新线程(0,lambda:(s.嵌入(),s.对齐桌面(),s.状态检查()))
		
		#s.背景视频.show()
		#qt
		#win32gui.ShowWindow(s.winid_背景视频,win32con.SW_HIDE)
		#win32gui.SetWindowPos(s.winid_背景图片,win32con.HWND_TOP,0,0,0,0,win32con.SWP_NOMOVE|win32con.SWP_NOSIZE)
		#win32gui.SetWindowPos(s.winid_背景视频,win32con.HWND_BOTTOM,0,0,0,0,win32con.SWP_NOMOVE|win32con.SWP_NOSIZE)
		#s.show()
		#'''
		#s.背景动画_入.start()
		#s.背景.show()
		#s.背景视频.show()
		'''
		s.背景视频.show()
		s.背景视频.显示()
		#'''
		
		#_thread.start_new_thread(s.player.play,())
		#'''
		s.show()
		s.课程表.start(True)
		#import threading
		#t=threading.Thread(target=s.sm)
		#t.start()
		
		#新线程(0,s.sm)
		threading.Thread(target=s.sm).start()
		#_thread.start_new_thread(s.sm,())
		#'''
		if 配置l['天气']['key']:
			s.天气.l()
		else:
			print('未配置天气')
		#'''
		#s.天气.更新天气()

class 托盘图标(QSystemTrayIcon):
	def __init__(s,parent=None):
		super().__init__()
		s.主窗口:主窗口=parent
		s.setIcon(QIcon('icon.png'))
		s.setToolTip('桌面背景')
		#s.activated.connect(s.点击)
		s.setVisible(True)
		s.menu=QMenu()


		s.menu.addAction('上一张').triggered.connect(s.sp_s)
		s.menu.addAction('下一张').triggered.connect(s.sp_x)
		s.menu.addAction('退出').triggered.connect(s.tc)
		s.setContextMenu(s.menu)
		s.show()
		#s.setVisible(True)
	def 点击(s):
		pass
	
	def 视频_更换(s,项=None,变化=None):
		if not 项:
			if not 变化:
				raise
			else:
				项=配置l['视频背景']['项']+变化
		
		s.主窗口.背景视频.准备视频(项)

	def sp_s(s):
		s.视频_更换(变化=-1)

	def sp_x(s):
		s.视频_更换(变化=1)

	def tc(s):
		s.退出()
	def 退出(s):
		s.setVisible(False)
		#s.deleteLater()
		s.主窗口.背景视频.出()
		if s.主窗口.背景视频.启用背景动画:
			新线程(s.主窗口.背景视频.背景动画_时间/1000+0.5,s.退出_)
		else:
			s.退出_()
		#sys.exit()

	def 退出_(s):
		app.exit()
		#sys.exit()


if __name__ == "__main__":

	配置l=flj('配置.json')

	if not 配置l.d:
		配置l.关闭()
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
		},
		'天气':{
			'启用':True,
			'经度':0,
			'纬度':0,
			'key':''
		}
		
	})

	时差=配置l['课程表']['时差']
	#t_6=配置l['周六时间']

	w=主窗口()

	ti=QSystemTrayIcon(w)

	#'''
	'''

	tim=QMenu()
	tim.addAction(QAction('&退出(Exit)',ti,triggered=lambda:(ti.setVisible(False),w.背景视频.出(),新线程(4,app.quit))))
	ti.setContextMenu(tim)
	icon=QIcon('icon.png')
	#icon.addPixmap(QPixmap.loadFromData('iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9TS0UqDnYQcchQnSyIFhFcpIpFsFDaCq06mFz6BU0akhQXR8G14ODHYtXBxVlXB1dBEPwAcXRyUnSREv+XFFrEeHDcj3f3HnfvAKFZZarZMwGommWkE3Exl18Vg68Q4EcAs4hJzNSTmcUsPMfXPXx8vYvyLO9zf45+pWAywCcSzzHdsIg3iKc3LZ3zPnGYlSWF+Jx43KALEj9yXXb5jXPJYYFnho1sep44TCyWuljuYlY2VOIYcURRNcoXci4rnLc4q9U6a9+TvzBU0FYyXKc5ggSWkEQKImTUUUEVFqK0aqSYSNN+3MM/7PhT5JLJVQEjxwJqUCE5fvA/+N2tWZyadJNCcSDwYtsfo0BwF2g1bPv72LZbJ4D/GbjSOv5aE5j5JL3R0SJHwMA2cHHd0eQ94HIHGHrSJUNyJD9NoVgE3s/om/LA4C3Qt+b21t7H6QOQpa6Wb4CDQ2CsRNnrHu/u7e7t3zPt/n4AvP9yxa0hWoIAAAAGYktHRAAAAAAAAPlDu38AAAAJcEhZcwAALiMAAC4jAXilP3YAAAAHdElNRQfmAgMGDzjPq3ZSAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAlZJREFUeNrtmj1rVFEQhp/R2GiUSPxIRC5qoUEETdIIBhEstLIOFloYO3+E+DfcSkHr7QKC1UIC4kastBFcgq4f0WhwBZvXZm44WXazIVrkcOeFZefOuffuzsPcmTnLQigUCoVCoVComrJ161FblYr81phtdFQJQBLrrtxjkTQradjtYUmzbk9JuilparPrh3ZYMAIwM+uyX7o9LWkOeNjj2tR+6mYHeANMZwHAzKyXDdxN/DWg1hX8XI971bbymUM5pLmZNQes17Z77+xrwL8qAASAimuntcEJ4Cqw7MWt7r5UZ5LiV5c0Dpwzs2eSJn2pAFpAYWb1nLpAC6gDv7t8qb70gXfH+z7AbmAEaGSVAWbWSYJY90ka7RP0KDAGfPXXhA8+BfDazFaymwOSND4J3AA+JMungcc9sqZU298bwIxnU3aD0FvgGnAbaAJPgG++NgN8Ai4Bz4Fyzt/rmVBCGAFO5ToJnvcvf98DPOv+Y8A94AXwA7gCvANOAJ+BV8Bqmg2SJs1sKSsAZrYg6QjQMrOlrud/wTPgT9oJknpQdoDCM6Kd617gKPBA0qIfHwS+A4e6zjvsu8D9wJr71oBF4FfyWGQHYB/wMTl+DxzwNE+1nMA57r6LwAXvCp2cd4N7gJ99ZoEy1S97oOPJOfP++Kz4bJAlgLKgtZJgu9XYQp9vDiqEOxXAqg81m6mQVAw457q/5wXAq///uNV8tjVgUP+O7XAACAABIAAEgAAQAAJAAAgAASAABIAAEAACQAAIANvSxt8Eq/Z32VAoFAqFQqFQhfUX3qDIplPG4R4AAAAASUVORK5CYII='))
	ti.setIcon(icon)
	ti.show()
	#'''

	w.开始()
	'''
	日历=日历组件()
	日历.更新日期()
	日历.show()
	#'''
	sys.exit(app.exec())