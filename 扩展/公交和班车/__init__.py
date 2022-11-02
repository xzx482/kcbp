import time

from PyQt6.QtGui import QFontMetrics
from kcb_basic import 获取字体,缩放, 获取秒
from PyQt6.QtCore import QThread, Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(__file__))+os.sep+'bc')
from .bc import gj,bc
sys.path.pop()


@gj.重试_倍数延迟_修饰器(8,3)
def gj_打开url_自动重试_失败回调(错误,计数):
	print('公交和班车:网络错误,第'+str(计数)+'次:'+str(错误))

gj.gj_basic.gj_打开url_自动重试_失败回调=gj_打开url_自动重试_失败回调

class 公交查询_线程(QThread):
	gxxx=pyqtSignal(list)#更新信息
	zcxl=pyqtSignal(list)#正常线路
	jfcxl=pyqtSignal(list)#仅发车线路
	jx=pyqtSignal()#就绪
	def __init__(s,p,正常查询器:gj.混合查询器,仅发车时间查询器:gj.混合查询器):
		s.p:实时公交组件=p
		s.正常查询器=正常查询器
		s.仅发车时间查询器=仅发车时间查询器
		s.需获取线路=False
		s.需停止=False
		super().__init__()

	def 获取线路信息(s):
		print('gj:i;获取线路信息')
		i=None # 先声明, 否则可能for循环后i被清理
		for i in s.正常查询器.获取线路信息():
			pass
		if s.需停止:
			return
		s.zcxl.emit(i)
		i=None
		for i in s.仅发车时间查询器.获取线路信息():
			pass
		if s.需停止:
			return
		s.jfcxl.emit(i)
		s.jx.emit()
		s.需获取线路=False

	def 获取并发送(s):
		更新时间_文本=time.strftime('%H:%M:%S')
		print('gj:i;获取公交'+更新时间_文本)
		s.p.更新时间_文本=更新时间_文本
		车辆信息=s.正常查询器.获取车辆信息()
		s.gxxx.emit(车辆信息)

	def run(s):
		s.获取线路信息()
		print('gj:i;公交已就绪')
		s.循环()
		print('gj:e;线程已终止')
	
	def 循环(s):
		while 1:
			if s.需停止:
				break

			if s.需获取线路: # 一般在新的一天时触发
				s.获取线路信息()

			if s.p.预更新 or s.p.显示状态:
				if s.p.预更新:
					print('gj:i;预更新')
					s.p.预更新=False
				s.获取并发送()
				time.sleep(15)
			else:
				time.sleep(10)



class 单发车时间组件(QWidget):
	def __init__(s):
		super().__init__()
		s.setFont(获取字体(15))
		s.setContentsMargins(0,0,0,0)
		s.根纵=QVBoxLayout()
		s.根纵.setSpacing(0)
		s.根纵.setContentsMargins(0,0,0,0)
		s.setLayout(s.根纵)

		s.名称=QLabel()
		s.名称.setText('X路(XX→XXX)')
		s.名称.setFont(获取字体(17))
		s.根纵.addWidget(s.名称)

		s.发车时间=QLabel()
		s.发车时间.setText('发车时间: XX:XX')
		s.发车时间.setFont(获取字体(16))
		s.根纵.addWidget(s.发车时间)

		s.线路信息=None # 线路信息(NamedTuple)[Name,...,发车时间...]

	def 更新发车时间(s):
		f_=gj.获取下次发车时间(time.time(),s.线路信息,2)
		sf=','.join(f_)
	
		s.发车时间.setText('发车时间: '+sf)

	
	def 设置(s,线路信息):
		s.线路信息=线路信息
		s.名称.setText(线路信息.Name.replace('尤溪',''))


单实时公交_列数=3
#列: 距离, 下一站距离, 下一站

