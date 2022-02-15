import win32gui

SW_HIDE=0

class 桌面窗口错误(BaseException):
	pass

#移植于 https://blog.csdn.net/Just_bg/article/details/116887990

def CBFindWorkerW1(hWnd,lp):
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


#获取透明的WorkerW1窗口句柄
def GetDesktopWorkerW1():
	hWork1=[]
	win32gui.EnumWindows(CBFindWorkerW1,hWork1)
	if not hWork1:
		raise 桌面窗口错误('找不到桌面窗口')
	return hWork1[0]

#获取WorkerW2句柄
def GetDesktopWorkerW2():
	hWorkerW1=GetDesktopWorkerW1()
	if (not win32gui.IsWindow(hWorkerW1)):
		return None

	hWorkWWnd=win32gui.FindWindowEx(None,hWorkerW1,"WorkerW",None)
	return hWorkWWnd


#发送0x052C,让windows在桌面图标后面生成一个workerw窗口
def MakeDesktopTransparent():
	hWndShlMain=win32gui.FindWindow("Progman",None)
	win32gui.SendMessage(hWndShlMain, 0x052C, 0xD, 0)
	win32gui.SendMessage(hWndShlMain, 0x052C, 0xD, 1)
	hWorkW=0
	hWorkW=GetDesktopWorkerW1()
	if hWorkW==0:
		print('找不到WorkW窗口, 再次尝试!')
		win32gui.SendMessage(hWndShlMain, 0x52c, 0, 0)
		hWorkW=GetDesktopWorkerW1()

	return hWorkW!=None

def 准备桌面窗口():
	MakeDesktopTransparent()
	hWorker2=GetDesktopWorkerW2()
	win32gui.ShowWindow(hWorker2, SW_HIDE)
	
	hWndShlMain=win32gui.FindWindow("Progman","Program Manager")
	return hWndShlMain


def 嵌入(wid):
	hWndShlMain=准备桌面窗口()
	win32gui.SetParent(wid,hWndShlMain)
	return hWndShlMain



'''
		try:
			##这些是网上复制的玄学, 一般是看不懂的
			#找到桌面, 发送 0x052C 使桌面图标与背景分离
			hwnd = win32gui.FindWindow("Progman", "Program Manager")
			win32gui.SendMessageTimeout(hwnd, 0x052C, 0, None, 0, 0x03E8)

			hwnd_WorkW=None
			计数=0
			while 1:
				计数+=1
				if 计数>100:
					raise 
				hwnd_WorkW = win32gui.FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
				# print("hwnd_WorkW: ",hwnd_WorkW)
				if not hwnd_WorkW:
					continue
				hView = win32gui.FindWindowEx(hwnd_WorkW, None, "SHELLDLL_DefView", None)
				# print('hwmd_hView: ', hView)
				if not hView:#这个WorkerW下没有shell
					continue
				h = win32gui.FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
				#while h:
				#	win32gui.SendMessage(h, 0x0010, 0, 0)  # WM_CLOSE
				#	h = win32gui.FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
				break
				
			s.hwnd=hwnd


		except:
				msg_box=QMessageBox()
				msg_box.setWindowTitle("错误")
				msg_box.setText("无法找到桌面窗口, 尝试重启可能会解决该问题")
				msg_box.setIcon(QMessageBox.Information)
				msg_box.addButton("确定", QMessageBox.YesRole)
				msg_box.exec()
				raise
		
		'''