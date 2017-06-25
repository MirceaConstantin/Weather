import xml.etree.ElementTree as ET 

try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen

xml_url = "http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/en/forecast_BUCUR-BAN_latest.xml"

url = urlopen(xml_url).read()
xml = ET.fromstring(url)

weatherType = []
for wType in xml.findall('metData'):
	weatherType.append(wType.find('nn_shortText').text)

print(weatherType)