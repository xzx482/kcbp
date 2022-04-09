
import copy
import json
import os
import random
import time
import _thread
from typing import Tuple

from .访问 import 访问,解码

from urllib import parse,request

#from 全局常量 import 数据文件目录,更新url,完成延迟,配置

专题id={}
专题数据={}
获取文件缓存={}
缓存时间=60*5
超时时间=60*2


def 获取文件(路径:str,类型:str=None):
	'''
从"github"获取指定信息
'''
	if 路径 in 获取文件缓存 and isinstance(获取文件缓存[路径][1],int):
		a=超时时间-(time.time()-获取文件缓存[路径][1])
		while a>0:
			time.sleep(1)
			if isinstance(获取文件缓存[路径][1],str):
				break
			a-=1
	
	
	if 路径 in 获取文件缓存 and time.time()-获取文件缓存[路径][0]<缓存时间:
		数据=获取文件缓存[路径][1]
		if 获取文件缓存[路径][2]in 类型:
			return 获取文件缓存[路径][2][类型]
	else:
		数据=None
		获取文件缓存[路径]=[int(time.time())]*2
		for i in 更新url:
			try:
				r=request.Request(i+路径)
				uo=request.urlopen(r,timeout=10)
				if str(uo.code)[0]=='2':
					数据=解码(uo.read())
					获取文件缓存[路径]=[time.time(),数据,{}]
					break
			except:
				continue
	if 数据:
		try:
			if(类型=="json"):
				数据_=json.loads(数据)
			else:
				数据_=数据
		except:
			return None
		if isinstance(类型,str)and 类型 in['json']:
			获取文件缓存[路径][2][类型]=数据_
		return 数据_
	else:
		return None
		

def 输出(内容):
	print(内容)

def 获取专题id(url:str,作业id:str,输出=输出)->str:
	'''
获取专题活动的id
获取时,会先检查变量,若没有,则从url对应的网页获取,并添加到变量中

参数:
	url:
		该专题页面的url
	
	作业id:
		该专题的作业id

返回值:
	专题id

'''
	作业id=str(作业id)
	#global 专题id
	while 1:
		if 作业id in 专题id:
			if 专题id[作业id]==-1:
				raise 完成_普通专题_错误("多次错误的专题,作业id:"+作业id)
			elif isinstance(专题id[作业id],int)and 专题id[作业id]<-2:
				a=超时时间-(time.time()+专题id[作业id])
				超时=True
				while a>0:
					time.sleep(1)
					if isinstance(专题id[作业id],str)or(isinstance(专题id[作业id],int)and 专题id[作业id]>-2):
						超时=False
						break
					a-=1
				if not 超时:
					continue
				
			else:
				return str(专题id[作业id])
		break
	
	专题id[作业id]=-int(time.time())
	
	输出("未记录的id,通过网络获取")
	专题id_=获取专题id_网页(url)
	if(not 专题id_):
		专题id[str(作业id)]=-1
		raise 完成_普通专题_错误("获取id失败")
	else:
		专题id[str(作业id)]=专题id_
	return 专题id_


def 获取专题id_网页(url:str,id:str="specialId",跳转:int=0,输出=输出)->str:
	'''
"获取专题id"会调用
"获取专题id_网页"会调用.有些网页要跳转,将跳转后的url传给"获取专题id_网页"
从网页获取"三明安全教育平台"的"专题活动"的id

参数:
	url:
		该专题页面的url
	
	id:
		要获取的id,默认是specialId(专题id,普通专题使用),常用的还有schoolYear(学年,寒暑假专题使用)
	
	跳转:
		可选.若该函数是自身调用,则会传入该参数,用于跳转次数过多停止

返回值:
	"专题id"或0,若为0即获取失败

'''
	if(跳转>10):
		return 0
	访问结果=访问(url)
	返回数据=访问结果[6]
	if("window.location.href" in 返回数据 and "<title>跳转中...</title>" in 返回数据):
		#部分专题需跳转
		url2位置=返回数据.index("window.location.href")+21
		#res2 = request.Request("https:"+返回数据[url2位置:url2位置+70].split("'")[1],method="GET")
		#response2 = request.url2open(res2)
		#返回数据 = response2.read().decode("utf-8")
		url2=返回数据[url2位置:url2位置+70].split("'")[1]
		if(url2[0:2]=="//"):
			url2="https:"+url2
		elif(url2[0:4]=="http"):
			''
		else:
			url2="https://"+url2
		if(url2[-11:]=="/index.html"):
			try:
				return 获取专题id_网页(url2[0:-11]+"/video.html",id,跳转+1,输出)
			except:
				return 获取专题id_网页(url2[0:-11]+"/yitu.html",id,跳转+1,输出)
		输出("跳转到"+url2)
		return 获取专题id_网页(url2,id,跳转+1)
	#print(返回数据)
	id="data-"+id
	id位置=返回数据.index(id)+len(id)+1
	return 返回数据[id位置:id位置+10].split('"')[1]