class 单实时公交组件(单发车时间组件):
	def __init__(s):
		super().__init__()
		s.目标站点信息=None

		s.下横=QHBoxLayout()
		s.下横.setSpacing(缩放(10))
		s.根纵.addLayout(s.下横)
		s.下横.addSpacing(缩放(20))
		s.信息ls:list[QLabel]=[]
		for i in range(单实时公交_列数):
			i_=QLabel()
			i_.setFont(获取字体(16))
			i_.setTextFormat(Qt.TextFormat.PlainText)
			s.下横.addWidget(i_)
			s.信息ls.append(i_)
		
		s.信息ls[0].setText('XX')
		s.信息ls[1].setText('X')
		s.信息ls[2].setText('XXXXX')

		s.下横.addStretch(1)
		s.fm=QFontMetrics(s.font())
		s.字最大宽度=s.fm.horizontalAdvance('啊啊啊啊啊啊啊啊啊啊啊')
	
	def 缩字(s,文本):
		return s.fm.elidedText(文本,Qt.TextElideMode.ElideRight,s.字最大宽度)
		
	def 设置(s,线路信息,目标站点信息):
		super().设置(线路信息)
		s.目标站点信息=目标站点信息

	def 设置内容(s,车辆信息_:list[gj.gj_basic.车辆信息]):
		
		if not 车辆信息_:
			s.信息ls[0].setText('')
			s.信息ls[1].setText('')
			s.信息ls[2].setText('获取数据失败')
			return

		车辆信息_.sort(key=lambda x:x.站点索引,reverse=True)

		站点信息=s.目标站点信息 # (经度,纬度,索引)

		距离=[]
		下一站距离=[]
		下一站=[]
		计数=0
		已超过站点的车辆=None
		for i in 车辆信息_:
			if 计数>=3:
				break
			if i.站点索引>站点信息[2]:
				已超过站点的车辆=i
				continue
			计数+=1
			距离.append(str(int( gj.gj_basic.经纬度换算(i.经度,i.纬度,站点信息[0],站点信息[1]) /100 )))
			下一站_站点信息:gj.gj_basic.站点信息=s.线路信息.站点[i.站点索引]
			下一站距离.append(str(int( gj.gj_basic.经纬度换算(i.经度,i.纬度,下一站_站点信息.Lon,下一站_站点信息.Lat) /100 )))
			下一站.append(s.缩字(下一站_站点信息.Name))

		距离s='\n'.join(距离)
		下一站距离s='\n'.join(下一站距离)
		if 下一站:
			下一站s='\n'.join(下一站)
		else:
			if 已超过站点的车辆 and 已超过站点的车辆.站点索引-5<站点信息[2]:
				下一站s='已错过, 车辆已驶出'+str(已超过站点的车辆.站点索引-站点信息[2])+'站'
			else:
				下一站s='暂无'

		s.信息ls[0].setText(距离s)
		s.信息ls[1].setText(下一站距离s)
		s.信息ls[2].setText(下一站s)

		



