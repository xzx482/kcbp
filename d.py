import win32gui

SW_HIDE=0

class 桌面窗口错误(BaseException):
	pass

#移植于 https://blog.csdn.net/Just_bg/article/details/116887990

def CBFindWorkerW1(hWnd,lp:list):
	if lp:
		return

	hShl=None
	hShl=win32gui.FindWindowEx(hWnd,None,"SHELLDLL_DefView",None)
	
	if hShl:
		strClass=win32gui.GetClassName(hWnd)
		if strClass=="WorkerW":
			lp.append(hWnd)
			return

	return True





def 准备桌面窗口():
	
	for i in range(2):
		#先检查是否已经有WorkerW窗口, 兼容其他动态壁纸软件
		hWork1=[]
		win32gui.EnumWindows(CBFindWorkerW1,hWork1)
		if hWork1:
			hWorkerW1=hWork1[0]
			break
		
		hWndShlMain=win32gui.FindWindow("Progman",None)
		win32gui.SendMessage(hWndShlMain, 0x052C, 0xD, 0)
		win32gui.SendMessage(hWndShlMain, 0x052C, 0xD, 1)
	else:
		raise 桌面窗口错误('找不到桌面窗口')

	
	if (not win32gui.IsWindow(hWorkerW1)):
		return None

	hWorker2=win32gui.FindWindowEx(None,hWorkerW1,"WorkerW",None)
	#win32gui.ShowWindow(hWorker2, SW_HIDE)
	
	#hWndShlMain=win32gui.FindWindow("Progman","Program Manager")
	#return hWndShlMain
	return hWorker2


'''
def 准备桌面窗口():
	hWndShlMain=int(input(':'),16)
	return hWndShlMain
#'''

def 嵌入(wid):
	hWndShlMain=准备桌面窗口()
	win32gui.SetParent(wid,hWndShlMain)
	return hWndShlMain

