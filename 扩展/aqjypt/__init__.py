import time
from PyQt6.QtCore import QThread,pyqtSignal
from . import 用户

y=用户.用户()




class 作业获取t(QThread):
    gx=pyqtSignal(list)
    def __init__(s,parent,UserID):
        super().__init__()
        s.parent=parent
        s.UserID=UserID

    def run_(s):
        y.登录(UserID=s.UserID)

        while True:
            未完成作业数=y.查询未完成作业数()
            if 未完成作业数>0:
                print('aqjypt.cxzy')
                作业=y.查询作业()
                #作业={"795127":["2022年中小学生（幼儿）预防溺水专题教育","https://huodong.xueanquan.com/2022yfns/index.html","2022-04-12",0,[-1,0,9,789,1,"https://huodong.xueanquan.com/2022yfns/index.html"]],"791765":["2022年中小学生国家安全教育专题活动","https://huodong.xueanquan.com/2022gjaq/index.html","2022-04-06","2022-04-09 09:42:44.847",[-1,0,9,789,1,"https://huodong.xueanquan.com/2022gjaq/index.html"]],"779578":["2022年中小学生（幼儿）安全教育日专题活动","https://huodong.xueanquan.com/2022safeedu/index.html","2022-03-14","2022-03-17 20:48:03.683",[-1,0,9,789,0,"https://huodong.xueanquan.com/2022safeedu/index.html"]],"768419":["网络是把“双刃剑”",1,"2022-03-07","2022-03-07 14:07:40.12",[796,0,1,789,1,""]],"749087":["公共交通遇险自救",1,"2022-02-28","2022-03-07 14:07:41.727",[797,0,1,789,1,""]],"743008":["野外遇险巧求生",1,"2022-02-24","2022-02-27 13:08:30.463",[808,0,1,789,1,""]],"738458":["救命知识不可少",1,"2022-02-22","2022-02-27 13:08:34.923",[806,0,1,789,1,""]],"738438":["2022年中小学生（幼儿）春季开学安全第一课","https://huodong.xueanquan.com/2022cjkxaq/index.html","2022-02-10","2022-02-17 17:38:59.12",[-1,0,9,789,0,"https://huodong.xueanquan.com/2022cjkxaq/index.html"]],"1":["2022年中小学生（幼儿）平安寒假专项活动","寒假专题","2022-01-05","2022-01-10 15:23:21.607",[0,1,7,0,0,""]],"735459":["2021年中小学生（幼儿）交通安全教育专题","https://huodong.xueanquan.com/2021jtaq/index.html","2021-11-24","2021-12-02 17:53:40.77",[-1,0,9,789,0,"https://huodong.xueanquan.com/2021jtaq/index.html"]],"729902":["2021年中小学生（幼儿）119消防安全专题教育","https://huodong.xueanquan.com/2021firesafety/index.html","2021-10-29","2021-11-03 15:57:54.39",[-1,0,9,789,0,"https://huodong.xueanquan.com/2021firesafety/index.html"]],"705141":["正视自我开心生活",1,"2021-09-24","2021-09-24 08:50:26.477",[1347,0,1,789,1,""]],"701945":["烟酒赌毒，要远离",1,"2021-09-23","2021-09-23 08:50:09.107",[1346,0,1,789,1,""]],"698678":["青春来敲门，一起谈谈“性”",1,"2021-09-22","2021-09-22 10:00:18.537",[1345,0,1,789,1,""]],"697487":["正确运动有利健康",1,"2021-09-20","2021-09-20 15:51:23.95",[1344,0,1,789,1,""]],"677978":["2021年中小学生（幼儿）秋季开学安全第一课","https://huodong.xueanquan.com/2021autumnclass/index.html","2021-08-26","2021-09-19 04:00:49.707",[-1,0,9,789,0,"https://huodong.xueanquan.com/2021autumnclass/index.html"]]}
                未完成=[]
                for  i in 作业:
                    if not i.完成时间:
                        未完成.append((i.标题,i.布置时间[:10]))
                if 未完成:
                    print("aqjypt.有未完成")
                s.gx.emit(未完成)
            else:
                print("aqjypt.无未完成")
                s.gx.emit([])
            s.sleep(60*60)

    def run(s):
        try:
            s.run_()
        except Exception as e:
            print("aqjypt.线程已中止: "+str(e))

class 主():
    def __init__(s,p,UserID):
        s.p=p
        p.aqjypt=s
        s.消息=p.主消息.添加消息(1)
        s.获取t=作业获取t(s,UserID)
        s.获取t.gx.connect(s.gx)
        p.ks.connect(s.ks)
    
    def ks(s):
        s.获取t.start()
        #s.获取t.run()

    
    def gx(s,*a):
        s.更新(*a)
    def 更新(s,未完成):
        s.未完成作业=未完成
        最晚开始时间=0
        if 未完成:
            文本=''
            for i in 未完成:
                文本+=i[0]+' '+i[1]+'\n'
                t0=time.mktime(time.strptime(i[1],"%Y-%m-%d"))
                if 最晚开始时间<t0:
                    最晚开始时间=t0
            s.消息.设置('安全教育平台 有未完成',文本,True,time.time()-1,最晚开始时间+86400*20)
        else:
            s.消息.设置('','',False)

        

def 配置(p,配置l):
    配置l.添加默认值(
        "aqjypt",
        {
		    "UserID":None,
            "启用":False
        }
    )
    if 配置l['aqjypt']['启用']:
        UserID=配置l['aqjypt']['UserID']
        if UserID==None:
            print("未配置aqjypt.UserID")
            return
        a=主(p,UserID)
