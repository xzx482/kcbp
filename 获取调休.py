from urllib import request
import 解析html
import time



调休信息={}
def 更新调休_单天(lti,n):
    if lti.tm_year not in 调休信息:
        调休年=调休信息[lti.tm_year]={}
    else:
        调休年=调休信息[lti.tm_year]

    if lti.tm_mon not in 调休年:
        调休月=调休年[lti.tm_mon]={}
    else:
        调休月=调休年[lti.tm_mon]

    调休月[lti.tm_mday]=n


def 获取调休信息(tl=None):
    #tl=time.localtime(int(time.mktime((2015,1,1,0,0,0,0,0,0))))
    if not tl:
        tl=time.localtime()
    年=tl.tm_year
    默认日期=[tl.tm_year,tl.tm_mon,tl.tm_mday]

    html_t=request.urlopen('http://sousuo.gov.cn/s.htm?q='#不用https是很危险的
        #国务院办公厅关于xxxx年部分节假日安排的通知
        '%E5%9B%BD%E5%8A%A1%E9%99%A2%E5%8A%9E%E5%85%AC%E5%8E%85%E5%85%B3%E4%BA%8E'
        +str(年)+
        '%E5%B9%B4%E9%83%A8%E5%88%86%E8%8A%82%E5%81%87%E6%97%A5%E5%AE%89%E6%8E%92%E7%9A%84%E9%80%9A%E7%9F%A5&t=paper'#t=paper 为国务院文件
    ).read().decode('utf-8')
    h=解析html.解析(html_t)
    result=h.查找(属性={'class':'result'})
    搜索结果=result[0][1]
    找到=False
    for i in range(len(搜索结果)):
        if isinstance(搜索结果[i],解析html.Dom):
            超链接=搜索结果[i][1][0]
            超链接_文本=超链接[0]
            if isinstance(超链接_文本,解析html.Dom)and 超链接_文本.内容[0]=='国务院办公厅关于'+str(年)+'年部分节假日安排的通知':
                找到=True
                break

    if not 找到:
        raise
    html_t2=request.urlopen(超链接.属性['href']).read().decode('utf-8')
    h2=解析html.解析(html_t2)
    ucap=h2.查找(属性={'id':'UCAP-CONTENT'})[0].转文本().replace('\u3000','').split('\n')
    
    
    开始=False
    for i in ucap:
        i:str
        if i:
            if 开始:
                if '：' in i:
                    #i.内容 [span{'style': 'font-weight: bold;'}:['二、春节：'], '1月31日至2月6日放假调休，共7天。1月29日（星期六）、1月30日（星期日）上班。']
                    节日名,调休情况_文本=i.split('、',1)[1].split('：')
                    #调休情况_文本=i.内容[1]
                    #用最简单的方法解析


                    放假文本,上班文本=调休情况_文本.split('。')[0:2]#放假文本,上班文本
                    if '放假调休'in 放假文本:
                        调休=True
                    elif '放假'in 放假文本:
                        调休=False
                    else:
                        raise
                    放假文本_=放假文本.split('，')
                    放假范围文本=放假文本_[0]
                    if len(放假文本_)>1:
                        放假补充文本=放假文本_[1]
                    else:
                        放假补充文本=''
                    放假范围_=[[i]for i in 放假范围文本.split('放假')[0].split('至')]
                    #放假范围=放假范围_.copy()
                    日期_范围前=默认日期.copy()
                    日期_范围后=None
                    日期_范围=[日期_范围前]
                    if '清明节'in i:
                        pass#下断点,清明节有问题
                    for i in range(2):
                        放假范围_i=放假范围_[i]
                        for i2 in range(3):
                            放假范围_i=放假范围_i[-1].split('年月日'[i2])
                            if len(放假范围_i)>1:
                                日期_范围[i][i2]=int(放假范围_i[0])
                        if i==0:
                            if len(放假范围_)>1:#有范围 xx月xx日至(xx月)xx日放假(调休)
                                日期_范围后=日期_范围前.copy()
                                日期_范围.append(日期_范围后)
                            else:#没有范围 xx月xx日放假
                                break
                        

                    日期_范围#提取的放假日期范围
                    日期_范围_=[]
                    for i in 日期_范围:
                        日期_范围_.append(int(time.mktime((*i,0,0,0,0,0,0))))

                    if len(日期_范围_)>1:
                        for i in range(日期_范围_[0],日期_范围_[1]+1,86400):#日期_范围_[1]+1是为了把最后一天也加进去
                            更新调休_单天(time.localtime(i),1)
                    else:
                        更新调休_单天(time.localtime(日期_范围_[0]),1)

                    if '补休'in 放假补充文本:
                        补休文本=放假补充文本.replace('补休','').split('、')
                        for i in range(len(补休文本)):
                            日期_=日期_范围[0].copy()
                            上i=[补休文本[i]]
                            for i2 in range(3):
                                上i=上i[-1].split('年月日'[i2])
                                if len(上i)>1:
                                    日期_[i2]=int(上i[0])
                            更新调休_单天(time.localtime(int(time.mktime((*日期_,0,0,0,0,0,0)))),1)


                    上班日期=[]
                    if 调休:
                        上班文本=上班文本.split('上班')[0].split('、')
                        for i in range(len(上班文本)):
                            if 上班文本[i]:
                                日期_=日期_范围[0].copy()
                                上i=[上班文本[i]]
                                for i2 in range(3):
                                    上i=上i[-1].split('年月日'[i2])
                                    if len(上i)>1:
                                        日期_[i2]=int(上i[0])
                                更新调休_单天(time.localtime(int(time.mktime((*日期_,0,0,0,0,0,0)))),2)


                    #print(节日名,调休情况_文本)
                #print(i.内容)
            else:
                if '具体安排通知如下'in i:
                    开始=True

if __name__ == '__main__':
    for i in range(2021,2022+1):
        获取调休信息(time.localtime(int(time.mktime((i,1,1,0,0,0,0,0,0)))))
    print(调休信息)
#input(result)
