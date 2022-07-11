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
from ctypes import windll

def 已锁定电脑():
		return windll.user32.GetForegroundWindow()% 10 == 0

def 创建通知器():
	global 通知器
	通知器=toast.通知器(toast.application_id)



def 时间转换(t)->str:
	分钟,秒=divmod(int(t),60)
	
		
	return f'{分钟:02}:{秒:02}'


def 获取秒(tl:time.struct_time)->int:
	return (tl.tm_hour*60+tl.tm_min)*60+tl.tm_sec


通知0xml="""
<toast scenario="reminder" launch="点击">
	<visual>
		<binding template="ToastGeneric">
			__1__
			<text>__0__</text>
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
			content="取消"
			arguments="取消"
			activationType="background"/>
	
	</actions>
	<audio silent="true"/>
</toast>
"""

class 退出(Exception):
	pass




通知1xml="""
<toast scenario="reminder" launch="点击">
	<visual>
		<binding template="ToastGeneric">
			<text hint-maxLines="10">__0__</text>
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



class 通知0_:
	def __init__(s,__0__,__1__=''):
		s.需退出=False
		s.通知=toast.通知(
			通知0xml
			.replace('__0__',__0__)
			.replace('__1__',__1__),
			s.激活回调,
			s.关闭回调,
			标签='通知0'
		)
		s.状态=False
	
	def 激活回调(s,参数,获取输入):
		s.状态=参数
	
	def 关闭回调(s,_,__):
		s.状态=-1
	
	def 显示(s):
		s.通知.设置数据({"progressValue":"0","progressValueString":"-","progressStatus":"-"},0)
		通知器.显示(s.通知)

	def 循环(s):
		通知器.清除通知()
		s.显示()
		s.状态=False
		i=0
		计时=20
		while i<计时:
			if s.需退出:
				raise 退出
			if s.状态:
				if s.状态=='取消' or s.状态==-1:
					raise 退出
				elif s.状态=='确定' or s.状态=='点击':
					break
			time.sleep(0.2)
			i+=0.2

			通知器.更新通知({"progressValue":str(i/计时),"progressValueString":str(int(计时-i+0.5))+"秒"},0,'通知0')
		time.sleep(1)
		通知器.清除通知()


class 通知1_:
	def __init__(s,player,audioMedia,消息):
		s.需退出=False
		s.状态=False
		s.player:vlc.MediaPlayer=player
		s.audioMedia:vlc.Media=audioMedia
		s.消息=消息
		s.z1=0

	def 激活回调(s,参数,获取输入):
		s.状态=参数

	def 关闭回调(s,_,__):
		s.状态=-1

	def 显示(s):
		'''
		z1:
			0:暂停
			1:播放
		'''
		z1=s.z1
		通知1=toast.通知(
			通知1xml
			.replace('__0__',tl.标题())
			.replace('__暂停__','暂停' if z1 else '播放'),
			s.激活回调,
			s.关闭回调,
			标签='通知1'
		)
		#通知1.设置数据({"progressValue":str(进度),"progressValueString":str(int(当前时间))+'/'+str(int(总时间))+"秒","progressStatus":"正在播放" if z1 else "已暂停"},0)
		通知1.设置数据({"progressValue":str(s.进度),"progressValueString":时间转换(s.当前时间)+'/'+s.总时间_文本,"progressStatus":"正在播放" if z1 else "已暂停"},0)
		通知器.显示(通知1)

	def 循环(s):
		通知器.清除通知()

		s.player.play()

		总时间=-1
		while 总时间<0:
			总时间=s.audioMedia.get_duration()/1000-20
			time.sleep(0.2)

		s.总时间=总时间



		s.总时间_文本=时间转换(s.总时间)


		s.状态=False
		s.进度=0
		s.当前时间=0

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
				s.状态=False
			time.sleep(0.5)
			s.当前时间=s.player.get_time()/1000
			s.进度=s.当前时间/s.总时间
			通知器.更新通知({"progressValue":str(s.进度),"progressValueString":时间转换(s.当前时间)+'/'+s.总时间_文本},0,'通知1')
			
		
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
		文件名=s.tl.文件名()
		print('wd_.tl:'+文件名)
		player:vlc.MediaPlayer=vlc.MediaPlayer()
		audioMedia:vlc.Media=vlc.Media(文件名)
		player.set_media(audioMedia)
		通知0=通知0_(s.tl.标题())
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

		通知0=通知0_(内容,'<image placement="hero" src="'+图片路径+'"/><text>'+x['title']+'</text>')
		try:
			通知0.循环()
		except 退出:
			通知器.清除通知()
		else:
			try:
				t=time.time()
				while time.time()-t<60:
					if not 已锁定电脑():
						time.sleep(3)
						打开新闻周刊.main(x['url'])
						break
					else:
						print('已锁定电脑')
					time.sleep(1)
					
			except Exception as e:
				print('打开新闻周刊失败:')
				print(e)

	def run(s):
		创建通知器()
		while True:
			time.sleep(1)
			课程表状态=s.主.课程表.状态
			t=time.time()
			#t=time.time()+(1*60-23)*60
			if t-s.配置l['wd_']['时间']>7200 and (18*60+28)*60<获取秒(time.localtime(t))<(18*60+34)*60 and 课程表状态['上课'] and 0<课程表状态['上课']<=2:#时间在18:28-18:34之间 且 预备或者已上课
				s.配置l['wd_']['时间']=t
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