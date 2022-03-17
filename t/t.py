import time,os

记录时间_=['0','1']
def 记录时间():
	if not os.path.isdir('t'):
		os.mkdir('t')
	while 1:
		for i in range(2):
			tl=time.localtime()
			if (tl.tm_hour==11 and tl.tm_min>53)or(tl.tm_hour==12 and tl.tm_min<20)or(tl.tm_hour==17 and tl.tm_min>45)or(tl.tm_hour==18 and tl.tm_min<5)or(tl.tm_hour==22 and tl.tm_min>35)or(tl.tm_hour>=23):
				with open('t/'+记录时间_[i]+'_'+time.strftime('%Y%m%d_%H',tl)+'.txt','w') as f:
					f.seek(0)
					f.truncate(0)
					f.write(time.strftime('%Y%m%d_%H%M%S',tl))
					f.flush()
			time.sleep(30)

if __name__=='__main__':
    记录时间()