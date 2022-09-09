
from flj import flj
import time

def 获取天(t:int)->int:
    tl=time.localtime(t)
    return tl.tm_year*10000+tl.tm_mon*100+tl.tm_mday


class tl_:
    def __init__(s,f):
        s.f:flj=f
        s.f.添加默认值('tl',{'n':0,'t':0})
        s.n=s.f['tl']['n']

    def 修改(s,n):
        s.n=n
        s.f['tl']['n']=s.n
        s.f['tl']['t']=time.time()
        s.f.写_()
    
    def 加(s):
        s.修改(s.n+1)

    def 是否达到时间(s):
        return 获取天(time.time())>获取天(s.f['tl']['t'])

    def 是否存在(s):
        return 0<s.n<=44

    def 标题(s):
        return "高中英语听力宝典 提升训练下 模拟试题 "+str(s.n)+'\n第'+str(18+2*s.n)+'页'

    def 标题_消息(s):
        return '英语听力 第'+str(18+2*s.n)+'页'

    def 内容_消息(s):
        return "  高中英语听力宝典\n  提升训练下\n  模拟试题 "+str(s.n)

    def 文件名(s):
        return r"D:\Desktop\英语\2022版听力宝典 提升训练下 成盘\2022版听力宝典 提升训练下 mp3 标准\0"+str(s.n+14)+" 2022版高中英语听力宝典 提升训练下  模拟试题 "+str(s.n)+".mp3"
        #return r"D:\Downloads\Paladin.mp3"

