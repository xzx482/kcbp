
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