class 会话:
	'''
meiyouruanyong的东西,但是又有些用
'''

	def __init__(s):
		s.cookie={}
		s.重复_={}
		s.默认请求头={}
		s._={}
		s.输出=输出

	def 访问(s,url,请求头={},请求方法=None,数据=None,自动解码=True):
		请求头_=copy.deepcopy(s.默认请求头)
		请求头_.update(请求头)
		结果=访问(url,请求头=请求头_,请求方法=请求方法,数据=数据,cookie=s.cookie,自动解码=自动解码)
		s.cookie.update(结果[5])
		return 结果

	def 重复(s,变量,函数,参数:Tuple,id=None):
		if id:
			if id in s.重复_:
				return False
		else:
			id=time.time()
		s.重复_[id]=True
		try:
			while s.重复_[id]:
				if 变量:
					break
				函数(*参数)
		finally:
			del(s.重复_[id])
	
	def 异步重复(s,变量,函数,参数:Tuple,id=None):
		if id:
			if id in s.重复_:
				return False
		else:
			id=time.time()
		_thread.start_new_thread(s.重复,(变量,函数,参数,id))
		return id
		
	def 结束所有重复(s):
		for i in s.重复_:
			s.重复_[i]=False

	
class 假登录(会话):
	'''
用于防止被风控察觉,模拟正常的登录,可获取到UserID
'''
	def __init__(s):
		会话.__init__(s)
		s.默认请求头={
			'Origin':'https://login.xueanquan.com',
			'Referer':'https://login.xueanquan.com/',
			'sec-ch-ua':'"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile':'?0',
			'sec-ch-ua-platform':'"Windows"',
			'Sec-Fetch-Dest':'empty',
			'Sec-Fetch-Mode':'cors',
			'Sec-Fetch-Site':'same-site',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
		}
		s.延迟=配置['延迟']


	def 获取二维码状态_(s,encodeSceneId):
		id=time.time()
		s.重复_[id]=True
		while s.重复_[id]:
			time.sleep(6)
			srd=json.loads(s.访问('https://appapi.xueanquan.com/usercenter/api/v5/wx/scan-result?encodeSceneId='+encodeSceneId,{},"POST","encodeSceneId="+encodeSceneId)[6])['data']
			if srd['status']!='Wait':
				break
		

	def 假登录_前(s):
		#变量以访问url的最后一个斜杠之后的首字母及取回的内容的首字母确定
		wlqd=json.loads(s.访问('https://appapi.xueanquan.com/usercenter/api/v5/wx/wx-login-qrcode')[6])["data"]
		s._['encodeSceneId']=wlqd['encodeSceneId']
		s.访问(wlqd['relativeUrl'],自动解码=False)
		_thread.start_new_thread(s.获取二维码状态_,(wlqd['encodeSceneId'],))

	def 假登录_登录(s,用户名,密码,次数=0):
		if 次数>1:
			return [False,None]
		s.结束所有重复()
		l=json.loads(s.访问('https://appapi.xueanquan.com/usercenter/api/v3/wx/login?checkShowQrCode=true&tmp=false',{"Content-Type":"application/json;charset=UTF-8"},'POST','{"username":"'+用户名+'","password":"'+密码+'","loginOrigin":1}')[6])
		s.结束所有重复()
		s._['dl_err_code']=l['err_code']
		ld=l['data']
		if l['err_code']==0:
			s._['token']=ld['token']
			if ld['isWeakPwd']:
				s.输出('尝试修改"'+用户名+'"的密码为"'+配置['修改密码']+'"')
				修改结果=s.假登录_修改密码(密码,配置['修改密码'])
				s.输出('修改'+'成功'if 修改结果[0]else ('失败'+('信息: '+修改结果[1])if 修改结果[1]else''))
				time.sleep(完成延迟.假登录_修改密码*s.延迟)
				s.假登录_前()
				time.sleep(完成延迟.假登录*s.延迟)
				return s.假登录_登录(用户名,配置['修改密码'],次数+1)
			return [True,s.cookie['UserID'][0],None if 'isWeakPwd'in ld else ld['isWeakPwd']]
		else:
			return [False,l['err_desc'] if'err_desc'in l else None]

	def 假登录_修改密码(s,旧密码,新密码):
		epbop=json.loads(s.访问('https://appapi.xueanquan.com/usercenter/api/users/edit-pwd-byoldpwd?api-version=2',{'Authorization':s._['token'],"Content-Type":"application/json;charset=UTF-8"},'POST','{"oldPwd":"'+旧密码+'","newPwd":"'+新密码+'"}')[6])
		return [epbop['result'],None if 'message' not in epbop else epbop['message']]


