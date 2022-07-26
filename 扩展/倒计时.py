import time
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget
from kcb_basic import 获取字体,缩放,时间转文字

class 单倒计时组件(QWidget):
    def __init__(s,名称,时间):
        super().__init__()
        s.名称=名称

        s.时间=时间

        s.根横=QHBoxLayout()
        s.setLayout(s.根横)
        s.根横.setContentsMargins(0,0,0,0)
        s.根横.addSpacing(缩放(10))
        s.名称l=QLabel()
        s.名称l.setFont(获取字体(16))
        s.名称l.setText(s.名称)
        s.根横.addWidget(s.名称l)

        s.倒计时l=QLabel()
        s.倒计时l.setFont(获取字体(16))
        s.倒计时l.setText('好多天+∞时+∞分+∞秒')
        s.根横.addWidget(s.倒计时l)
        
        s.根横.addStretch(1)

    def 更新(s,时间:int):
        t=s.时间-时间
        if t<0:
            s.setVisible(False)
        else:
            s.倒计时l.setText(时间转文字(t))


class 倒计时组件(QWidget):
    def __init__(s,配置l):
        super().__init__()
        s.根纵=QVBoxLayout()
        s.setLayout(s.根纵)

        标题l=QLabel('倒计时')
        标题l.setFont(获取字体(12))
        s.根纵.addWidget(标题l)

        倒计时l=配置l['倒计时']['时间']

        s.单倒计时l:单倒计时组件=[]
        for i in 倒计时l:
            单倒=单倒计时组件(i,倒计时l[i])
            s.单倒计时l.append(单倒)
            s.根纵.addWidget(单倒)

    def gx(s,tl):
        t=time.time()
        for i in s.单倒计时l:
            i.更新(t)



def 配置(p,配置l):
    配置l.添加默认值(
        '倒计时',
        {
            '启用':False,
            '时间':{}
        }
    )

    if 配置l['倒计时']['启用']:
        倒计时=倒计时组件(配置l)
        p.根纵_上横_左纵.addWidget(倒计时)
        p.添加淡化组件(倒计时,0.5)
        p.线程.xtsjm.connect(倒计时.gx)



