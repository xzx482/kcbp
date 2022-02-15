import json,time,os,_thread
'''
class 字典_(dict):
	def __init__(s,*a1,**a2):
		super().__init__(*a1,**a2)

	def __setitem__(s,k,v):
		s.d[k]=v
		s.a_()

	def __delitem__(s,k):
		del(s[k])
		s.a_()

class 列表_(list)
'''

class flj():
	'''
适用于使用json的对象保存的数据文件
像操作字典一样

'''
	def __init__(s,fn):
		'''
实例化
fn:文件名
'''
		s.fn=fn
		s.d={} #数据
		s.s=20 #写文件间隔
		s.t=[time.time(),False]#写文件 时间 和 锁
		s.需要写=False
		s.默认值={}
		s.fo=open(fn,"a+")

		try:
			s.读()
		except json.decoder.JSONDecodeError:
			s.写_(False)

		s.写线程_thread=_thread.start_new_thread(s.写线程,())

	def __getitem__(s,k):
		return s.d[k]
	
	def __setitem__(s,k,v):
		s.d[k]=v
		s.写()

	def __len__(s):
		return len(s.d)

	def __delitem__(s,k):
		del(s[k])
		s.写()
	
	def 设置默认值(s,d):
		s.默认值=d
		d.update(s.d)
		s.d=d

	def 读_(s):
		'''
读取文件并返回数据, 但不更改 s.d
建议使用 s.读 方法以同步 s.d
'''
		s.fo.seek(0)
		d=json.load(s.fo)
		return d
	
	def 读(s,更新方式=1):
		'''
读取文件并更新 s.d
'''
		d=s.读_()
		if 更新方式==0:#覆盖 变量中的数据
			s.d=d
		elif 更新方式==1:#重复项 取 变量中的数据
			d.update(s.d)
			s.d=d
		elif 更新方式==2:#重复项 取 文件中的数据
			s.d.update(d)

	def 写线程(s):
		'''
定期检查文件是否应该写入
'''
		while 1:
			time.sleep(s.s)
			if s.fo.closed:
				return
			if s.需要写:
				s.需要写=False
				s.写_(False)


	def 写_(s,读取=True):
		'''
将更改写入文件, 无论是否已间隔了 s.s 所设置的时间
适合在退出时保存数据
'''
		if 读取:
			s.读()
		s.fo.seek(0)
		s.fo.truncate(0)
		json.dump(s.d,s.fo,ensure_ascii=False,indent="\t",sort_keys=True)#格式化的json
		#json.dump(s.d,s.fo,ensure_ascii=False,separators=(',',':'))#压缩的json
		s.fo.flush()

	def 写(s):
		'''
将更改(不频繁地)写入文件
这是在更改了 s.d 之后应该执行的方法
不必担心文件被频繁地写入, 每次写入至少会间隔 s.s 所设置的时间
'''
		s.需要写=True
			
	def 写__(s):
		'''
写入数据, 在出错时将数据输出到控制台
'''
		try:
			s.写_()
			return True
		except:
			print('数据无法保存, 文件名"'+s.fn+'"')
			print('----数据_开始----')
			print(json.dumps(s.d,ensure_ascii=False,separators=(',',':')))
			print('----数据_结束----')
			return False

	def 重写(s,b=True):
		'''
清空数据
'''
		s.fo.close()
		if b:
			时间=time.time()
			备份名=s.fn+'.'+(time.strftime("%Y%m%d-%H%M%S",time.localtime(时间))+"."+str(时间).split(".")[1])+'.bak'
			os.rename(s.fn,备份名)
		open(s.fn,"w+").close()
		s.fo=open(s.fn,"a+")
		#s.fo.write('{}')
		s.写_(False)
	
	def 关闭(s):
		'''
关闭文件
'''
		s.写_()
		s.fo.close()


	#可将其作为一个字典使用
	#使用以下方法将字典操作重定向到 s.d

	def __eq__(s,v):
		s.d.__eq__(s,v)

	def __ge__(s,v):
		s.d.__ge__(s,v)

	def __gt__(s,v):
		s.d.__gt__(s,v)

	def __ior__(s,v):
		s.d.__ior__(s,v)

	def __le__(s,v):
		s.d.__le__(s,v)

	def __lt__(s,v):
		s.d.__lt__(s,v)

	def __ne__(s,v):
		s.d.__ne__(s,v)

	def __or__(s,v):
		s.d.__or__(s,v)

	def __iter__(s):
		iter(s.d)
	


if __name__=='__main__':
	dl=flj('hello_flj.json')
	dl['hello']='world'
	dl.写()

	#退出前记得保存
	dl.关闭()
	exit()
