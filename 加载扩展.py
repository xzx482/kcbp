import importlib
from modulefinder import Module
import pkgutil, 扩展

class 加载扩展():
    def __init__(s):
        s.所有扩展={}
        for filefiner, name, ispkg in pkgutil.iter_modules(扩展.__path__, 扩展.__name__ + "."):
            print("{0} name: {1:12}, is_sub_package: {2}".format(filefiner, name, ispkg))
            if name[0:3]=='扩展.':
                s.所有扩展[ name[3:] ]=importlib.import_module(name)
    
    def 配置(s,parent,配置l):
        for i in s.所有扩展:
            s.所有扩展[i].配置(parent,配置l)

    def __getattribute__(s, __name:str)->Module:
        try:
            return s.所有扩展[__name]
        except KeyError:
            raise AttributeError(__name)

