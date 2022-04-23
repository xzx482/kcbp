from . import a #要引入同目录下的模块, 请使用 'from . import 模块名'
from .a2 import hw #要引入同目录下模块的方法或属性, 请使用 'from .模块名 import 方法或属性'

hw()

def 配置(p,配置l):
    p.ks.connect()