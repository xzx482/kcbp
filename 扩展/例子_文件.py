

class 主():
    def __init__(s,p):
        s.p=p
        s.消息=p.主消息.添加消息(1)

    def ks(s):
        pass

def 配置(p,配置l):
    例子=主(p)
    p.例子=例子#一定要有这一句, 否则 连接的槽函数 不会被调用, 如 例子.ks 将不会被调用.
    p.ks.connect(例子.ks)