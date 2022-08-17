

class 主():
	def __init__(s,p,配置l):
		s.p=p
		s.淡化动画方向=None
		s.配置l=配置l
		配置l.添加默认值(
			'隐藏下课倒计时',
			{
				'启用':False,
				'课程':[]
			}
		)
		s.l=配置l['隐藏下课倒计时']

		s.所有课程都隐藏=not bool(s.l['课程'])
		s.隐藏课程=s.l['课程']

	def ks(s):
		if s.l['启用']:
			s.淡化动画=s.p.添加淡化组件(s.p.课程表.上课状态d)
			s.淡化动画.设置脱离主窗口并行(True)
			s.p.kcztbh.connect(s.kcztbh)
	
	def 开始淡化(s,方向):
		if s.淡化动画方向!=方向:
			s.淡化动画方向=方向
			s.淡化动画.设置方向(方向)
			s.淡化动画.start()


	def kcztbh(s,上课状态):
		if 上课状态==2 and (s.所有课程都隐藏 or s.p.课程表.状态['当前课程'] in s.隐藏课程):
			s.开始淡化(False)
		else:
			s.开始淡化(True)

def 配置(p,配置l):
	隐藏下课倒计时=主(p,配置l)
	p.隐藏下课倒计时=隐藏下课倒计时
	p.ks.connect(隐藏下课倒计时.ks)