class 错误(Exception):
	def __init__(s,错误信息=None):
		s.名称=s.__class__.__name__
		s.错误信息=错误信息 if 错误信息 else s.__class__.__name__
	def __str__(s):
		return str(s.错误信息)
	def __repr__(s):
		return '<'+str(s.名称)+': '+str(s.错误信息)+'>'

class 用户_错误(错误):
	pass

class 登录_错误(错误):
	pass

class 完成_作业_错误(错误):
	pass

class 完成_安全学习_错误(完成_作业_错误):
	pass

class 完成_普通专题_错误(完成_作业_错误):
	pass

class 完成_假期专题_错误(完成_作业_错误):
	pass

class 用户:
	def __init__(s,用户名:str=None,密码:str=None):
		s.用户名=用户名
		s.密码=密码
		s.cookie=""
		s.用户信息={}
		s.状态=None   #-3:帐号密码错误次数过多;-1:用户名或密码不正确;1:登录成功;
		s.延迟=0 #1为模拟正常人的速度,0为不延迟,2为比正常人慢一倍,以此类推,可为小数
		s._={}  #可随用户附带的标记数据,可自行添加
		s.输出=输出
	

	def 登录(s,用户名:str=None,密码:str=None,UserID:str=None,假登录_=True):
		'''
使用用户名和密码登录 三明安全教育平台

参数:
	用户名:
		要登录的用户名
	
	密码:
		用户名对应的密码

返回值:
	列表:
		cookie:
			登录后网页的"Set-Cookie"的字符串
		
		用户信息
			登录后获得的用户信息

'''
		if s.cookie:
			raise 用户_错误("已登录过")

		请求头={"referer":"https://sanming.xueanquan.com/login.html"}

		if UserID:
			访问结果=访问("https://fujianlogin.xueanquan.com/LoginHandler.ashx",请求头,"POST","r="+str(random.random())+"&loginType=1",'UserID='+UserID)
		else:
			if 用户名:
				s.用户名=用户名
			else:
				if s.用户名:
					用户名=s.用户名
				else:
					raise 用户_错误("用户名为空")
			
			if 密码:
				s.密码=密码
			else:
				if s.密码:
					密码=s.密码
				else:
					raise 用户_错误("密码为空")
			
			url字符='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
			for i in 用户名+密码:
				if(not i in url字符):
					登录_错误("用户名或密码中含有特殊字符:'"+i+"'")
			if 假登录_:
				假登录_=假登录()
				假登录_.输出=s.输出
				假登录_.假登录_前()
				time.sleep(完成延迟.假登录*s.延迟)
				d=假登录_.假登录_登录(用户名,密码)
				if d[0] and d[1]:
					return s.登录(UserID=d[1])
				else:
					错误码_新到旧={8:-1}
					if 'dl_err_code'in 假登录_._ and 假登录_._['dl_err_code']in 错误码_新到旧:
						s.状态=错误码_新到旧[ 假登录_._['dl_err_code'] ]
					else:
						s.状态=假登录_._['dl_err_code']

					raise 登录_错误(d[1])
			else:
				访问结果=访问("https://fujianlogin.xueanquan.com/LoginHandler.ashx?userName="+用户名+"&password="+密码+"&type=login&loginType=1",请求头)
		返回数据=json.loads(访问结果[6])
		
		s.状态=返回数据["Code"]
		if(返回数据["Code"]!=1):
			raise 登录_错误(返回数据["ErrorMsg"] if "ErrorMsg" in 返回数据 else "其他错误")
		s.用户信息=返回数据["UInfo"]
		s.cookie=访问结果[4]
		return [访问结果[4],返回数据["UInfo"]]
	
	def 转列表(s)->list:
		return [s.cookie,s.用户信息]
	
	def 查询已完成作业(s)->dict:
		'''
"查询作业"会调用
查询用户在 三明安全教育平台 中已的完成作业

参数:
	无

返回值:
	字典:
		字符串的作业id:字符串类型的完成时间

'''     
		if not s.cookie:
			raise 用户_错误("cookie为空,尝试 用户.登录(用户名,密码) 以获得cookie")
		访问结果=访问("https://sanming.xueanquan.com/JiaTing/CommonHandler/MyHomeWork.ashx?method=myhomeworkinfo",cookie=s.cookie)
		返回数据=json.loads(访问结果[6])
		已完成作业={}
		if(返回数据["WinterInfo"]["Status"]):
			已完成作业[1]=返回数据["WinterInfo"]["FinishTime"]
		if(返回数据["SummerInfo"]["Status"]):
			已完成作业[2]=返回数据["SummerInfo"]["FinishTime"]
		for index in 返回数据["FinishInfo"]:
			已完成作业[index["WorkId"]]=index["FinishTime"]
		已完成作业2={}
		for index in 已完成作业:
			已完成作业2[str(index)]=已完成作业[index].replace("T"," ")
		return 已完成作业2

	def 查询所有作业(s)->dict:
		'''
	"查询作业"会调用
	查询用户在 三明安全教育平台 中所有的作业

	参数:
		无

	返回值:
		字典:
			字符串的作业id:
				列表:
					作业标题
					作业类型
					布置时间
					完成时间: 暂时为None,在"查询作业"中会与"查询已完成作业"的结果合并为完成时间,若未完成则仍为None
					作业showhdtcbox: 网页中作业的"showhdtcbox"的信息,在"完成安全学习"会用到

	'''
		访问结果=访问("https://file.xueanquan.com/webapi.fujian/jt/MyHomeWork.html?grade="+str(s.用户信息["Grade"])+"&classroom="+str(s.用户信息["ClassRoom"])+"&cityid="+str(s.用户信息["CityCode"]))
		返回数据=访问结果[6].replace("');document.writeln('","").split('tr>')
		作业={}
		aa=0
		for 一项作业_乱 in 返回数据:
			aa+=1
			if(一项作业_乱[-1]=="/"and "title"in 一项作业_乱):
				if("专题活动"in 一项作业_乱):
					类型=一项作业_乱.split("\\")[1][1:]
				elif("安全学习"in 一项作业_乱):
					类型=1
				else:
					类型=2			
				#以双引号拆分字符串
				一项作业_引号分割=一项作业_乱.split('"')
				aaa=0
				标题=""
				for 作业信息_引号分割 in 一项作业_引号分割:
					if(作业信息_引号分割[-6:]=="title="):
						标题 = 一项作业_引号分割[aaa+1]
					elif(作业信息_引号分割[-9:]=="<td name="):
						作业id = 一项作业_引号分割[aaa+1][15:]
					aaa+=1
				布置时间=""
				
				一项作业_表格分割=一项作业_乱.split('td>')
				#以表格标签拆分字符串
				# for 作业信息_表格分割 in 一项作业_表格分割:
				# 	#获取日期
				# 	if(作业信息_表格分割[0:32]=="                                "and 作业信息_表格分割[36:37]=="-"and 作业信息_表格分割[39:40]=="-"):
				# 		布置时间=作业信息_表格分割[32:42]
				布置时间=一项作业_表格分割[7][44:54]
				作业showhdtcbox位置=一项作业_乱.index('onclick=" showhdtcbox(')+22
				作业showhdtcbox=json.loads("["+一项作业_乱[作业showhdtcbox位置:一项作业_乱.index(')',作业showhdtcbox位置)].replace("\\'",'"')+"]")
				try:作业[作业id]=[标题,类型,布置时间,None,作业showhdtcbox]
				except:pass
		
		try:
		#if(1):
			##假期专题链接插入
			#假期专题信息插入
			try:作业["1"][1]="寒假专题"
			except KeyError:''
			#else:
				#寒假专题链接位置=返回数据[0].index('(sporttype == 1) {                    window.open("//huodong." + host.join(\\\'.\\\') + ')+84
				#作业["1"][1]="https://huodong.xueanquan.com"+返回数据[0][寒假专题链接位置:寒假专题链接位置+80].split('"')[1]
			try:作业["2"][1]="暑假专题"
			except KeyError:''
			#else:
				#暑假专题链接位置=返回数据[0].index('(sporttype == 2) {                    window.open("//huodong." + host.join(\\\'.\\\') + ')+84
				#作业["2"][1]="https://huodong.xueanquan.com"+返回数据[0][暑假专题链接位置:暑假专题链接位置+80].split('"')[1]
		except:''#print("警告:假期专题链接获取失败")
		return 作业
	
	def 查询作业(s)->dict:
		'''
	查询用户在 三明安全教育平台 中已完成和所有作业

	参数:
		无

	返回值:
		字典:
			字符串的作业id:
				列表:
					作业标题
					作业类型
					布置时间
					完成时间:若未完成则为None
					作业showhdtcbox: 网页中作业的"showhdtcbox"的信息,在"完成安全学习"会用到

	'''
		所有作业=s.查询所有作业()
		已完成作业=s.查询已完成作业()
		for 作业id in 所有作业:
			if(作业id in 已完成作业):
				所有作业[作业id][3]=已完成作业[作业id]
			else:
				所有作业[作业id][3]=0
		return 所有作业

	def 完成安全学习(s,workid,showhdtcbox):
		'''
	完成用户在 三明安全教育平台 中的一项作业

	参数:
		workid:
			在"查询作业"或"查询所有作业"中得到的"作业id"

		showhdtcbox:
			在"查询作业"或"查询所有作业"中得到的"showhdtcbox"

	返回值:
		无

	'''
		请求头={"cookie":s.cookie}

		作业信息=访问("https://sanming.xueanquan.com/JiaTing/EscapeSkill/SeeVideo.aspx?gid="+str(showhdtcbox[3])+"&li="+str(showhdtcbox[0]),请求头)[6]
		
		作业信息_有用部分_位置=作业信息.index("SeeVideo.TemplateIn2(")+21
		作业信息_有用部分=作业信息[作业信息_有用部分_位置:作业信息.index(")",作业信息_有用部分_位置)].replace('"','').replace("'",'').replace(" ",'').split(",")
		
		作业信息_videoid_位置=作业信息.index("SeeVideo.SkillCheckName(")+24
		作业信息_videoid=作业信息[作业信息_videoid_位置:作业信息_videoid_位置+9].split('"')[1]

		作业信息_testID_位置=作业信息.index("SeeVideo.TestPaperlistGet(")+26
		作业信息_testID=作业信息[作业信息_testID_位置:作业信息_testID_位置+9].split('"')[1]
		
		
		#(workid,	fid,	title,			require,	purpose,	contents,	testwanser,			testinfo,				testMark,		testReulst,	SiteName,		siteAddrees,	watchTime,	CourseID,callback,context)
		#"466032", 	"912", 	"关注饮食安全", ""		,	"",			"",			testanswer="0|0|0",	testinfo="已掌握技能",	testMark=100,	1,			WcContent="",	"",				"",			"1336"
		time.sleep(完成延迟.完成安全学习_视频*s.延迟)
		访问("https://sanming.xueanquan.com/jiating/ajax/FamilyEduCenter.EscapeSkill.SeeVideo,FamilyEduCenter.ashx?_method=CourseAllGet&_session=rw",请求头,"POST","gid="+str(showhdtcbox[3]))
		time.sleep(完成延迟.完成安全学习_视频*s.延迟)
		访问("https://sanming.xueanquan.com/jiating/ajax/FamilyEduCenter.EscapeSkill.SeeVideo,FamilyEduCenter.ashx?_method=I_VideoGet&_session=rw",请求头,"POST","gradeid="+str(showhdtcbox[3]))
		time.sleep(完成延迟.完成安全学习_视频*s.延迟)
		访问("https://sanming.xueanquan.com/jiating/ajax/FamilyEduCenter.EscapeSkill.SeeVideo,FamilyEduCenter.ashx?_method=SkillCheckName&_session=rw",请求头,"POST","videoid="+str(作业信息_videoid)+"\x0d\x0agradeid="+str(showhdtcbox[3])+"\x0d\x0acourseid="+作业信息_有用部分[13])
		time.sleep(完成延迟.完成安全学习_视频*s.延迟)
		访问("https://sanming.xueanquan.com/jiating/ajax/FamilyEduCenter.EscapeSkill.SeeVideo,FamilyEduCenter.ashx?_method=AllSituation&_session=rw",请求头,"POST","gradeid="+str(s.用户信息["Grade"]))
		time.sleep(完成延迟.完成安全学习_视频*s.延迟)
		访问("https://sanming.xueanquan.com/jiating/ajax/FamilyEduCenter.EscapeSkill.SeeVideo,FamilyEduCenter.ashx?_method=VideoDetailInfoGet&_session=rw",请求头,"POST","Vid="+str(作业信息_videoid)+"\x0d\x0acourseid="+作业信息_有用部分[13]+"\x0d\x0acourseid="+作业信息_有用部分[13])
		#'''
		time.sleep(完成延迟.完成安全学习_视频*s.延迟)
		TestPaperlistGet=json.loads(访问("https://sanming.xueanquan.com/jiating/ajax/FamilyEduCenter.EscapeSkill.SeeVideo,FamilyEduCenter.ashx?_method=TestPaperlistGet&_session=rw",请求头,"POST","testID="+str(作业信息_testID))[6].replace("'",'"'))
		
		qID=""
		for i in TestPaperlistGet["Rows"]:
			qID+=str(i["id"])+","
		qID=qID[0:-1]
		#print(qID)
		time.sleep(完成延迟.完成安全学习_视频*s.延迟)
		访问("https://sanming.xueanquan.com/jiating/ajax/FamilyEduCenter.EscapeSkill.SeeVideo,FamilyEduCenter.ashx?_method=TestPaperThreelistGet2&_session=rw",请求头,"POST","qID="+qID)
		#'''
		data = [
		#"workid="+str(workid),
		"workid="+作业信息_有用部分[0],
		"fid="+作业信息_有用部分[1],
		"title="+作业信息_有用部分[2],
		"require="+作业信息_有用部分[3],
		"purpose="+作业信息_有用部分[4],
		"contents="+作业信息_有用部分[5],
		"testwanser=0|0|0",
		"testinfo=已掌握技能",
		"testMark=100",
		"testReulst="+作业信息_有用部分[9],
		"SiteName="+作业信息_有用部分[10],
		"siteAddrees="+作业信息_有用部分[11],
		"watchTime="+作业信息_有用部分[12],
		"CourseID="+作业信息_有用部分[13]
		]
		data2 = ""
		for index in data:
			data2 += "\x0d\x0a"+index
		
		time.sleep(完成延迟.完成安全学习_问题*s.延迟)
		访问结果=访问("https://sanming.xueanquan.com/jiating/ajax/FamilyEduCenter.EscapeSkill.SeeVideo,FamilyEduCenter.ashx?_method=TemplateIn2&_session=rw",请求头,"POST",data2)
		
		返回数据=访问结果[6]
		
		if not(返回数据=="'4'"or 返回数据=="'1'"):
			#提示信息来自"安全教育平台"
			if(返回数据 == "'-4'"):
				raise 完成_安全学习_错误("正在操作中，请勿重复提交")
			elif(返回数据 == "'-2'"):
				raise 完成_安全学习_错误("不能提前参加下半学年的训练")
			elif(返回数据 == "'-5'"):
				raise 完成_安全学习_错误("您不是学生用户，不参与测试记录")
			else:
				raise 完成_安全学习_错误("意外的返回信息:"+str(返回数据))
		

	def 完成专题活动(s,specialId,检查完成=True):
		'''
	完成用户在 三明安全教育平台 中的一项普通专题

	参数:
		专题id:
			"获取专题id"得到的"专题id"
		
		检查完成:
			尝试完成后再查询一次完成信息,若仍未完成则引发错误

	返回值:
		无

	'''
		if(not specialId):

			raise 完成_普通专题_错误("无效的专题id")
		specialId=str(specialId)
		
		if(specialId in 专题数据):
			数据=专题数据[specialId]
		else:
			try:
				with open(数据文件目录+specialId+".json","r",encoding="utf-8")as f:
					数据=json.loads(f.read())
			#try:''
			except FileNotFoundError:
				s.输出('专题未记录,尝试获取')
				数据=获取文件("%E4%B8%93%E9%A2%98%E6%95%B0%E6%8D%AE/"+specialId+".json","json")
				#input(type(数据))
				if(数据 is None):
					raise 完成_普通专题_错误("未记录的专题id")
				try:
					with open(数据文件目录+specialId+".json","w",encoding="utf-8")as f:f.write(json.dumps(数据))
				except:
					s.输出("注意:\""+specialId+"\".json不能写入")
			专题数据[specialId]=数据
		
		请求头={
			"Cookie":s.cookie,
			"Content-Type":"application/json",
		}
		专题点击url="https://huodongapi.xueanquan.com/p/fujian/Topic/topic/platformapi/api/v1/records/sign"
		专题问卷url="https://huodongapi.xueanquan.com/Topic/topic/main/api/v1/records/survey"
		for index in 数据:
			time.sleep(完成延迟.完成专题活动_签到*s.延迟)

			if isinstance(数据[index],list):
				数据_替换=[]			
				for index2 in 数据[index]:
					if("answer" in index2):
						time.sleep(完成延迟.完成专题活动_问卷_单题*s.延迟)
						if isinstance(index2["answer"],list):
							选项_=index2["answer"]
							if 选项_[0]==1:#性别
								选项_=选项_[1][s.用户信息["Sex"]]
							if 选项_[0]==2:#随机
								if isinstance(选项_[1][0],dict):
									l2=[]
									for i3 in 选项_[1][0]:
										for i4 in range(选项_[1][0][i3]):
											l2.append(i3)
									
									if len(选项_[1][0])<选项_[1][1]:
										n=len(选项_[1][0])
									elif len(选项_[1])>2:
										if len(选项_[1][0])<选项_[1][2]:
											选项_[1][2]=len(选项_[1][0])
										n=random.randint(选项_[1][1],选项_[1][2])
									else:
										n=选项_[1][1]
								
								if isinstance(选项_[1][0],list):
									l2=选项_[1][0]
								
								#n=random.randint(选项_[1][1],选项_[1][2])if 选项_[1][2]else 选项_[1][1]

								选项_=[]
								while 1:
									l_=random.choice(l2)
									while 1:
										try:
											l2.remove(l_)
										except ValueError:
											break
									选项_.append(l_)
									if len(选项_)>=n:
										break
							index2["answer"]=','.join(sorted(选项_))
					数据_替换.append(index2)
				time.sleep(完成延迟.完成专题活动_问卷*s.延迟)
				返回数据=访问(专题问卷url,请求头,"POST",json.dumps(
					{"user":
						{"userID":"0",
						"userName":s.用户信息["UserName"],
						"trueName":s.用户信息["TrueName"],
						"regionalAuthority":s.用户信息["regionalAuthority"],
						"userType":"Users",
						"prvCode":s.用户信息["PrvCode"],
						"cityCode":s.用户信息["CityCode"],
						"schoolId":s.用户信息["SchoolID"],
						"schoolName":s.用户信息["SchoolName"],
						"grade":s.用户信息["Grade"],
						"classRoom":s.用户信息["ClassRoom"],
						"comeFrom":s.用户信息["ComeFrom"]},
						"UserAnswers":数据_替换,
						"specialId":specialId,
						"step":index
					}
				,ensure_ascii=False))[6]
				
			返回数据=访问(专题点击url,请求头,"POST","{specialId:"+specialId+", step:"+index+"}")[6]
		if 检查完成:
			time.sleep(完成延迟.完成专题活动_检查*s.延迟)
			完成状态=json.loads(访问("https://huodongapi.xueanquan.com/p/fujian/Topic/topic/platformapi/api/v1/records/finish-status?specialId="+specialId,请求头)[6])
			if not 完成状态["finishStatus"]:
				raise 完成_普通专题_错误("尝试所有步骤后仍无法完成")

	def 完成假期专题活动(s,专题布置时间:str):
		'''
	完成用户在 三明安全教育平台 中的一项假期专题

	参数:
		假期专题:
			与"作业id"相同
			若是寒假专题,则为1
			若是暑假专题,则为2

		专题布置时间:
			"查询作业"得到的"布置时间"

		检查完成:
			尝试完成后再查询一次完成信息,若仍未完成则引发错误

	返回值:
		无

	'''
		if 专题布置时间 in 专题数据:
			数据=专题数据[专题布置时间]
		else:
			try:
				with open(数据文件目录+专题布置时间+".json","r",encoding="utf-8")as f:数据=json.loads(f.read())
			#try:''
			except:
				s.输出('专题未记录,尝试获取')
				数据=获取文件("%E4%B8%93%E9%A2%98%E6%95%B0%E6%8D%AE/"+专题布置时间+".json","json")
				if(数据 is None):
					s.输出('获取失败')
				try:
					with open(数据文件目录+专题布置时间+".json","w",encoding="utf-8")as f:f.write(json.dumps(数据))
				except:
					s.输出("注意:\""+专题布置时间+".json\"不能写入")
			专题数据[专题布置时间]=数据
		
		#完成状态=1
		请求头={
			"Cookie":s.cookie,
			"Content-Type":"application/json",
		}
			
		专题点击url="https://huodongapi.xueanquan.com/p/fujian/Topic/topic/platformapi/api/v1/holiday/sign"#此处的url与"完成专题活动"的url不同
		专题问卷url="https://huodong.xueanquan.com/HolidayService/SubmitTest"
		for index in 数据["步骤"]:
			time.sleep(完成延迟.完成专题活动_签到*s.延迟)
			返回数据=访问(专题点击url,请求头,"POST",'{"schoolYear":'+数据["schoolYear"]+',"semester":'+数据["semester"]+',"step":'+index+',"prvName":"'+s.用户信息["PrvName"]+'","cityName":"'+s.用户信息["CityName"]+'"}')[6]
			if(str(type(数据["步骤"][index]))=="<class 'list'>"):
				'''
				数据_替换=[]
				for index2 in 数据[index]:
					if("answer" in index2 and index2["answer"][0:5]=="用户_性别"):
						选项=json.loads(index2["answer"][5:].replace("'",'"'))
						if(s.用户信息["Sex"]=="1"):#男
							index2["answer"]=选项["男"]
						elif(s.用户信息["Sex"]=="2"):#女
							index2["answer"]=选项["女"]
						else:
							index2["answer"]=""
					数据_替换.append(index2)
				'''
				time.sleep(完成延迟.完成专题活动_问卷*s.延迟)
				返回数据=访问(专题问卷url,{**请求头,**{"Content-Type":"application/x-www-form-urlencoded"}},"POST",
					parse.urlencode({
						'r':random.random(),
						'schoolYear':数据["schoolYear"],
						'semester':数据["semester"],
						'userType':s.用户信息["UserType"],
						'answerJson':json.dumps(数据["步骤"][index],ensure_ascii=False),
						'prv':s.用户信息["PrvCode"],
						'city':s.用户信息["CityCode"],
						'county':s.用户信息["CountryId"],
						'school':s.用户信息["SchoolID"],
						'grade':s.用户信息["Grade"],
						'Class':s.用户信息["ClassRoom"],
						'comefrom':s.用户信息["ComeFrom"],
						'version':数据["version"],
						'TrueName':s.用户信息["TrueName"],
						'prvName2':s.用户信息["PrvName"],
						'cityName2':s.用户信息["CityName"],
					})
				)[6]
		time.sleep(完成延迟.完成专题活动_检查*s.延迟)
		完成状态=json.loads(访问("https://huodongapi.xueanquan.com/p/fujian/Topic/topic/platformapi/api/v1/holiday/finish-status?schoolYear="+数据["schoolYear"]+"&semester="+数据["semester"],请求头)[6])
		if not 完成状态["finishStatus"]:
			raise 完成_普通专题_错误("尝试所有步骤后仍无法完成")

	def 完成作业(s,作业id,作业):
		if(s.用户信息["UserType"]!=0):
			raise 完成_作业_错误("非学生账号不能完成作业")
		if(作业[1]==1):#安全学习
			s.输出('尝试完成安全学习"'+作业[0]+'"')
			s.完成安全学习(作业id,作业[4])

		elif(作业[1]=="寒假专题" or 作业[1]=="暑假专题"):#假期专题
			s.输出('尝试完成假期专题活动"'+作业[0]+'"')
			s.完成假期专题活动(作业[2])
			
		elif(作业[1]!=3):#普通专题
			s.输出('尝试完成普通专题活动"'+作业[0]+'"')
			s.完成专题活动(获取专题id(作业[1],作业id,s.输出))

		s.输出('已完成"'+作业[0]+'"')

