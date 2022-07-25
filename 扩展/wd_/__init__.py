from dataclasses import replace
import json
import os
from urllib import request
from PyQt6.QtCore import QThread,pyqtSignal
import toast
import time,sys
from . import 打开新闻周刊
import vlc
from .tl_ import tl_
from isLocked import isLocked
from kcb_basic import 获取秒



def 创建通知器():
	global 通知器
	通知器=toast.通知器(toast.application_id)



def 时间转换(t)->str:
	分钟,秒=divmod(int(t),60)
	
		
	return f'{分钟:02}:{秒:02}'



通知0xml_正常="""
<toast scenario="reminder" launch="点击">
	<visual>
		<binding template="ToastGeneric">
			__1__
			<text hint-maxLines="10">__0__</text>
			<progress
				title="即将播放"
				value="{progressValue}"
				valueStringOverride="{progressValueString}"
				status="{progressStatus}"/>
		</binding>
	</visual>
	<actions>
		<action
			content="播放"
			arguments="确定"
			activationType="background"/>

		<action
			content="关闭"
			arguments="取消"
			activationType="background"/>
	
	</actions>
	<audio silent="true"/>
</toast>
"""

通知0xml_锁屏="""
<toast scenario="reminder" launch="点击">
	<visual>
		<binding template="ToastGeneric">
			__1__
			<text hint-maxLines="10">__0__</text>
			<text>解锁电脑后__2__</text>
			<progress
				title="__3__"
				value="{progressValue}"
				valueStringOverride="{progressValueString}"
				status="{progressStatus}"/>
		</binding>
	</visual>
	<actions>
		__4__
	</actions>
	<audio silent="true"/>
</toast>
"""

class 退出(Exception):
	pass




通知1xml_正常="""
<toast scenario="reminder" launch="点击">
	<visual>
		<binding template="ToastGeneric">
			<text>__0__</text>
			<progress
				title="进度"
				value="{progressValue}"
				valueStringOverride="{progressValueString}"
				status="{progressStatus}"/>
		</binding>
	</visual>
	<actions>
		<action
			content="__暂停__"
			arguments="__暂停__"
			activationType="background"/>

		<action
			content="关闭"
			arguments="关闭"
			activationType="background"/>
	
	</actions>
	<audio silent="true"/>
</toast>
"""

通知1xml_锁屏="""
<toast scenario="reminder" launch="点击">
	<visual>
		<binding template="ToastGeneric">
			<text>__0__</text>
			<text>解锁电脑后查看更多\n若要关闭, 点击右上角的×</text>
			<progress
				title="进度"
				value="{progressValue}"
				valueStringOverride="{progressValueString}"
				status="{progressStatus}"/>
		</binding>
	</visual>
	<actions>
	
	</actions>
	<audio silent="true"/>
</toast>
"""