class 实时公交组件(QWidget):
	def __init__(s,p,配置l):
		super().__init__()
		
		s.p=p
		s.配置l=配置l

		s.已就绪=False

		s.目标站点名称=s.配置l['公交和班车']['公交']['站点名称']

		s.单实时公交组件:list[单实时公交组件]=[]
		s.单发车时间组件:list[单发车时间组件]=[]

		for i in range(4):
			s.单实时公交组件.append(单实时公交组件())

		for i in range(3):
			s.单发车时间组件.append(单发车时间组件())

		s.所有组件:list[单发车时间组件]=s.单实时公交组件+s.单发车时间组件

		#二路和三路不能使用gj_0595erp查询器; 其他路只能使用gj_0595erp查询器

		s.正常查询器=gj.混合查询器({
			gj.gj_0595erp.查询器:[["尤溪1路(通演→城西园)","尤溪1路(城西园→通演)"]],

			# 尤溪3路(水东建材广场→玉池); 尤溪3路(玉池→水东建材广场)
			gj.gj_xmpark.查询器:[[('6520cde6f0fb5898d545f9fc3010417e',1),('6520cde6f0fb5898d545f9fc3010417e',2)]]
			#gj.gj_mygolbs.查询器:[[('3路（尤溪）',1),('3路（尤溪）',2)]]
		},
		(0,0,1,1)
		)

		s.仅发车时间查询器=gj.混合查询器({
			gj.gj_0595erp.查询器:[["尤溪6路(火车站→通演)","尤溪8路(火车站→三奎首末站)"]],

			# 尤溪2路(火车站→水东建材广场)
			gj.gj_xmpark.查询器:[[('1a8b189e08d201dc98d783c82e3b2991',2)]]
			#gj.gj_mygolbs.查询器:[[('2路（尤溪）',2)]]
		},
		(1,0,0)
		)

		s.setContentsMargins(缩放(20),缩放(10),0,0)

		s.根纵=QVBoxLayout()
		s.根纵.setContentsMargins(0,0,0,0)
		s.根纵.setSpacing(缩放(10))

		s.上横=QHBoxLayout()
		s.根纵.addLayout(s.上横)
		s.上横.setContentsMargins(0,0,0,0)
		s.上横.setSpacing(0)
		q1=QLabel('公交  更新于')
		q1.setFont(获取字体(13))
		s.上横.addWidget(q1)
		s.更新时间=QLabel()
		s.更新时间.setFont(获取字体(15))
		s.更新时间.setText('很久很久以前')
		s.更新时间_文本=''
		s.上横.addWidget(s.更新时间)
		s.上横.addStretch(1)


		for i in s.所有组件:
			s.根纵.addWidget(i)
		s.根纵.addStretch(1)
		s.setLayout(s.根纵)

		s.显示状态=False
		s.预更新=False

		s.获取t=公交查询_线程(s,s.正常查询器,s.仅发车时间查询器)
		s.获取t.zcxl.connect(s.zcxl)
		s.获取t.jfcxl.connect(s.jfcxl)
		s.获取t.jx.connect(s.jx)
		s.获取t.gxxx.connect(s.gx)

		
		s.淡化动画=p.添加淡化组件(s)
		s.淡化动画.设置脱离主窗口并行(True)

		
	def 是否应显示(s):#未测试的方法-----------------------------------------------------
		#在一节课下课后:
		#若一天的课程没有全部结束, 且离上课还有至少50分钟, 则应显示
		#若一天的课程已经全部结束, 且时间小于18:00, 则应显示
		课程状态=s.p.课程表.状态
		已上课数=课程状态['已上课数']
		一天课程=课程状态['一天课程']
		上课状态=课程状态['上课']

		if 上课状态==2:#已上课, 视为这节课已下课
			已上课数=已上课数+1
		
		时差=s.配置l['课程表']['时差']
		当前秒=获取秒(time.localtime(time.time()+时差))
		if 已上课数>=len(一天课程):#课程已经全部结束
			if 当前秒<(18*60)*60:
				return True
			else:
				return  False
		else:
			下一节课=一天课程[已上课数]
			下一节课上课时间=下一节课[0][0][0]*60
			if 当前秒<下一节课上课时间-50*60:
				return True
			else:
				return False




	def zcxl(s,多个线路信息): # 获取到 正常线路信息 
		for i in range(len(多个线路信息)):
			i_=多个线路信息[i] # 单线路信息
			索引_=0
			for i2 in i_.站点:
				i2:gj.gj_basic.站点信息
				if s.目标站点名称 in i2.Name:
					s.单实时公交组件[i].设置(i_,(i2.Lon,i2.Lat,索引_)) # 对于每个查询器,相同站点的经纬度与其他查询器不同, 分别记录站点信息; 坐标使用wgs84坐标系
					break
				索引_+=1
			else:
				print("gj:e;未找到目标站点")
				s.获取t.需停止=True

	def jfcxl(s,多个线路信息): # 获取到 仅发车线路信息 
		for i in range(len(多个线路信息)):
			s.单发车时间组件[i].设置(多个线路信息[i])
		
	def jx(s):
		s.已就绪=True
		s.更新发车时间()

	def xtsjf(s,tl): # 每一分钟整更新一次
		if s.显示状态:
			if s.是否应显示():
				s.更新发车时间()
			else:
				s.更新显示状态(False)
	
	def xtsjt(s): # 每天更新一次
		s.获取t.需获取线路=True
	
	def 更新发车时间(s):
		if s.已就绪:
			for i in s.所有组件:
				i.更新发车时间()
				
			s.update() # 多次更新后, 字符会叠加在一起, 似乎是之前的内容没有清除, 调用update重绘后可解决
				


	def gx(s,车辆信息_:list[list[gj.gj_basic.车辆信息]]):
		s.更新时间.setText(s.更新时间_文本)
		for i in range(len(车辆信息_)):
			i_=车辆信息_[i]
			s.单实时公交组件[i].设置内容(i_)
		
		s.update()
		

	def ygx(s):
		if s.是否应显示():
			s.预更新=True
			s.更新发车时间()

	def 更新显示状态(s,显示状态):
		if s.显示状态!=显示状态:
			s.显示状态=显示状态
			s.淡化动画.设置方向(显示状态)
			s.淡化动画.start()
		
	def xsztbh(s,显示状态):
		if 显示状态 and s.是否应显示():
			s.更新显示状态(True)
		else:
			s.更新显示状态(False)
	

	def ks(s):
		if s.配置l['公交和班车']['公交']['启用']:
			s.获取t.start()
			s.预更新=False
		else:
			s.setVisible(False)


#
#
# 班车先扔了, 下次再说
#
#


def 配置(p,配置l):
	配置l.添加默认值(
		'公交和班车',
		{
			'公交':{
				'启用':True,
				'站点名称':None
			},
			'班车':{
				'启用':True,
			}
		}
	)
	公交=实时公交组件(p,配置l)
	p.公交=公交
	p.根纵_上横_右纵_横.addWidget(公交)
	p.zjxsztbh.connect(公交.xsztbh)
	p.ygx.connect(公交.ygx)
	p.ks.connect(公交.ks)
	p.线程.xtsjf.connect(公交.xtsjf)
	p.线程.xtsjt.connect(公交.xtsjt)