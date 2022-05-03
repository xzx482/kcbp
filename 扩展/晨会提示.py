import time


class 主():
    def __init__(s,p,配置l):
        s.p=p
        s.配置l=配置l
        s.消息=p.主消息.添加消息(1)

    def tqgx(s,天气j):
        今天=s.p.日历.日期j['今天']
        if 今天.星期()>=2:
            周=今天.sx.getWeekIndex()#一个月的第几周
            晨会提示l=s.配置l['晨会提示']

            当前时间=天气j['current']['dt']
            当前时间tm=time.localtime(当前时间)
            if 周!=晨会提示l['周']:
                #晨会提示l['周']
                #判断时间是否大于18时
                if 当前时间tm.tm_hour>=18:
                    print('第'+str(周)+'周, 晨会提示')

                    #分析天气是否适宜明天早上六点半的晨会
                    每小时天气l=天气j['hourly']
                    几小时天气=[]
                    ts=0
                    for i in 每小时天气l:
                        if time.localtime(i['dt']).tm_hour in [2,3,4,5,6,7,8,9,10]:
                            几小时天气.append(i)
                    
                    一半样本数=len(几小时天气)//2
                    样本数=len(几小时天气)
                    for i in range(len(几小时天气)):
                        if str(几小时天气[i]['weather'][0]['id'])[0] in "78":#7或8开头的编号没有下雨, 更有可能晨会
                            #中间的样本权重更大
                            ts+=1*(1.5-((i-一半样本数)/一半样本数)**2)
                    
                    晨会概率=ts/样本数
                    晨会概率2=((晨会概率-0.5)*0.7)+0.5#将概率靠近0.5
                    print(晨会概率2)
                    信息='明天'
                    可能性=abs(晨会概率2-0.5)
                    if 可能性>0.3:
                        信息+='大概率'
                    else:
                        信息+='可能'
                    
                    if 晨会概率2>0.5:
                        信息+='有'
                    else:
                        信息+='没有'
                    信息+='晨会'

                    t2=time.localtime()
                    今天最后一秒=time.mktime((t2.tm_year,t2.tm_mon,t2.tm_mday,23,59,59,t2.tm_wday,t2.tm_yday,t2.tm_isdst))
                    s.消息.设置('晨会率'+str(round(晨会概率2*100))+'%',信息,True,time.time()-1,今天最后一秒)




                    

            pass


def 配置(p,配置l):
    配置l.添加默认值('晨会提示',{'周':0})
    晨会提示=主(p,配置l)
    p.晨会提示=晨会提示
    p.天气.gxtq_signal.connect(晨会提示.tqgx)