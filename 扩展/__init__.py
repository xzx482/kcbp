import importlib

已启用扩展=['aqjypt','日期','天气']

class 加载扩展():
    def __init__(s):
        s.所有扩展={}
        for i in 已启用扩展:
            s.所有扩展[i]=importlib.import_module('.'+i,__package__)
        '''
        for filefiner, name, ispkg in pkgutil.iter_modules(扩展.__path__, 扩展.__name__ + "."):
            print("{0} name: {1:12}, is_sub_package: {2}".format(filefiner, name, ispkg))
            if name[0:3]=='扩展.':
                s.所有扩展[ name[3:] ]=importlib.import_module(name)
        '''
    
    def 配置(s,parent,配置l):
        for i in s.所有扩展:#按顺序加载和配置
            s.所有扩展[i].配置(parent,配置l)

    def __getattr__(s, __name:str):
        try:
            return s.所有扩展[__name]
        except KeyError:
            raise AttributeError(__name)

