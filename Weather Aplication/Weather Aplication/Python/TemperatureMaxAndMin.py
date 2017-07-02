def RetData():	
	import xml.etree.ElementTree as ET

	try:
		from urllib.request import urlopen
	except ImportError:
		from urllib2 import urlopen

	xml_url = "http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/en/forecast_BUCUR-BAN_latest.xml"

	url = urlopen(xml_url).read()
	xml = ET.fromstring(url)

	MinMaxTemp = []
	for temps in xml.findall('metData'):
		MinMaxTemp.append((temps.find('txsyn').text, temps.find('tnsyn').text))
	return MinMaxTemp
	
	