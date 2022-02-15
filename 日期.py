import sxtwl
import time


天干 = ("甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸")
地支 = ("子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥")
生肖 = ("鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪")
数字 = ("零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十")
节气 = ("", 
	"立春", "雨水", "惊蛰", "春分", "清明", "谷雨", 
	"立夏", "小满", "芒种", "夏至", "小暑", "大暑", 
	"立秋", "处暑", "白露", "秋分", "寒露", "霜降", 
	"立冬", "小雪", "大雪", "冬至", "小寒", "大寒"
)

农历_月=("", "正月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "腊月")
农历_日 = ("",
	"初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", 
	"十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", 
	"廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"
)
XiZ = ['摩羯', '水瓶', '双鱼', '白羊', '金牛', '双子', '巨蟹', '狮子', '处女', '天秤', '天蝎', '射手']
WeekCn = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]

class 日期():
	def __init__(s,t=None):
		tl=time.localtime(t)
		s.sx=sxtwl.fromSolar(tl.tm_year,tl.tm_mon,tl.tm_mday)
		s.农历_值=None
		s.公历_值=None
		s.更新()
	
	def 更新(s):
		s.农历()
		s.公历()


	def 农历(s):
		d=(s.sx.getLunarYear(),s.sx.getLunarMonth(),s.sx.getLunarDay())
		s.农历_值=d
		return d
	
	def 公历(s):
		d=(s.sx.getSolarYear(),s.sx.getSolarMonth(),s.sx.getSolarDay())
		s.公历_值=d
		return d

	def 节气(s):
		a=s.sx.getJieQi()
		if a!=225:
			return (a-2)%24
		else:
			return 0


	def 后(s,n):
		s.sx=s.sx.after(n)
		s.更新()

	def 前(s,n):
		s.sx=s.sx.before(n)
		s.更新()

	def 简日(s):
		农节=农历节日(s.sx)
		if 农节:
			return 农节
		elif s.sx.hasJieQi():
			return 节气[s.节气()]
		elif s.农历_值[2]==1:#每月的第一天显示月份
			return [s.农历_值[1]]
		else:
			return 农历_日[s.农历_值[2]]



def 农历节日(sx):
	#年=sx.getLunarYear()
	月=sx.getLunarMonth()
	#月天数=sxtwl.getLunarMonthNum(年,月)
	日=sx.getLunarDay()

	match 月:
		case 1:
			match 日:
				case 1:return ("春节",2)
				case 15:return ("元宵",0)
		case 2:
			match 日:
				case 2:return ("春龙",0)
		case 3:
			match 日:
				case 5:return ("上巳",0)
		case 5:
			match 日:
				case 5:return ("端午",1)
		case 7:
			match 日:
				case 7:return ("七夕",0)
				case 15:return ("中元",0)
		case 8:
			match 日:
				case 15:return ("中秋",1)
		case 9:
			match 日:
				case 9:return ("重阳",0)
		case 10:
			match 日:
				case 1:return ("寒衣",0)
				case 15:return ("下元",0)
		case 12:
			match 日:
				case 8:return ("腊八",0)
				#case 23:return ("小年",0)#北方
				case 24:return ("小年",0)#南方
			#除夕
			if sxtwl.getLunarMonthNum(sx.getLunarYear(),月)==日:
				return ("除夕",3)
	return None

def 公历节日(sx):
	年=sx.getSolarYear()
	月=sx.getSolarMonth()
	日=sx.getSolarDay()

	match 月:
		case 1:
			match 日:
				case 1:return ("元旦",1)
		case 2:
			match 日:
				case 14:return ("情人节",0)
		case 3:
			match 日:
				case 8:return ("妇女节",0)
				case 12:return ("植树节",0)
		case 4:
			match 日:
				case 1:return ("愚人节",0)
		case 5:
			match 日:
				case 1:return ("劳动节",3)
		case 6:
			match 日:
				case 1:return ("儿童节",0)
		case 7:
			match 日:
				case 1:return ("建党节",0)
		case 8:
			match 日:
				case 1:return ("建军节",0)
		case 9:
			match 日:
				case 10:return ("教师节",0)
		case 10:
			match 日:
				case 1:return ("国庆节",3)
		case 12:
			match 日:
				case 25:return ("圣诞节",0)

	
def 获取调休(y,m,d):
	
	


sx=日期()
sx.sx=sxtwl.fromSolar(2022,2,4)
sx.更新()
for i in range(20):
	print(*sx.公历(),sx.简日())
	sx.后(1)
