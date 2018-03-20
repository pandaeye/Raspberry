#coding:utf-8
import urllib
import time
from xml.dom.minidom import parseString
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def TestUrlOpen():
	page = urllib.urlopen("http://ws.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName=59493")#深圳
	lines = page.readlines()
	page.close()
	document = ""
	for line in lines :
		document = document + line
	dom =parseString(document)
	strings = dom.getElementsByTagName("string")
	sBroadcast=time.strftime('%m月%d日%H点%M分',time.localtime(time.time()))
	#sBroadcast=strings[1].childNodes[0].data+sBroadcast
	sWeather=strings[10].childNodes[0].data
	nTemperatureIndex1=sWeather.find("气温")
	nTemperatureIndex2=sWeather.find("℃")
	sTemperature=sWeather[nTemperatureIndex1:nTemperatureIndex2]+'度'

	nWindIndex1=sWeather.find("风力")
	sWind=sWeather[nWindIndex1:]
	nWindIndex2=sWind.find("；")
	sWind=sWind[:nWindIndex2]

	nHumidityIndex1=sWeather.find("湿度")
	nHumidityIndex2=sWeather.find("%")
	sHumidity=sWeather[nHumidityIndex1:nHumidityIndex2]

	nUVIndex1=sWeather.find("紫外线强度")
	sUV=sWeather[nUVIndex1:]
	nUVIndex2=sUV.find("空气质量")
	sUV=sUV[:nUVIndex2]

	nPMIndex1=sWeather.find("空气质量")
	sPM=sWeather[nPMIndex1:]

	sWeather="  "+sTemperature+"  "+sWind+"  "+sHumidity+"  "+sPM
	sBroadcast=sBroadcast+sWeather
	sNum="0123456789"
	i=0
	while True:
		c1=sBroadcast[i]
		if c1 in sNum:
			c2 =sBroadcast[i+1]
			if c2 in sNum:
				if c1=='0' and c2=='0':
					sBroadcast=sBroadcast[:i]+sBroadcast[i+1:]
				elif c1=='1' and c2=='0':
					sBroadcast=sBroadcast[:i]+'十'+sBroadcast[i+2:]
				elif c1=='1' and c2!='0':
					sBroadcast=sBroadcast[:i]+'十'+sBroadcast[i+1:]
					i+=1
				elif c1!='1' and c1!='0' and c2!='0':
					sBroadcast=sBroadcast[:i+1]+'十'+sBroadcast[i+1:]
					i+=1
				elif c1!='1' and c1!='0' and c2=='0':
					sBroadcast=sBroadcast[:i+1]+'十'+sBroadcast[i+2:]
				elif c1=='0' and c2!='0':
					sBroadcast=sBroadcast[:i]+sBroadcast[i+1:]
		i+=1
		if i>=len(sBroadcast):
			break;
	return sBroadcast
	#print sBroadcast
TestUrlOpen()