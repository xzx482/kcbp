import os
import time
from PyQt6.QtCore import QThread,pyqtSignal

def 解析lrc(lrcdata):
        lrc = []
        for line in lrcdata.split('\n'):
            #try:
            t0, lyric = line.split(']')
            t0 = t0[1:].split(':')
            if t0[0][0] in '0123456789':
                t0 = int(t0[0]) * 60 + float(t0[1])
                lrc.append((t0, lyric))
                        
        return lrc


class 更新歌词t(QThread):
    gxgc=pyqtSignal()
    def __init__(s,parent=None):
        super().__init__(parent)
        s.显示=False
    def run(s):
        while True:
            if not s.显示:
                s.sleep(2)
                continue
            time.sleep(0.2)
            s.gxgc.emit()

class 主():
    def __init__(s,p):
        s.p=p
        s.消息=p.主消息.添加消息(1)
        s.歌词=[]
        s.当前歌词=0
        s.当前歌词_索引=0
        s.t=0
        
        s.线程=更新歌词t()
        s.线程.gxgc.connect(s.gx)

    def 读取歌词(s):
        #歌词位于歌词文件夹下
        #歌词文件名为歌曲名
        #歌词文件名后缀为.lrc

        for i in os.listdir(os.path.join(os.path.dirname(__file__),'歌词')):
            if i[-4:]=='.lrc':
                with open(os.path.join(os.path.dirname(__file__),'歌词',i))as f:
                    s.歌词.append( ( i[:-4], 解析lrc( f.read() ) ) )

    def 获取当前歌词(s):
        歌词=s.歌词[s.当前歌词][1]
        t0=time.time()
        while 1:
            if s.当前歌词_索引+1>=len(歌词):
                引加=s.当前歌词_索引
            else:
                引加=s.当前歌词_索引+1
            if t0-s.t>=歌词[引加][0]:
                s.当前歌词_索引+=1
                if s.当前歌词_索引>=len(歌词):
                    s.当前歌词_索引=0
                    s.t=t0
                    s.当前歌词+=1
                    if s.当前歌词>=len(s.歌词):
                        s.当前歌词=0
                    歌词=s.歌词[s.当前歌词][1]
            else:
                break
        
        return 歌词[s.当前歌词_索引][1]

    def gx(s):
        tm=time.time()
        歌词=s.获取当前歌词()
        s.消息.设置('𝅘𝅥𝅮'+s.歌词[s.当前歌词][0],歌词,True,tm-1,tm+10)

    def zjxsztbh(s,显示):
        s.线程.显示=显示

    def ks(s):
        s.t=time.time()
        s.读取歌词()
        if s.歌词:
            s.线程.start()
        else:
            print('歌词显示: 没有歌词')


def 配置(p,配置l):
    歌词显示=主(p)
    p.歌词显示=歌词显示
    p.ks.connect(歌词显示.ks)
    p.zjxsztbh.connect(歌词显示.zjxsztbh)
    #p.线程.xtsjm.connect(歌词显示.gx)
