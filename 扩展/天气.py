import json
import time

from urllib import request

from flj import flj
from PyQt6.QtCore import QAbstractAnimation, QEasingCurve, QParallelAnimationGroup, QPoint, QPointF, QPropertyAnimation, QSequentialAnimationGroup, Qt, QThread, pyqtSignal
from PyQt6.QtGui import QBrush, QColor, QFont, QFontMetrics, QPainter, QPen, QPolygonF
from PyQt6.QtWidgets import QGraphicsOpacityEffect, QHBoxLayout, QLabel, QVBoxLayout, QWidget
from kcb_basic import 获取字体,缩放


class 天气获取t(QThread):
	trigger=pyqtSignal(dict)
	sxym=pyqtSignal()
	def __init__(s,parent):
		super().__init__()
		s.parent:天气组件=parent
	def 获取并发送(s):
		print('获取天气'+time.strftime('%H:%M:%S'))
		try:
			'''
			uo=request.urlopen('https://api.openweathermap.org/data/2.5/onecall?units=metric&lang=zh_cn&lat='+str(s.配置l['天气']['纬度'])+'&lon='+str(s.配置l['天气']['经度'])+'&appid='+s.配置l['天气']['key'],timeout=60)
			jl=json.load(uo)
			"""
			'''
			time.sleep(2)
			jl={'lat': 26.1718, 'lon': 118.1419, 'timezone': 'Asia/Shanghai', 'timezone_offset': 28800, 'current': {'dt': 1648995877, 'sunrise': 1648936606, 'sunset': 1648981475, 'temp': -233.3, 'feels_like': 11.29, 'pressure': 1026, 'humidity': 73, 'dew_point': 7.43, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 90, 'wind_gust': 1.04, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴+++', 'icon': '01n'}]}, 'minutely': [{'dt': 1648995900, 'precipitation': 0}, {'dt': 1648995960, 'precipitation': 28}, {'dt': 1648996020, 'precipitation': 0}, {'dt': 1648996080, 'precipitation': 0}, {'dt': 1648996140, 'precipitation': 0}, {'dt': 1648996200, 'precipitation': 0}, {'dt': 1648996260, 'precipitation': 0}, {'dt': 1648996320, 'precipitation': 0}, {'dt': 1648996380, 'precipitation': 0}, {'dt': 1648996440, 'precipitation': 0}, {'dt': 1648996500, 'precipitation': 0}, {'dt': 1648996560, 'precipitation': 0}, {'dt': 1648996620, 'precipitation': 0}, {'dt': 1648996680, 'precipitation': 0}, {'dt': 1648996740, 'precipitation': 0}, {'dt': 1648996800, 'precipitation': 0}, {'dt': 1648996860, 'precipitation': 0}, {'dt': 1648996920, 'precipitation': 0}, {'dt': 1648996980, 'precipitation': 0}, {'dt': 1648997040, 'precipitation': 0}, {'dt': 1648997100, 'precipitation': 0}, {'dt': 1648997160, 'precipitation': 0}, {'dt': 1648997220, 'precipitation': 0}, {'dt': 1648997280, 'precipitation': 0}, {'dt': 1648997340, 'precipitation': 0}, {'dt': 1648997400, 'precipitation': 0}, {'dt': 1648997460, 'precipitation': 0}, {'dt': 1648997520, 'precipitation': 0}, {'dt': 1648997580, 'precipitation': 0}, {'dt': 1648997640, 'precipitation': 0}, {'dt': 1648997700, 'precipitation': 0}, {'dt': 1648997760, 'precipitation': 0}, {'dt': 1648997820, 'precipitation': 0}, {'dt': 1648997880, 'precipitation': 0}, {'dt': 1648997940, 'precipitation': 0}, {'dt': 1648998000, 'precipitation': 0}, {'dt': 1648998060, 'precipitation': 0}, {'dt': 1648998120, 'precipitation': 0}, {'dt': 1648998180, 'precipitation': 0}, {'dt': 1648998240, 'precipitation': 0}, {'dt': 1648998300, 'precipitation': 0}, {'dt': 1648998360, 'precipitation': 0}, {'dt': 1648998420, 'precipitation': 0}, {'dt': 1648998480, 'precipitation': 0}, {'dt': 1648998540, 'precipitation': 0}, {'dt': 1648998600, 'precipitation': 0}, {'dt': 1648998660, 'precipitation': 0}, {'dt': 1648998720, 'precipitation': 0}, {'dt': 1648998780, 'precipitation': 0}, {'dt': 1648998840, 'precipitation': 0}, {'dt': 1648998900, 'precipitation': 0}, {'dt': 1648998960, 'precipitation': 0}, {'dt': 1648999020, 'precipitation': 0}, {'dt': 1648999080, 'precipitation': 0}, {'dt': 1648999140, 'precipitation': 0}, {'dt': 1648999200, 'precipitation': 0}, {'dt': 1648999260, 'precipitation': 0}, {'dt': 1648999320, 'precipitation': 0}, {'dt': 1648999380, 'precipitation': 0}, {'dt': 1648999440, 'precipitation': 0}, {'dt': 1648999500, 'precipitation': 0}], 'hourly': [{'dt': 1648994400, 'temp': 12.12, 'feels_like': 11.29, 'pressure': 1026, 'humidity': 73, 'dew_point': 7.43, 'uvi': 0.9, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.93, 'wind_deg': 90, 'wind_gust': 1.04, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0.9}, {'dt': 1648998000, 'temp': 11.99, 'feels_like': 11.18, 'pressure': 1026, 'humidity': 74, 'dew_point': 7.51, 'uvi': 0.9, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.68, 'wind_deg': 107, 'wind_gust': 1.57, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0.9}, {'dt': 1649001600, 'temp': 11.59, 'feels_like': 10.82, 'pressure': 1026, 'humidity': 77, 'dew_point': 7.7, 'uvi': 0.9, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 97, 'wind_gust': 1.23, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0.9}, {'dt': 1649005200, 'temp': 11.01, 'feels_like': 10.28, 'pressure': 1026, 'humidity': 81, 'dew_point': 7.88, 'uvi': 0.9, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.58, 'wind_deg': 101, 'wind_gust': 1.49, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0.9}, {'dt': 1649008800, 'temp': 10.19, 'feels_like': 9.46, 'pressure': 1026, 'humidity': 84, 'dew_point': 7.61, 'uvi': 0.9, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.15, 'wind_deg': 105, 'wind_gust': 1.17, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0.9}, {'dt': 1649012400, 'temp': 9.3, 'feels_like': 9.3, 'pressure': 1026, 'humidity': 87, 'dew_point': 5.43, 'uvi': 0.9, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 109, 'wind_gust': 1.18, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0.9}, {'dt': 1649016000, 'temp': 8.88, 'feels_like': 8.88, 'pressure': 1026, 'humidity': 87, 'dew_point': 5.08, 'uvi': 0.9, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.25, 'wind_deg': 104, 'wind_gust': 1.15, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0.9}, {'dt': 1649019600, 'temp': 8.48, 'feels_like': 8.48, 'pressure': 1027, 'humidity': 88, 'dew_point': 4.75, 'uvi': 0.9, 'clouds': 90, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 102, 'wind_gust': 1.16, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649023200, 'temp': 8.17, 'feels_like': 8.17, 'pressure': 1027, 'humidity': 88, 'dew_point': 4.48, 'uvi': 0.9, 'clouds': 90, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 100, 'wind_gust': 0.94, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649026800, 'temp': 9.91, 'feels_like': 9.91, 'pressure': 1028, 'humidity': 81, 'dew_point': 5.04, 'uvi': 0.49, 'clouds': 0, 'visibility': 10000, 'wind_speed': 0.9, 'wind_deg': 96, 'wind_gust': 1.33, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649030400, 'temp': 12.65, 'feels_like': 11.75, 'pressure': 1028, 'humidity': 68, 'dew_point': 5.21, 'uvi': 1.91, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.09, 'wind_deg': 78, 'wind_gust': 1.53, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649034000, 'temp': 15.04, 'feels_like': 14.11, 'pressure': 1027, 'humidity': 58, 'dew_point': 5.16, 'uvi': 4.35, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.18, 'wind_deg': 85, 'wind_gust': 1.83, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649037600, 'temp': 17.27, 'feels_like': 16.33, 'pressure': 1027, 'humidity': 49, 'dew_point': 4.98, 'uvi': 7.28, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.16, 'wind_deg': 71, 'wind_gust': 1.81, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649041200, 'temp': 19, 'feels_like': 18.1, 'pressure': 1026, 'humidity': 44, 'dew_point': 4.89, 'uvi': 9.73, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 61, 'wind_gust': 1.94, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649044800, 'temp': 20.39, 'feels_like': 19.53, 'pressure': 1026, 'humidity': 40, 'dew_point': 4.93, 'uvi': 10.79, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.33, 'wind_deg': 48, 'wind_gust': 1.77, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649048400, 'temp': 21.03, 'feels_like': 20.18, 'pressure': 1025, 'humidity': 38, 'dew_point': 4.82, 'uvi': 10.14, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.73, 'wind_deg': 45, 'wind_gust': 1.92, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649052000, 'temp': 21.35, 'feels_like': 20.53, 'pressure': 1023, 'humidity': 38, 'dew_point': 4.82, 'uvi': 7.99, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.85, 'wind_deg': 49, 'wind_gust': 2.02, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649055600, 'temp': 21.39, 'feels_like': 20.58, 'pressure': 1022, 'humidity': 38, 'dew_point': 4.96, 'uvi': 5.12, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.86, 'wind_deg': 52, 'wind_gust': 2.07, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649059200, 'temp': 20.94, 'feels_like': 20.11, 'pressure': 1022, 'humidity': 39, 'dew_point': 5.11, 'uvi': 2.46, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.87, 'wind_deg': 64, 'wind_gust': 2.28, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649062800, 'temp': 20.12, 'feels_like': 19.39, 'pressure': 1022, 'humidity': 46, 'dew_point': 6.64, 'uvi': 0.77, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.52, 'wind_deg': 74, 'wind_gust': 2.25, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649066400, 'temp': 17.14, 'feels_like': 16.45, 'pressure': 1022, 'humidity': 59, 'dew_point': 7.47, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.24, 'wind_deg': 98, 'wind_gust': 1.24, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649070000, 'temp': 14.79, 'feels_like': 13.97, 'pressure': 1023, 'humidity': 63, 'dew_point': 6.12, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.35, 'wind_deg': 120, 'wind_gust': 1.28, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649073600, 'temp': 13.83, 'feels_like': 12.99, 'pressure': 1024, 'humidity': 66, 'dew_point': 5.93, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.43, 'wind_deg': 118, 'wind_gust': 1.33, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649077200, 'temp': 12.99, 'feels_like': 12.17, 'pressure': 1025, 'humidity': 70, 'dew_point': 5.93, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.47, 'wind_deg': 111, 'wind_gust': 1.38, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649080800, 'temp': 12.22, 'feels_like': 11.43, 'pressure': 1026, 'humidity': 74, 'dew_point': 5.9, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.54, 'wind_deg': 111, 'wind_gust': 1.41, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649084400, 'temp': 11.49, 'feels_like': 10.68, 'pressure': 1026, 'humidity': 76, 'dew_point': 5.74, 'uvi': 0, 'clouds': 1, 'visibility': 10000, 'wind_speed': 1.44, 'wind_deg': 107, 'wind_gust': 1.33, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649088000, 'temp': 10.84, 'feels_like': 10.04, 'pressure': 1026, 'humidity': 79, 'dew_point': 5.54, 'uvi': 0, 'clouds': 1, 'visibility': 10000, 'wind_speed': 1.27, 'wind_deg': 98, 'wind_gust': 1.22, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649091600, 'temp': 10.23, 'feels_like': 9.4, 'pressure': 1026, 'humidity': 80, 'dew_point': 5.29, 'uvi': 0, 'clouds': 1, 'visibility': 10000, 'wind_speed': 1.26, 'wind_deg': 103, 'wind_gust': 1.2, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649095200, 'temp': 9.77, 'feels_like': 9.77, 'pressure': 1026, 'humidity': 82, 'dew_point': 5.05, 'uvi': 0, 'clouds': 1, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 100, 'wind_gust': 1.07, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649098800, 'temp': 9.38, 'feels_like': 9.38, 'pressure': 1026, 'humidity': 83, 'dew_point': 4.88, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.11, 'wind_deg': 103, 'wind_gust': 1.02, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649102400, 'temp': 9.02, 'feels_like': 9.02, 'pressure': 1026, 'humidity': 84, 'dew_point': 4.7, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 0.96, 'wind_deg': 107, 'wind_gust': 0.97, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649106000, 'temp': 8.77, 'feels_like': 8.77, 'pressure': 1026, 'humidity': 84, 'dew_point': 4.53, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1, 'wind_deg': 106, 'wind_gust': 0.95, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649109600, 'temp': 8.59, 'feels_like': 8.59, 'pressure': 1026, 'humidity': 84, 'dew_point': 4.34, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 0.89, 'wind_deg': 115, 'wind_gust': 0.86, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649113200, 'temp': 10.52, 'feels_like': 9.64, 'pressure': 1027, 'humidity': 77, 'dew_point': 4.92, 'uvi': 0.5, 'clouds': 0, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 131, 'wind_gust': 0.92, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649116800, 'temp': 13.62, 'feels_like': 12.71, 'pressure': 1026, 'humidity': 64, 'dew_point': 5.18, 'uvi': 1.96, 'clouds': 0, 'visibility': 10000, 'wind_speed': 0.55, 'wind_deg': 104, 'wind_gust': 0.69, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649120400, 'temp': 16.57, 'feels_like': 15.69, 'pressure': 1026, 'humidity': 54, 'dew_point': 5.6, 'uvi': 4.52, 'clouds': 0, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 81, 'wind_gust': 0.64, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649124000, 'temp': 19.25, 'feels_like': 18.46, 'pressure': 1025, 'humidity': 47, 'dew_point': 6.16, 'uvi': 7.54, 'clouds': 0, 'visibility': 10000, 'wind_speed': 0.46, 'wind_deg': 52, 'wind_gust': 0.5, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649127600, 'temp': 21.42, 'feels_like': 20.77, 'pressure': 1024, 'humidity': 44, 'dew_point': 7, 'uvi': 10.07, 'clouds': 0, 'visibility': 10000, 'wind_speed': 0.7, 'wind_deg': 15, 'wind_gust': 0.96, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649131200, 'temp': 22.93, 'feels_like': 22.38, 'pressure': 1023, 'humidity': 42, 'dew_point': 7.8, 'uvi': 11.18, 'clouds': 0, 'visibility': 10000, 'wind_speed': 0.66, 'wind_deg': 28, 'wind_gust': 1.04, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649134800, 'temp': 23.65, 'feels_like': 23.12, 'pressure': 1021, 'humidity': 40, 'dew_point': 7.82, 'uvi': 10.51, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.2, 'wind_deg': 353, 'wind_gust': 1.86, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649138400, 'temp': 23.9, 'feels_like': 23.36, 'pressure': 1020, 'humidity': 39, 'dew_point': 7.75, 'uvi': 8.28, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.32, 'wind_deg': 2, 'wind_gust': 1.97, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649142000, 'temp': 23.73, 'feels_like': 23.18, 'pressure': 1019, 'humidity': 39, 'dew_point': 7.65, 'uvi': 5.26, 'clouds': 0, 'visibility': 10000, 'wind_speed': 1.45, 'wind_deg': 4, 'wind_gust': 1.99, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649145600, 'temp': 23.15, 'feels_like': 22.59, 'pressure': 1019, 'humidity': 41, 'dew_point': 7.72, 'uvi': 2.53, 'clouds': 1, 'visibility': 10000, 'wind_speed': 1.71, 'wind_deg': 360, 'wind_gust': 2.22, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649149200, 'temp': 22.31, 'feels_like': 21.88, 'pressure': 1019, 'humidity': 49, 'dew_point': 9.57, 'uvi': 0.79, 'clouds': 2, 'visibility': 10000, 'wind_speed': 1.38, 'wind_deg': 16, 'wind_gust': 2, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649152800, 'temp': 19.42, 'feels_like': 19.01, 'pressure': 1019, 'humidity': 61, 'dew_point': 10.13, 'uvi': 0, 'clouds': 4, 'visibility': 10000, 'wind_speed': 1.14, 'wind_deg': 15, 'wind_gust': 1.17, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'pop': 0}, {'dt': 1649156400, 'temp': 17.41, 'feels_like': 16.88, 'pressure': 1020, 'humidity': 64, 'dew_point': 8.81, 'uvi': 0, 'clouds': 7, 'visibility': 10000, 'wind_speed': 0.85, 'wind_deg': 43, 'wind_gust': 0.91, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649160000, 'temp': 16.81, 'feels_like': 16.24, 'pressure': 1020, 'humidity': 65, 'dew_point': 8.57, 'uvi': 0, 'clouds': 8, 'visibility': 10000, 'wind_speed': 0.72, 'wind_deg': 72, 'wind_gust': 0.79, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01n'}], 'pop': 0}, {'dt': 1649163600, 'temp': 16.34, 'feels_like': 15.75, 'pressure': 1021, 'humidity': 66, 'dew_point': 8.46, 'uvi': 0, 'clouds': 22, 'visibility': 10000, 'wind_speed': 0.56, 'wind_deg': 93, 'wind_gust': 0.61, 'weather': [{'id': 801, 'main': 'Clouds', 'description': '晴，少云', 'icon': '02n'}], 'pop': 0}], 'daily': [{'dt': 1648958400, 'sunrise': 1648936606, 'sunset': 1648981475, 'moonrise': 1648940880, 'moonset': 1648988400, 'moon_phase': 0.06, 'temp': {'day': 19.23, 'min': 8.48, 'max': 20.46, 'night': 11.99, 'eve': 15.49, 'morn': 8.48}, 'feels_like': {'day': 18.33, 'night': 11.18, 'eve': 14.79, 'morn': 8.48}, 'pressure': 1025, 'humidity': 43, 'dew_point': 4.69, 'wind_speed': 2.35, 'wind_deg': 29, 'wind_gust': 3.82, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'clouds': 0, 'pop': 0, 'uvi': 10.42}, {'dt': 1649044800, 'sunrise': 1649022942, 'sunset': 1649067902, 'moonrise': 1649029320, 'moonset': 1649078160, 'moon_phase': 0.09, 'temp': {'day': 20.39, 'min': 8.17, 'max': 21.39, 'night': 11.49, 'eve': 17.14, 'morn': 8.17}, 'feels_like': {'day': 19.53, 'night': 10.68, 'eve': 16.45, 'morn': 8.17}, 'pressure': 1026, 'humidity': 40, 'dew_point': 4.93, 'wind_speed': 1.87, 'wind_deg': 64, 'wind_gust': 2.28, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'clouds': 0, 'pop': 0, 'uvi': 10.79}, {'dt': 1649131200, 'sunrise': 1649109279, 'sunset': 1649154330, 'moonrise': 1649117880, 'moonset': 1649167860, 'moon_phase': 0.13, 'temp': {'day': 22.93, 'min': 8.59, 'max': 23.9, 'night': 15.67, 'eve': 19.42, 'morn': 8.59}, 'feels_like': {'day': 22.38, 'night': 15.09, 'eve': 19.01, 'morn': 8.59}, 'pressure': 1023, 'humidity': 42, 'dew_point': 7.8, 'wind_speed': 1.71, 'wind_deg': 360, 'wind_gust': 2.22, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'clouds': 0, 'pop': 0, 'uvi': 11.18}, {'dt': 1649217600, 'sunrise': 1649195615, 'sunset': 1649240758, 'moonrise': 1649206620, 'moonset': 1649257620, 'moon_phase': 0.16, 'temp': {'day': 24.25, 'min': 14.83, 'max': 24.59, 'night': 17.51, 'eve': 22.07, 'morn': 14.83}, 'feels_like': {'day': 24.01, 'night': 17.33, 'eve': 22, 'morn': 14.46}, 'pressure': 1020, 'humidity': 49, 'dew_point': 11.42, 'wind_speed': 1.86, 'wind_deg': 7, 'wind_gust': 2.27, 'weather': [{'id': 801, 'main': 'Clouds', 'description': '晴，少云', 'icon': '02d'}], 'clouds': 22, 'pop': 0, 'uvi': 10.93}, {'dt': 1649304000, 'sunrise': 1649281953, 'sunset': 1649327186, 'moonrise': 1649295660, 'moonset': 0, 'moon_phase': 0.19, 'temp': {'day': 24.1, 'min': 14.59, 'max': 25.7, 'night': 17.31, 'eve': 24.56, 'morn': 14.59}, 'feels_like': {'day': 23.9, 'night': 16.98, 'eve': 24.38, 'morn': 14.43}, 'pressure': 1020, 'humidity': 51, 'dew_point': 11.7, 'wind_speed': 2.25, 'wind_deg': 22, 'wind_gust': 3.17, 'weather': [{'id': 802, 'main': 'Clouds', 'description': '多云', 'icon': '03d'}], 'clouds': 28, 'pop': 0, 'uvi': 10.17}, {'dt': 1649390400, 'sunrise': 1649368290, 'sunset': 1649413614, 'moonrise': 1649384940, 'moonset': 1649347260, 'moon_phase': 0.22, 'temp': {'day': 24.11, 'min': 14.12, 'max': 25.93, 'night': 15, 'eve': 23.35, 'morn': 14.12}, 'feels_like': {'day': 23.54, 'night': 14.17, 'eve': 22.81, 'morn': 13.7}, 'pressure': 1018, 'humidity': 37, 'dew_point': 7.1, 'wind_speed': 2.71, 'wind_deg': 91, 'wind_gust': 4.92, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'clouds': 0, 'pop': 0, 'uvi': 11}, {'dt': 1649476800, 'sunrise': 1649454628, 'sunset': 1649500042, 'moonrise': 1649474460, 'moonset': 1649436720, 'moon_phase': 0.25, 'temp': {'day': 24.72, 'min': 13, 'max': 27.8, 'night': 17.83, 'eve': 26.16, 'morn': 13}, 'feels_like': {'day': 24.53, 'night': 17.76, 'eve': 26.16, 'morn': 12.39}, 'pressure': 1016, 'humidity': 49, 'dew_point': 11.73, 'wind_speed': 1.29, 'wind_deg': 115, 'wind_gust': 1.31, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'clouds': 1, 'pop': 0, 'uvi': 11}, {'dt': 1649563200, 'sunrise': 1649540967, 'sunset': 1649586471, 'moonrise': 1649564160, 'moonset': 1649526060, 'moon_phase': 0.28, 'temp': {'day': 27.37, 'min': 15.59, 'max': 30.48, 'night': 22.01, 'eve': 28.09, 'morn': 15.59}, 'feels_like': {'day': 27.78, 'night': 22.17, 'eve': 28.64, 'morn': 15.69}, 'pressure': 1015, 'humidity': 50, 'dew_point': 14.41, 'wind_speed': 1.2, 'wind_deg': 114, 'wind_gust': 1.5, 'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'}], 'clouds': 9, 'pop': 0, 'uvi': 11}]}
			#"""
			s.trigger.emit(jl)
			return True
		except BaseException as e:
			print('更新天气失败,'+str(e))
			return False
	def run(s):
		s.配置l=s.parent.配置l
		while 1:
			if s.获取并发送():
				break
			else:
				time.sleep(10)
		time.sleep(120)
		s.sxym.emit()
		while 1:
			if s.parent.预更新 or s.parent.显示状态:
				if s.parent.预更新:
					s.parent.预更新=False
				s.获取并发送()
				time.sleep(180)
			else:
				time.sleep(30)

