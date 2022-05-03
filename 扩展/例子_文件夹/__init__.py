from . import a #要引入同目录下的模块, 请使用 'from . import 模块名'
from .a2 import hw #要引入同目录下模块的方法或属性, 请使用 'from .模块名 import 方法或属性'

hw()

class 主():
    def __init__(s):
        pass

    def ks(s):
        pass

def 配置(p,配置l):
    例子=主()
    p.例子=例子#一定要有这一句, 否则 连接的槽函数 不会被调用, 如 例子.ks 将不会被调用.
    p.ks.connect(例子.ks)