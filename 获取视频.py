import json
from urllib import request


清晰度_={'1080':(1920,1080),'1440':(2560,1440),'2160':(3840,2160)}

def 获取屏幕宽高():

    return (宽,高)

class 背景():
    def __init__(s):
        s.d=None

    def 获取(s):
        s.d=json.load(request.urlopen('https://ntp.msn.cn/resolver/api/resolve/v3/config/?expType=AppConfig&expInstance=default&apptype=edgeChromium&v=20220201.140&targetScope={%22locale%22:{%22content%22:{%22language%22:%22zh%22,%22market%22:%22cn%22},%22display%22:{%22language%22:%22zh%22,%22market%22:%22cn%22}}}'))
        return s.d

    def 整理(s,清晰度=None,宽高=None):
        if not s.d:
            s.获取()
        if not 清晰度:
            if not 宽高:
                raise
                宽高=获取屏幕宽高()
            宽=宽高[0]
            高=宽高[1]
            for i in 清晰度_:
                i_=清晰度_[i]
                if i_[0]>=宽 and i_[1]>=高:
                    break
            清晰度=i
        else:
            清晰度=str(清晰度)
        properties=s.d["configs"]["BackgroundImageWC/default"]["properties"]
        video_titles=properties["localizedStrings"]["video_titles"]
        pvd=properties["video"]["data"]

        vl=[]
        for i in range(len(pvd)):
            pvdi=pvd[i]
            vl.append((video_titles['video'+str(i)],pvdi['attribution'],pvdi['firstFrame']['i'+清晰度],pvdi['video']['v'+清晰度]))
        s.vl=vl
        return vl

if __name__=='__main__':
    vl=背景().整理(宽高=(1920,1080))
    print(vl)