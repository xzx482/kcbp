from html.parser import HTMLParser
from html import unescape
#import sys
#sys.setrecursionlimit(3000)  # 将默认的递归深度修改为3000

class Dom():
    def __init__(s,标签=None,属性=None,内容=None)->None:
        s.标签=标签 if 标签 else ''
        s.属性=属性 if 属性 else {}
        s.内容=内容 if 内容 else []
    
    def __iter__(s):
        s.iter=iter(s.内容)
        return s
    
    def __next__(s):
        return next(s.iter)
    
    def __getitem__(s,n):
        return s.内容[n]
    
    def __len__(s):
        return len(s.内容)

    def __str__(s):
        return str(s.标签)+str(s.属性)+':'+str(s.内容)
    
    __repr__ = __str__

    def 添加(s,内容):
        s.内容.append(内容)

    def _查找(dom_,标签=None,属性=None,文本=None,父级=0,所有=False):
        找到=False
        d=[[],[]]
        if 标签 and dom_.标签==标签:
            找到=True
        if 属性 and dom_.属性:
            for i in 属性:
                if i in dom_.属性 and((not 属性[i])or dom_.属性[i]==属性[i]):
                    找到=True
                    break
            
        if 找到:
            d[0].append(0)
            if not 所有:
                return d
        
        if not 找到 or 所有:
            for i in dom_:
                if isinstance(i,Dom):
                    if i.内容:
                        a=__class__._查找(i,标签,属性,文本,父级,所有)
                        d[1]+=a[1]
                        for i2 in a[0]:
                            if 父级>i2:
                                d[0].append(i2+1)
                            else:
                                d[1].append(i)
                                if not 所有:
                                    return d
                        if not 所有 and(d[0]or d[1]):
                            return d
                        
                else:
                    if 文本 and 文本 in i:
                        d[0].append(0)
                        if not 所有:
                            return d
        
        return d

    def 查找(dom_,标签=None,属性=None,文本=None,父级=0,所有=False):
        return dom_._查找(标签,属性,文本,父级,所有)[1]

    def 查找_多条件(d,s):
        '''
        s=[{'标签':'h2','属性':{'id':'ab'},'父级':2}]
        '''
        for i in s:
            b=None
            b=__class__.查找(d,**i)
            if b:
                d=__class__(内容=b)
        return b


class MyHTMLParser(HTMLParser):

    def __init__(self, *, convert_charrefs=True):
        """Initialize and reset this instance.

        If convert_charrefs is True (the default), all character references
        are automatically converted to the corresponding Unicode characters.
        """
        self.convert_charrefs = convert_charrefs
        self.reset()

        self.dom_=Dom('根')
        self.栈=[self.dom_]

    def handle_starttag(s,标签,属性):#<tag>
        y=Dom(标签,dict(属性))
        s.栈[-1].添加(y)
        #self.list_.append(y)
        s.栈.append(y)

    def handle_endtag(s,标签):#</tag>
        a=False
        for i in s.栈:
            if i.标签==标签:
                a=True
        if not a:
            return
        while 1:
            if s.栈.pop().标签==标签:
                break

    def handle_data(s,数据):#<tag>data</tag>
        s.栈[-1].添加(数据)

    def handle_startendtag(s,标签,属性):#<tag/>
        y=Dom(标签,dict(属性))
        s.栈[-1].添加(y)

    def handle_comment(self,data):#<!--data-->
        pass


def 解析(文本:str)->Dom:
    parser=MyHTMLParser()
    parser.feed(文本)
    return parser.dom_





#s=[('tag','body',0),('attr',{'id':'abc'},0),('text','12345',0)]


def 解实体(s):
    return unescape(s)

def 解析表格(表格):
    t=[]
    tbody=Dom.查找(表格,标签='tbody')[0]
    for tr in tbody:
        if isinstance(tr,Dom)and tr.标签=='tr':
            t2=[]
            for td in tr:
                if isinstance(td,Dom)and td.标签=='td':
                    t2.append(td.内容)
            t.append(t2)
    return t
