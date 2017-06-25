import xml.etree.ElementTree as ET

try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen

xml_url = "http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/en/forecast_BUCUR-BAN_latest.xml"

file_out = open("weather_Temperature.txt", 'w')

url = urlopen(xml_url).read()
xml = ET.fromstring(url)
temp = xml.find('metData')

print(temp.find('t').text)


