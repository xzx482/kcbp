import toast
import time,sys
import vlc
from .tl_ import tl_

通知器=toast.通知器(toast.application_id)



def 时间转换(t)->str:
	分钟,秒=divmod(int(t),60)
	
		
	return f'{分钟:02}:{秒:02}'





通知0xml="""
<toast scenario="reminder" launch="点击">
	<visual>
		<binding template="ToastGeneric">
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
			content=" 确定"
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
def 退出():
	通知器.清除通知()




通知1xml="""
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



class 通知0_:
	def __init__(s,消息):
		s.消息=消息
		s.通知=toast.通知(
			通知0xml
			.replace('__0__',tl.标题()),
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
		计时=10
		while i<计时:
			if s.状态:
				if s.状态=='取消' or s.状态==-1:
					s.消息.设置(显示=False,结束时间=1)
					退出()
				elif s.状态=='确定' or s.状态=='点击':
					break
			time.sleep(0.2)
			i+=0.2

			通知器.更新通知({"progressValue":str(i/计时),"progressValueString":str(int(计时-i+0.5))+"秒"},0,'通知0')
		
		通知器.清除通知()


class 通知1_:
	def __init__(s,player,audioMedia,消息):
		s.状态=False
		s.player:vlc.MediaPlayer=player
		s.audioMedia:vlc.Media=audioMedia
		s.消息=消息

	def 激活回调(s,参数,获取输入):
		s.状态=参数

	def 关闭回调(s,_,__):
		s.状态=-1

	def 显示(s,z1):
		'''
		z1:
			0:暂停
			1:播放
		'''
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

		time.sleep(1)#若没有等待,总时间会为0
		
		s.总时间=s.audioMedia.get_duration()/1000-20
		s.总时间_文本=时间转换(s.总时间)


		s.状态=False
		s.进度=0
		s.当前时间=0

		s.显示(1)

		while s.当前时间<s.总时间-1:
			if s.状态:
				if s.状态=='暂停':
					s.player.pause()
					s.显示(0)
				elif s.状态=='播放':
					s.player.play()
					s.显示(1)
				elif s.状态==-1 or s.状态=='关闭':
					s.消息.设置(显示=False,结束时间=1)
					退出()
				s.状态=False
			time.sleep(0.5)
			s.当前时间=s.player.get_time()/1000
			s.进度=s.当前时间/s.总时间
			通知器.更新通知({"progressValue":str(s.进度),"progressValueString":时间转换(s.当前时间)+'/'+s.总时间_文本},0,'通知1')
			
		



class 主():
	def __init__(s,p):
		s.tl=tl
		s.消息=p.主消息.添加消息(2)
		s.player:vlc.MediaPlayer=vlc.MediaPlayer()
		s.audioMedia:vlc.Media=vlc.Media(s.tl.文件名())
		s.player.set_media(s.audioMedia)
		s.通知0=通知0_(s.消息)
		s.通知1=通知1_(s.player,s.audioMedia,s.消息)


	def ks(s):
		if tl.是否达到时间():
			tl.加()
		print(tl.文件名())
		s.消息.设置(tl.标题_消息(),tl.内容_消息(),True,time.time()-1,time.time()+20*60)
		s.通知0.循环()
		s.通知1.循环()

def 配置(p,配置l):
	global tl
	tl=tl_(配置l)
	wd=主(p)
	p.wd=wd
	p.ks.connect(wd.ks)