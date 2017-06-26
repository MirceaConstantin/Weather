def RetData():
	import xml.etree.ElementTree as ET
	try:
    	from urllib.request import urlopen
	except ImportError:
    	from urllib2 import urlopen 

#URL-ul paginii xml
	xml_url = "http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/en/forecast_BUCUR-BAN_latest.xml"

# creeare si scrierea in fisier a datelor
	file_out = open("weather_Sunrise_Sunset.txt", 'w+')

# luam codul html din pagina si il stocam in memorie ca string (linia 18)
# din string, convertam in fisier xml                          (linia 19)
	url = urlopen(xml_url).read()
	xml = ET.fromstring(url)

	Hours = []
	for Nodes in xml.findall('metData'):
    	sunrise = Nodes.find('sunrise')
    	sunset = Nodes.find('sunset')
    	Hours.append((sunrise.text, sunset.text))
    return Hours