class 通知0_:
	def __init__(s,__0__,__1__='',锁屏时可播放=True):
		if 锁屏时可播放:
			__2__='查看更多\n若要关闭, 点击右上角的×'
			__3__='即将播放'
			__4__=''
		else:
			__2__='才能播放'
			__3__='请解锁电脑'
			__4__='''
				<action
				content="播放"
				arguments="确定"
				activationType="background"/>
				<action
					content="关闭"
					arguments="取消"
					activationType="background"/>
			'''
		s.需退出=False
		s.结束时锁屏则退出=not 锁屏时可播放
		s.通知_正常_xml=(通知0xml_正常
			.replace('__0__',__0__)
			.replace('__1__',__1__)
			#.replace('__2__',__2__)
			.replace('__3__',__3__)
		)
			
		s.通知_锁屏_xml=(
			通知0xml_锁屏
			.replace('__0__',__0__)
			.replace('__1__',__1__)
			.replace('__2__',__2__)
			.replace('__3__',__3__)
		)

		s.状态=False
		s.a=None
	
	def 激活回调(s,参数,获取输入):
		s.状态=参数
	
	def 关闭回调(s,原因):
		if 原因==toast.通知消除原因.超时:
			#在锁屏时点击通知或解锁,会触发此事件; 
			#设置了scenario="reminder"的通知, 正常时应该不会触发此事件
			#当用户解锁后, 会正常触发应触发的事件
			s.状态='重显'
		else:
			s.状态=-1
	
	def 显示(s):
		通知=toast.通知(
			s.通知_锁屏_xml if isLocked() else s.通知_正常_xml
			,
			s.激活回调,
			s.关闭回调,
			标签='通知0'
		)
		通知.设置数据({"progressValue":"0","progressValueString":"-","progressStatus":"-"},0)
		通知器.显示(通知)
	
	def 重显(s):
		通知器.清除通知()
		s.显示()

	def 循环(s):
		通知器.清除通知()
		s.显示()
		s.状态=False
		已锁屏_旧=None
		i=0
		重显计数=0
		计时=20
		while i<计时:
			if s.需退出:
				raise 退出

			if s.状态:
				if s.状态=='取消' or s.状态==-1:
					raise 退出
				elif s.状态=='确定' or s.状态=='点击':
					break
				elif s.状态=='重显':#用户在锁屏页面准备解锁时, 会触发此事件
					重显计数=1
					#通知器.清除通知()
					#s.显示()
					i=0
				s.状态=False
			else:#若用户点击通知而解锁, 会正常触发应触发的事件.若没有触发,则用户没有理睬通知,需要再次显示
				已锁屏=isLocked()
				if 已锁屏_旧 is not None and 已锁屏==True and 已锁屏_旧==False:#锁定时
					重显计数=0
					s.重显()
				已锁屏_旧=已锁屏
				if 重显计数>0 and not 已锁屏:
					重显计数+=1
						
					if 重显计数>=5:#等待几次循环, 以确保系统已经解锁
						重显计数=0
						s.重显()
				
			time.sleep(0.2)
			i+=0.2

			通知器.更新通知({"progressValue":str(i/计时),"progressValueString":str(int(计时-i+0.5))+"秒"},0,'通知0')
		time.sleep(1)
		通知器.清除通知()
		if s.结束时锁屏则退出 and isLocked():
			raise 退出


class 通知1_:
	def __init__(s,player,audioMedia,消息):
		s.需退出=False
		s.状态=False
		s.player:vlc.MediaPlayer=player
		s.audioMedia:vlc.Media=audioMedia
		s.消息=消息
		tl标题=tl.标题()
		s.通知_正常_xml=通知1xml_正常.replace('__0__',tl标题)
		s.通知_锁屏_xml=通知1xml_锁屏.replace('__0__',tl标题)
		s.z1=0

	def 激活回调(s,参数,获取输入):
		s.状态=参数

	def 关闭回调(s,原因):
		if 原因==toast.通知消除原因.超时:
			#在锁屏时点击通知或解锁,会触发此事件; 
			#设置了scenario="reminder"的通知, 正常时应该不会触发此事件
			#当用户解锁后, 会正常触发应触发的事件
			s.状态='重显'
		else:
			s.状态=-1

	def 显示(s):
		'''
		z1:
			0:暂停
			1:播放
		'''
		z1=s.z1
		通知1=toast.通知(
			(s.通知_锁屏_xml if isLocked() else s.通知_正常_xml)
			.replace('__暂停__','暂停' if z1 else '播放'),
			s.激活回调,
			s.关闭回调,
			标签='通知1'
		)
		通知1.设置数据({"progressValue":str(s.进度),"progressValueString":时间转换(s.当前时间)+'/'+s.总时间_文本,"progressStatus":"正在播放" if z1 else "已暂停"},0)
		通知器.显示(通知1)

	def 重显(s):
		通知器.清除通知()
		s.显示()

	def 循环(s):
		通知器.清除通知()

		s.player.play()

		总时间=-1
		for i in range(6):#等待音频就绪
			总时间=s.audioMedia.get_duration()
			if 总时间>0:
				break
			time.sleep(0.4)
		else:
			print('wd_.tl:e;音频加载超时')
			raise 退出('音频无法播放')

		总时间=总时间/1000-20

		s.总时间=总时间



		s.总时间_文本=时间转换(s.总时间)


		s.状态=False
		s.进度=0
		s.当前时间=0
		已锁屏_旧=None
		重显计数=0
		s.z1=1
		s.显示()

		while s.当前时间<s.总时间-1:
			if s.需退出:
				s.player.stop()
				raise 退出
			if s.状态:
				if s.状态=='点击':
					s.显示()
				elif s.状态=='暂停':
					s.player.pause()
					s.z1=0
					s.显示()
				elif s.状态=='播放':
					s.player.play()
					s.z1=1
					s.显示()
				elif s.状态==-1 or s.状态=='关闭':
					s.player.stop()
					raise 退出
				elif s.状态=='重显':
					重显计数=1
				s.状态=False
			else:
				已锁屏=isLocked()
				if 已锁屏_旧 is not None and 已锁屏==True and 已锁屏_旧==False:#锁定时
					重显计数=0
					s.重显()
				已锁屏_旧=已锁屏
				if 重显计数>0 and not 已锁屏:
					重显计数+=1
						
					if 重显计数>=2:
						重显计数=0
						s.重显()

			time.sleep(0.5)
			s.当前时间=s.player.get_time()/1000
			s.进度=s.当前时间/s.总时间
			通知器.更新通知({"progressValue":str(s.进度),"progressValueString":时间转换(s.当前时间)+'/'+s.总时间_文本},0,'通知1')
		s.player.stop()
		通知器.清除通知()
		
		
