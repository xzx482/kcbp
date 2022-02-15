import time
from PyQt6.QtCore import QThread

'''
注意: QThread: Destroyed while thread is still running
	是因为传入的参数是局部变量, 局部变量在使用后即被清除, 若该变量已被清除, 但线程仍在运行, 则会出现此错误
'''

ids={}

class 线程(QThread):
	def __init__(s,t,f,*a1,**a2):
		super().__init__()
		s.id=time.perf_counter_ns()
		ids[s.id]=s
		s.f=f
		s.t=t
		s.a1=a1
		s.a2=a2
	def run(s):
		if s.t:
			s.msleep(int(s.t*1000))
		s.f(*s.a1,**s.a2)
		ids.pop(s.id)

	def 运行(s):
		s.start()


def 新线程(t,f,*a1,**a2):
	线程(t,f,*a1,**a2).运行()


def a(b,c,t):
	#print(b)
	time.sleep(t)
	#print(c)

if __name__=='__main__':
	#t1=新线程(print,2)
	#新延时(2,print,2)
	for i in range(10):
		新线程(0.001,a,1,0.001,3)
		#time.sleep(0.01)
	#新线程(0.001,a,1,0.001,3)


	time.sleep(10)
	print('a')