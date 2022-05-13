from ctypes import Union
from io import BytesIO
from urllib import request,parse
import gzip
import time
import json
#from 终端控制 import 按任意键继续
出错暂停时间=10
出错停止次数=-1

#使urllib 4xx-5xx状态码不引发异常
class HTTPErrorProcessor(request.BaseHandler):
	handler_order = 1000  # after all other processing
	def http_response(self, request, response):
		return response
	https_response = http_response
request.HTTPErrorProcessor=HTTPErrorProcessor

出错=0

def 访问(url,请求头={},请求方法=None,数据=None,cookie=None,转换='str'):
	'''
访问 http url.调用了urllib,简化了参数及流程

参数:
	url:
		访问的url,具体查看urllib.request.Request函数中参数url
	
	请求头:
		可选.默认请求头在"请求头_"中
		可传入  字典 列表 字符串  类型,但在本函数中最终都会转为字典:
			字典 类型:
				{"键1":"值1","键2":"值2","键3":"值3"}
			
			列表 类型:(": "可换为":")
				["键1: 值1","键2: 值2","键3: 值3"]

			字符串 类型:(": "可换为":","\n\r"可换为"\n")
				"""键1: 值1\n\r键2: 值2\n\r键3: 值3"""
	
	请求方法:
		可选.请求方法=method,具体查看urllib.request.Request函数中参数method
	
	数据:
		可选.上传的数据,本函数内已使用bytes函数将其utf-8编码
	
	cookie:
		可选.要发送的cookie,将会包括在请求头中.若请求头中已有cookie,将会追加在后面,若有重复,则会重复发送
		可传入  字典 列表 字符串  类型,但在本函数中最终都会转为字符串到请求头中:
			字典 类型:
				{"键1":["值1","域1","路径1","过期时间1"],"键2":["值2","域2","路径2","过期时间2"],"键3":["值3","域3","路径3","过期时间3"]}, 即与 "字典的响应cookie" 相同
				或
				{"键1":"值1","键2":"值2","键3":"值3"}
	
	转换:
		可选.将返回的数据转换为指定的类型,默认为str, 可选值为:
			"str": 纯文本
			"json": json格式
			"bytes": 二进制数据, 若有压缩(如gzip), 将解压缩
			"raw": 原始数据, 若有压缩(如gzip), 将不解压缩

返回值:
	列表:
		0:字符串的url:
			若进行了重定向,该值可能与参数的url不同

		1:数字的状态码:
			即"HTTP状态码"

		2:字符串的响应头:
			原始的响应头,包括"Set-Cookie"

		3:字典的响应头:
			整理后的便于程序使用的响应头,不包括"Set-Cookie"

		4:字符串的响应cookie:
			从响应头"Set-Cookie"中提出的不包括"domain" "path" "expires"的cookie,仅有"键1=值1; 键2=值2; 键3=值3"

		5:字典的响应cookie:
			从响应头"Set-Cookie"中提出的包括"domain" "path" "expires"的cookie,有 {"键1":["值1","域1","路径1","过期时间1"],"键2":["值2","域2","路径2","过期时间2"],"键3":["值3","域3","路径3","过期时间3"]}

		6:字符串的响应数据:
			正文内容

'''
	global 出错
	请求头_={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
	'Accept-Encoding':'gzip',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
	if(数据):
		data=bytes(数据,encoding="utf8")
	else:
		data=None
	if(isinstance(请求头,dict)):
		请求头_.update(请求头)
	elif(isinstance(请求头,list)or isinstance(请求头,str)):
		if(isinstance(请求头,str)):
			请求头.split("\n")
			for i in range(len(请求头)):
				if(请求头[i][-1]=="\r"):
					请求头[i]=请求头[i][0:-1]
		for i in 请求头:
			请求头_分割位置=请求头.index(":")
			if(请求头[请求头_分割位置+1]==""):
				请求头_[请求头[0:请求头_分割位置]]=请求头[请求头_分割位置+1:]
			elif(请求头[请求头_分割位置+1]==" "):
				请求头_[请求头[0:请求头_分割位置]]=请求头[请求头_分割位置+2:]

	else:
		raise TypeError("\"请求头\"的类型应为 dict list str 中的其中一种")
	
	url拆分=parse.urlparse(url)
	if(cookie):
		if(not "cookie" in 请求头_):
			请求头_["cookie"]=""
		else:
			请求头_["cookie"]+="; "
		if(isinstance(cookie,dict)):
			for i in cookie:
				if(isinstance(cookie[i],list)):
					if(not cookie[i][3] or time.mktime(time.strptime(cookie[i][3][5:-4],"%d-%b-%Y %H:%M:%S"))>time.time()):
						路径正确=False
						域名正确=False
						路径=url拆分.path
						cookie路径=cookie[i][2]
						if(cookie路径[-1]=="/"):
							if(len(路径)>len(cookie路径[0:-1])and 路径[0:len(cookie路径)]==cookie路径):
								路径正确=True
						else:
							if(cookie路径==路径):
								路径正确=True
						

						域名=url拆分.hostname
						cookie域名=cookie[i][1]
						if(cookie域名[0]=="."):
							if(len(cookie域名[1:].split("."))>1 and len(域名)>len(cookie域名[1:])and 域名[-len(cookie域名[1:]):]==cookie域名[1:]and 域名[0:-len(cookie域名[1:])].split(".")[-1]==""):
								域名正确=True
						else:
							if(cookie域名==域名):
								域名正确=True
						
						if(路径正确 and 域名正确):
							请求头_["cookie"]+=i+"="+cookie[i][0]+"; "

				elif(isinstance(cookie[i],str)):
					请求头_["cookie"]+=i+"="+cookie[i]+"; "
				
		elif(isinstance(cookie,list)):
			请求头_["cookie"]+="; ".join(cookie)+"; "
		
		elif(isinstance(cookie,str)):
			请求头_["cookie"]+=cookie+"; "
		else:
			raise TypeError("\"cookie\"的类型应为 dict list str 中的其中一种")


		请求头_["cookie"]=请求头_["cookie"][0:-2]

	#url字符="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~!*'();:@&=+$,/?#[]%"
	#for i in url:
	#	if(not i in url字符):
	#		raise UnicodeEncodeError("url中包含特殊字符")
	请求=request.Request(url,data=data,headers=请求头_,method=请求方法)
	#"""
	while 1:
		try:
			响应=request.urlopen(请求)
			出错=0
			break
			'''
		except request.URLError as 错误:
			print(repr(错误))
			print(repr(错误).split("(")[0])
			raise
		#'''
		except KeyboardInterrupt:
			raise
		except BaseException as 错误:
			出错+=1
			if 出错停止次数==-1 or 出错<出错停止次数:
				print("网络错误:"+str(错误)+", 连续第 "+str(出错)+" 次出错, 暂停 "+str(出错暂停时间)+" 秒")
				time.sleep(出错暂停时间)
			else:
				print("网络错误:"+str(错误)+", 连续第 "+str(出错)+" 次出错, 暂停 "+str(出错暂停时间*4)+" 秒")
				time.sleep(出错暂停时间*4)
	#"""
	#响应=request.urlopen(请求)

	响应头_原始=str(响应.info())
	响应头_=响应头_原始.split("\n")[0:-2]
	响应头_整理={}
	响应头_cookie_未整理=[]
	响应头_cookie_字符串=""
	响应头_cookie_整理={}
	for i in 响应头_:
		i_=i.split(": ",1)
		if(i_[0]=="Set-Cookie"):
			响应头_cookie_未整理.append(i_[1])
		else:
			响应头_整理[i_[0]]=i_[1]
	
	for i in 响应头_cookie_未整理:
		i_=i.split("; ")
		响应头_cookie_字符串=响应头_cookie_字符串+i_[0]+"; "
		i__=i_[0].split("=")
		i_1={}
		for i2 in i_[1:]:
			i2_=i2.split("=",1)
			if(len(i2_)==2):
				i_1[i2_[0]]=i2_[1]
			else:
				i_1[i2_[0]]=""
		
		响应url_=parse.urlparse(响应.geturl())
		try:
			i_1["domain"]
			if(i_1["domain"][0]!="."):
				i_1["domain"]="."+i_1["domain"]
		except:
			i_1["domain"]=响应url_.hostname
		try:
			i_1["expires"]
		except:
			i_1["expires"]=""
		try:
			i_1["path"]
		except:
			i_1["path"]="/"
		
		响应头_cookie_整理[i__[0]]=[i__[1],i_1["domain"],i_1["path"],i_1["expires"]]
	
	响应头_cookie_字符串=响应头_cookie_字符串[0:-2]

	原始数据=响应.read()
	if 转换=='raw':
		数据=原始数据
	else:
		原始数据=解gzip(原始数据)
		if 转换=='str':
			数据=原始数据.decode(json.detect_encoding(原始数据), 'surrogatepass')
		elif 转换=='json':
			数据=json.loads(原始数据)
		elif 转换=='bytes':
			数据=原始数据
	
	return (响应.geturl(),响应.getcode(),响应头_原始,响应头_整理,响应头_cookie_字符串,响应头_cookie_整理,数据)
	

def 解gzip(数据):
	'''
若为gzip数据,则解压
'''
	if(数据[:2]==b'\x1f\x8b'):
		return gzip.decompress(数据)
	return 数据

