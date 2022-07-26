
import time
from PyQt6.QtGui import QFont,QFontDatabase

缩放值=1366/1920

fontId=QFontDatabase.addApplicationFont("./HarmonyOS_Sans_Medium.ttf")
font=QFontDatabase.applicationFontFamilies(fontId)[0]

def 缩放f(值):
	return 值*缩放值

def 缩放(值):
	return int(值*缩放值)



def 获取字体(字号,*args,**kwargs)->QFont:
	f=QFont("黑体",*args,**kwargs)
	f.setPointSizeF(字号*缩放值)
	#f.setFamily(font)
	return f


def 获取秒(tl:time.struct_time)->int:
	return (tl.tm_hour*60+tl.tm_min)*60+tl.tm_sec



def 时间转文字(t):
	天,时=divmod(int(t),86400)
	时,分=divmod(时,3600)
	分,秒=divmod(分,60)
	s=''
	if 天:
		s+=str(天)+'天'
	if 时:
		s+=str(时)+'时'
	if 分:
		s+=str(分)+'分'
	if 秒:
		s+=str(秒)+'秒'
	elif s:
		s+='整'
	return s
