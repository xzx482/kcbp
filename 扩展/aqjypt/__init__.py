import time
from PyQt6.QtCore import QThread,pyqtSignal
from . import 用户

y=用户.用户()




class 作业获取t(QThread):
    gx=pyqtSignal(list)
    def __init__(s,parent):
        super().__init__()
        s.parent=parent

    def run(s):
        y.登录(UserID='B8BBC460CC8B3D49CFF03A5871AE99DD')

        while True:
            作业=y.查询作业()
            未完成=[]
            for  i in 作业:
                作业i=作业[i]
                if not 作业i[3]:
                    未完成.append((作业i[0],作业i[2]))

            s.gx.emit(未完成)
            time.sleep(60*20)

class 主():
    def __init__(s,p):
        s.p=p
        s.消息=p.主消息.添加消息(1)
        s.获取t=作业获取t(s)
        s.获取t.gx.connect(s.gx)
        s.获取t.start()

    
    def gx(s,*a):
        s.更新(*a)
    def 更新(s,未完成):
        s.未完成作业=未完成
        文本=''
        for i in 未完成:
            文本+=i

        

def 配置(p,配置l):
    a=主(p)