def 获取新闻周刊():
	t=time.time()
	while time.time()-t<60:
		try:
			return json.load(request.urlopen('https://api.cntv.cn/NewVideo/getVideoListByColumn?id=TOPC1451559180488841&n=1&p=1&mode=0&serviceId=tvcctv'))['data']['list'][0]
		except:
			time.sleep(5)
	raise


class 主(QThread):
	def __init__(s,p,配置l):
		super().__init__()
		s.主=p
		s.配置l=配置l
		s.tl=tl
		s.消息=p.主消息.添加消息(2)


	def bftl(s):
		if s.tl.是否达到时间():
			s.tl.加()
		if not s.tl.是否存在():
			print('wd_.tl:w;不存在指定的目标')
			return
		文件名=s.tl.文件名()
		print('wd_.tl:i;'+文件名)
		player:vlc.MediaPlayer=vlc.MediaPlayer()
		audioMedia:vlc.Media=vlc.Media(文件名)
		player.set_media(audioMedia)
		通知0=通知0_(s.tl.标题(),锁屏时可播放=True)
		通知1=通知1_(player,audioMedia,s.消息)
		s.消息.设置(s.tl.标题_消息(),s.tl.内容_消息(),True,time.time()-1,time.time()+20*60)
		try:
			通知0.循环()
			通知1.循环()
		except 退出:
			s.消息.设置(显示=False,结束时间=1)
			通知器.清除通知()
	

	def bfxwzk(s):
		x=获取新闻周刊()
		if time.time()-x['focus_date']/1000>60*60*24*7:
			return
		图片路径=os.getenv('temp')+'\\'+'xwzk.jpg'
		request.urlretrieve(x['image'],图片路径)
		内容_=x['brief'].replace('\r\n','\n').split('\n')
		内容='\n'.join(内容_[1:4])+'\n.....'

		通知0=通知0_(内容,'<image placement="hero" src="'+图片路径+'"/><text>'+x['title']+'</text>',False)
		try:
			通知0.循环()
		except 退出:
			print('wd_.xwzk:i;退出')
			通知器.清除通知()
		else:
			try:
				打开新闻周刊.main(x['url'])
			except Exception as e:
				print('wd_.xwzk:e;打开新闻周刊失败:')
				print(e)

	def run(s):
		创建通知器()
		while True:
			#'''
			课程表状态=s.主.课程表.状态
			if 课程表状态['上课'] is None:#未就绪
				time.sleep(1)
				continue
			#print('wd_:i;课程表状态:'+str(课程表状态))
			#'''
			t=time.time()
			if t-s.配置l['wd_']['时间']>7200 and (18*60+28)*60<获取秒(time.localtime(t))<(18*60+34)*60 and 课程表状态['上课'] and 0<课程表状态['上课']<=2:#时间在18:28-18:34之间 且 预备或者已上课
				s.配置l['wd_']['时间']=t
				#当前课程='新闻周刊'
				当前课程=课程表状态['当前课程']
				if 当前课程=='新闻周刊':
					s.bfxwzk()
				elif 当前课程=='外语听力':
					s.bftl()
				time.sleep(60)
			time.sleep(10)
			

	def ks(s):
		s.start()
		#s.run()
	


def 配置(p,配置l):
	配置l.添加默认值('wd_',{'启用':False,'时间':0})
	if 配置l['wd_']['启用']:
		global tl
		tl=tl_(配置l)
		wd=主(p,配置l)
		p.wd=wd
		p.ks.connect(wd.ks)