天气cl=flj('天气c.json')

def 天气_c(w):
	for i in w:
		i_=str(i['id'])
		if i_ not in 天气cl.d:
			天气cl[i_]=i['description']


def 格式化百分比(x:float)->str:
	if x>100:
		raise
	elif x==0:
		return '1'
	elif x==100:
		return '99'
	else:
		return str(round(x))+''


class 每分钟折线图表组件(QWidget):
	def __init__(s):
		super().__init__()
		s.完全更新大小()

	def 完全更新大小(s):
		s.setMinimumHeight(缩放(100))
		s.保留宽度=缩放(20)
		s.刻度宽=缩放(4)
		s.箭头宽=缩放(5)
		s.字体=获取字体(14)
		s.fm=QFontMetrics(s.字体)
		s.点集:list[tuple[int,int]]=[]
		s.最大y=0
		s.x_起始=0
		s.x_终止=0
		
		s.内坐标x=s.保留宽度*2
		s.内坐标y=s.保留宽度

		s.更新大小()
	
	def 更新大小(s):
		s.高度=s.height()
		s.宽度=s.width()
		s.高内标x=s.宽度-s.内坐标x-s.保留宽度
		s.高内标y=s.高度-s.内坐标y-s.保留宽度


	def 内坐标xf(s,x):
		return x*s.高内标x+s.内坐标x


	def 内坐标yf(s,y):
		return (1-y)*s.高内标y+s.内坐标y

	def 内坐标(s,x,y)->QPointF:
		return QPointF(s.内坐标xf(x),s.内坐标yf(y))
		

	def paintEvent(s,a0)->None:
		s.更新大小()

		坐标0=s.内坐标(0,0)
		x0,y0=坐标0.x(),坐标0.y()
		坐标1=s.内坐标(1,1)
		x1,y1=坐标1.x(),坐标1.y()

		箭宽=s.箭头宽
		y_=s.最大y
	#获取数量级
		数量级=0
		加数=1 if y_>5 else -1
		乘数=0.1 if 加数==1 else 10
		while not (1<=y_<10):
			y_*=乘数
			数量级+=加数

			if 加数==1 and y_<1:
				raise
			if 加数==-1 and y_>10:
				raise
		
		最大y列表=[10,5,4,2]
		for i in 最大y列表:
			if i>=y_:
				最大y=i
			else:
				break
		
		最大y_=最大y*10**数量级

		if 数量级==1:
			最大y*=10
			最大y_=最大y
			数量级=0

		painter=QPainter(s)
		#painter.setRenderHint(QPainter.RenderHint.Antialiasing,True)
		红色=QColor(200,0,0)
		绿色=QColor(0,255,0)
		白色=QColor(255,255,255)
		颜色1=QColor(43, 162, 255, 128)
		白笔=QPen(白色,1)
		painter.setFont(s.字体)
		字体度量=s.fm
		半字体高度=字体度量.height()//2

	##绘制边界
	#	painter.setBrush(QBrush(QColor(128,128,128)))
	#	painter.drawRect(0,0,s.宽度,s.高度)




	#绘制折线
		x跨度=s.x_终止-s.x_起始
		painter.setPen(Qt.PenStyle.NoPen)
		painter.setBrush(QBrush(颜色1))
		旧点=None
		点集=[]
		for i in s.点集:
			点=s.内坐标((i[0]-s.x_起始)/x跨度,i[1]/最大y_)
			点集.append(点)
			if 旧点:
				#不能同时画线和多边形,否则会导致有竖线
				#painter.drawLine(点,旧点)
				#填充折线下方区域
				painter.drawPolygon(QPolygonF([旧点,点,QPointF(点.x(),y0),QPointF(旧点.x(),y0)]))
			旧点=点
		
		#painter.setPen(QPen(QColor(43, 162, 255),1))
		painter.setPen(白笔)
		for i in range(len(点集)):
			if i:
				painter.drawLine(点集[i],点集[i-1])




		painter.setPen(白笔)
		x轴尾=x1+箭宽*2
		y轴尾=y1-箭宽*2#qt坐标系的y轴是反的
		原点=QPointF(x0,y0)
		x轴尾点=QPointF(x轴尾,y0)
		y轴尾点=QPointF(x0,y轴尾)
	#绘制坐标轴
		painter.drawLine(原点,x轴尾点)#x轴
		painter.drawLine(原点,y轴尾点)#y轴
	#绘制坐标轴末尾的箭头
		#x轴
		painter.drawLine(x轴尾点,QPointF(x轴尾-箭宽,y0-箭宽))
		painter.drawLine(x轴尾点,QPointF(x轴尾-箭宽,y0+箭宽))
		#y轴
		painter.drawLine(y轴尾点,QPointF(x0-箭宽,y轴尾+箭宽))
		painter.drawLine(y轴尾点,QPointF(x0+箭宽,y轴尾+箭宽))
		#
		等分x数量=10
		等分y数量=4
		
		等分最大y=最大y/等分y数量
		i等分最大y=int(等分最大y)
		if 等分最大y==i等分最大y:
			等分最大y=i等分最大y

	#绘制坐标轴刻度
		#painter.setPen(QPen(QColor(0,0,0),1))
		等分x值=x跨度/等分x数量
		刻度宽_=y0-s.刻度宽
		for i in range(0,等分x数量):#横坐标,x
			x=s.内坐标xf(i/等分x数量)
			painter.drawLine(QPointF(x,y0),QPointF(x,刻度宽_))

			t=i*等分x值+s.x_起始
			文字=time.strftime('%H:%M',time.localtime(t))
			文字宽度=字体度量.horizontalAdvance(文字)
			painter.drawText(QPointF(x-文字宽度//2,y0+半字体高度*2),文字)
		
		刻度宽_=x0+s.刻度宽
		for i in range(1,等分y数量+1):#纵坐标,y
			y=s.内坐标yf(i/等分y数量)
			painter.drawLine(QPointF(x0,y),QPointF(刻度宽_,y))

			文字=str(round(i*等分最大y,1))
			文字宽度=字体度量.horizontalAdvance(文字)
			painter.drawText(QPointF(x0-文字宽度,y+半字体高度),文字)

	#绘制x轴单位
		文字='时间'
		文字宽度=字体度量.horizontalAdvance(文字)
		painter.drawText(QPointF(x1-文字宽度-箭宽,y0+半字体高度*2),文字)
	#绘制y轴单位
		位置=x0+箭宽
		文字='降水量('
		文字宽度=字体度量.horizontalAdvance(文字)
		painter.drawText(QPointF(位置,半字体高度*2),文字)
		位置+=文字宽度
		if 数量级:
			文字='10^'+str(数量级)
			文字宽度=字体度量.horizontalAdvance(文字)
			painter.setPen(QPen(红色 if 数量级>0 else 绿色))
			painter.drawText(QPointF(位置,半字体高度*2),文字)
			painter.setPen(白笔)
			位置+=文字宽度
		文字='mm)'
		painter.drawText(QPointF(位置,半字体高度*2),文字)


		painter.end()






class 单天气组件(QVBoxLayout):
	def __init__(s,数量=3):
		super().__init__()
		s.setSpacing(缩放(1))

		s.labels=[QLabel()for i in range(数量)]
		for i in s.labels:
			i.setFont(获取字体(16))
			i.setStyleSheet('color:#ffffff')
			s.addWidget(i)
			i.setAlignment(Qt.AlignmentFlag.AlignCenter)
			'''
		s.labels[0].setFont(获取字体(18,QFont.Weight.Bold))
		s.labels[1].setFont(获取字体(20))
		s.labels[2].setFont(获取字体(20,QFont.Weight.Bold))
		'''
		s.labels[0].setMinimumWidth(缩放(60))

	def 设置内容(s,*a):
		for i in range(len(a)):
			s.labels[i].setText(str(a[i]))


class 天气组件(QWidget):
	gxtq_signal=pyqtSignal(dict)
	def __init__(s, parent=None):
		super().__init__(parent)


		s.天气j={}

		s.初始=True
		s.预更新=False
		s.显示状态=False
		s.淡化属性=QGraphicsOpacityEffect()
		s.淡化属性.setOpacity(1)
		s.setGraphicsEffect(s.淡化属性)

		#'''
		s.初入动画=QPropertyAnimation(s.淡化属性,b'opacity')
		s.初入动画.setDuration(1000)
		s.初入动画.setStartValue(0.01)
		s.初入动画.setEndValue(1)
		s.初入动画.setEasingCurve(QEasingCurve.Type.InCubic)
		#以下问题使用下面的方法
		#   QPainter::begin: A paint device can only be painted by one painter at a time.
		#   QPainter::translate: Painter not active
		#参考: https://forum.qt.io/topic/130718/qt-animation-a-paint-device-can-only-be-painted-by-one-painter-at-a-time/4
		s.初入动画.finished.connect(lambda:(s.setGraphicsEffect(None),s.p.刷新淡化值()))


		#s.初入动画.start()
		s.初入动画.finished.connect(s.初入动画.deleteLater)
		#'''




		s.获取t=天气获取t(s)
		s.获取t.trigger.connect(s.gxtq)

		s.setFont(获取字体(18,QFont.Weight.Bold))

		s.根纵=QVBoxLayout()
		s.根纵.setContentsMargins(0,0,0,0)
		s.根纵.setSpacing(0)
		s.setLayout(s.根纵)

		s.当前信息widget=QWidget()
		s.当前信息hbox=QHBoxLayout()
		s.当前信息hbox.setContentsMargins(0,0,0,0)
		s.当前信息widget.setLayout(s.当前信息hbox)
		s.当前信息hbox.setSpacing(缩放(5))

		'''
		s.每分钟信息widget=QWidget()
		s.每分钟信息vbox=QVBoxLayout()
		s.每分钟信息vbox.setSpacing(缩放(12))
		s.每分钟信息vbox.addSpacing(缩放(6))
		s.每分钟信息hbox1=QHBoxLayout()
		s.每分钟信息hbox2=QHBoxLayout()
		s.每分钟信息vbox.addLayout(s.每分钟信息hbox1)
		s.每分钟信息vbox.addLayout(s.每分钟信息hbox2)
		s.每分钟信息widget.setLayout(s.每分钟信息vbox)
		s.每分钟信息hbox1.setSpacing(缩放(1))
		s.每分钟信息hbox2.setSpacing(缩放(1))
		s.每分钟信息l1=[]
		s.每分钟信息l2=[]
		'''
		s.每分钟信息widget=每分钟折线图表组件()

		s.每小时信息widget=QWidget()
		s.每小时信息vbox=QVBoxLayout()
		s.每小时信息vbox.setSpacing(缩放(10))
		#s.每小时信息vbox.addSpacing(缩放(6))
		s.每小时信息hbox1=QHBoxLayout()
		s.每小时信息hbox2=QHBoxLayout()
		s.每小时信息hbox3=QHBoxLayout()
		s.每小时信息vbox.addLayout(s.每小时信息hbox1)
		s.每小时信息vbox.addLayout(s.每小时信息hbox2)
		s.每小时信息vbox.addLayout(s.每小时信息hbox3)
		s.每小时信息widget.setLayout(s.每小时信息vbox)
		s.每小时信息hbox1.setSpacing(缩放(4))
		s.每小时信息hbox2.setSpacing(缩放(4))
		s.每小时信息hbox3.setSpacing(缩放(4))
		s.每小时信息l1=[]
		s.每小时信息l2=[]
		s.每小时信息l3=[]
		
		s.每天信息widget=QWidget()
		s.每天信息vbox=QVBoxLayout()
		#s.每天信息vbox.setSpacing(缩放(10))
		#s.每天信息vbox.addSpacing()
		s.每天信息hbox=QHBoxLayout()
		s.每天信息vbox.addLayout(s.每天信息hbox)
		s.每天信息widget.setLayout(s.每天信息vbox)
		s.每天信息hbox.setSpacing(0)
		s.每天信息l=[]

		
		s.根纵.addWidget(s.当前信息widget)
		s.根纵.addWidget(s.每天信息widget)
		s.根纵.addWidget(s.每分钟信息widget)
		s.根纵.addWidget(s.每小时信息widget)
		s.根纵.addStretch(1)


		#(s.每分钟信息hbox,s.每分钟信息l,25,2),
		for i in (
			#(s.每分钟信息hbox1,s.每分钟信息l1,15,2),(s.每分钟信息hbox2,s.每分钟信息l2,15,2),
			(s.每小时信息hbox1,s.每小时信息l1,8,5),(s.每小时信息hbox2,s.每小时信息l2,8,5),(s.每小时信息hbox3,s.每小时信息l3,8,5),
			(s.每天信息hbox,s.每天信息l,8,5)
		):
			i[0].setSpacing(缩放(10))
			for i2 in range(i[2]+1):
				i_=单天气组件(i[3])

				#if i[3]==2:
				#	i_.labels[0].setMinimumWidth(缩放(40))

				i[0].addLayout(i_)
				i[1].append(i_)

		#s.每分钟信息l1.pop(0).设置内容('时间(分)','降水量(毫米)')
		#s.每分钟信息l2.pop(0).设置内容('时间(分)','降水量(毫米)')
		#s.每分钟信息l=s.每分钟信息l1+s.每分钟信息l2
		s.每小时信息l1.pop(0).设置内容('时间(时)','天气','云量(%) 降水概率(%)','湿度(%)','温度(°C)')
		s.每小时信息l2.pop(0).设置内容('时间(时)','天气','云量(%) 降水概率(%)','湿度(%)','温度(°C)')
		s.每小时信息l3.pop(0).设置内容('时间(时)','天气','云量(%) 降水概率(%)','湿度(%)','温度(°C)')
		s.每小时信息l=s.每小时信息l1+s.每小时信息l2+s.每小时信息l3
		s.每天信息l.pop(0).设置内容('时间(天)','天气','云量(%) 降水概率(%)','湿度(%)','最值温度(°C)')



		s.当前信息hbox.addSpacing(缩放(70))
		s.当前信息=QLabel()
		s.当前信息.setFont(获取字体(18,QFont.Weight.Bold))
		s.当前信息hbox.addWidget(s.当前信息)

		s.当前信息hbox.addSpacing(缩放(16))
		当前信息_更新时间0=QLabel('更新于')
		当前信息_更新时间0.setFont(获取字体(14))
		s.当前信息hbox.addWidget(当前信息_更新时间0)
		s.当前信息_更新时间=QLabel()
		s.当前信息_更新时间.setFont(获取字体(14))
		s.当前信息hbox.addWidget(s.当前信息_更新时间)



		s.当前信息hbox.addStretch(1)
		#s.每分钟信息hbox1.addStretch(1)
		#s.每分钟信息hbox2.addStretch(1)
		s.每小时信息hbox1.addStretch(1)
		s.每小时信息hbox2.addStretch(1)
		s.每小时信息hbox3.addStretch(1)
		s.每天信息hbox.addStretch(1)



		s.setVisible(False)

		#s.gxtq_signal.connect(lambda:print('gxtq_signal'))

		


	
	def gxtq(s,*a):
		s.更新天气(*a)
	def 更新天气(s,天气j):
		s.天气j=天气j
		s.gxtq_signal.emit(s.天气j)

		当前天气_=天气j['current']

		if 'alerts' in 天气j:
			print('alerts '+天气j['alerts'])

		天气_c(当前天气_['weather'])

		s.当前信息_更新时间.setText(time.strftime("%H:%M:%S",time.localtime(当前天气_['dt'])))
		#s.当前信息_天气.setText(当前天气_['weather'][0]['description'])

		当前信息s=''

		当前信息s+=天气cl[ str(当前天气_['weather'][0]['id']) ] + '   '
		当前信息s+=str(当前天气_['temp'])+'℃   '
		当前信息s+='湿度'+str(当前天气_['humidity'])+'%   '

		风速_=''
		风向=当前天气_['wind_deg']
		if 30<风向<150:
			风速_+='东'
		elif 210<风向<330:
			风速_+='西'

		if 风向<60 or 300<风向:
			风速_+='北'
		elif 120<风向<240:
			风速_+='南'

		风速_+='风 '+str(当前天气_['wind_speed'])+'米/秒'
		当前信息s+=风速_
		s.当前信息.setText(当前信息s)

		#'''
		if 'minutely' in 天气j:
			每分钟天气_=天气j['minutely']
			l每分钟天气_=len(每分钟天气_)
			有信息=False
			点集=s.每分钟信息widget.点集
			点集.clear()
			s.每分钟信息widget.x_起始=每分钟天气_[0]['dt']
			s.每分钟信息widget.x_终止=每分钟天气_[-1]['dt']
			最大y=0
			for i in range(l每分钟天气_):
				i3=每分钟天气_[i]
				y=i3['precipitation']
				点集.append((i3['dt'],y))
				if y>最大y:
					最大y=y
				if y:
					有信息=True
				
			s.每分钟信息widget.最大y=最大y
						
			
			if 有信息:
				s.每分钟信息widget.setVisible(True)
				s.每分钟信息widget.update()
			else:
				s.每分钟信息widget.setVisible(False)
		else:
			s.每分钟信息widget.setVisible(False)

		#'''	
		if 'hourly' in 天气j:
			每小时天气_=天气j['hourly']
			for i in 每小时天气_:
				天气_c(i['weather'])
			i2=1
			for i in range(len(s.每小时信息l)):
				if len(每小时天气_)>i2:
					i3=每小时天气_[i2]
					s.每小时信息l[i].设置内容(str(time.localtime(i3['dt']).tm_hour)+'时', 天气cl[ str(i3['weather'][0]['id']) ] ,格式化百分比(i3['clouds'])+' '+格式化百分比(i3['pop']*100),格式化百分比(i3['humidity']),i3['temp'])
					i2+=1
				else:
					break
				
			s.每小时信息widget.setVisible(True)
		else:
			s.每小时信息widget.setVisible(False)

		if 'daily' in 天气j:
			每天天气_=天气j['daily']
			for i in 每天天气_:
				天气_c(i['weather'])
			i2=0
			for i in range(len(s.每天信息l)):
				if len(每天天气_)>i2:
					i3=每天天气_[i2]
					温度=i3['temp']
					s.每天信息l[i].设置内容(str(time.localtime(i3['dt']).tm_mday)+'日', 天气cl[ str(i3['weather'][0]['id']) ] ,格式化百分比(i3['clouds'])+' '+格式化百分比(i3['pop']*100),格式化百分比(i3['humidity']),str(round(温度['min']))+'/'+str(round(温度['max'])))
					i2+=1
				else:
					break

			s.每天信息widget.setVisible(True)
		else:
			s.每天信息widget.setVisible(True)

		#s.adjustSize()
		s.ccxs()
		#s.xsztbh()
	def ccxs(s):
		if s.初始:
			s.初始=False


			s.setVisible(True)
			s.淡化属性.setOpacity(0.01)
			s.初入动画.start()
			

	def xsztbh(s,显示状态):
		s.显示状态=显示状态

	def ks(s):
		if s.配置l['天气']['启用']:
			if s.配置l['天气']['key']:
				s.获取t.start()
			else:
				print('未配置天气')

	def ygx(s):
		s.预更新=True


def 配置(p,配置l):
	配置l.添加默认值(
		'天气',
		{
			'启用':True,
			'经度':0,
			'纬度':0,
			'key':''
		}
	)
	p.根纵_下横.addStretch(1)
	天气=天气组件()
	天气.配置l=配置l
	p.天气=天气
	天气.p=p
	p.根纵_上横_右纵_横.addWidget(天气)
	p.添加淡化组件(天气.当前信息widget)
	p.添加淡化组件(天气.每天信息widget,0.5)
	p.添加淡化组件(天气.每分钟信息widget)
	p.添加淡化组件(天气.每小时信息widget)
	p.zjxsztbh.connect(天气.xsztbh)
	p.ygx.connect(天气.ygx)
	p.ks.connect(天气.ks)


