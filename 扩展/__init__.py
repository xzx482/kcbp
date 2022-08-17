import importlib
import sys,os

路径=os.path.dirname(os.path.abspath(__file__))

# 公交和班车 应在 天气 之后; 晨会提示 应在 日期 之后; 倒计时 应在 日期 之后
已启用扩展=['隐藏下课倒计时','wd_','aqjypt','日期','倒计时','天气','公交和班车']

class 加载扩展():
    def __init__(s):
        s.所有扩展={}
        for i in 已启用扩展:
            '''
            路径_=路径+os.sep+i
            目录=False
            if os.path.isdir(路径_):
                目录=True
            if 目录:
                sys.path.append(路径_)
            #'''
            s.所有扩展[i]=importlib.import_module('.'+i,__package__)
            #if 目录:
            #    sys.path.pop()
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

