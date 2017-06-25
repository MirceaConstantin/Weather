def RetData():
	import xml.etree.ElementTree as ET 

	try:
		from urllib.request import urlopen
	except ImportError:
		from urllib2 import urlopen

	xml_url = "http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/en/forecast_BUCUR-BAN_latest.xml"

	url = urlopen(xml_url).read()
	xml = ET.fromstring(url)

	Date = []
	for day in xml.findall('metData'):
		Date.append((day.find('valid').text.split(' ')[0], day.find('valid_day').text.split(' ')[0]))
	
	return Date


