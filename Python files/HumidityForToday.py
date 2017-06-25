# folosim urllib pentru a lua codul html de pe pagina cu datele xml
# iar daca exista vreo eroare folosim urllib2
# folosim xml.etree.ElementTree pentru a interoga fisierul xml si a extrage datele
def RetData():
	import xml.etree.ElementTree as ET
	try:
		from urllib.request import urlopen
	except ImportError:
		from urllib2 import urlopen

#URL-ul paginii xml
	xml_url = "http://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_BUCUR-BAN_latest.xml"

# luam codul html din pagina si il stocam in memorie ca string (linia 23)
# din string, convertam in fisier xml                          (linia 24)
# gasim unde in xml exista campul <metDAta>                    (linia 25)
# in <metData> cautam <rh>                                     (linia 26)
# scriem in fisier valoarea campului                           (linia 28)

	url = urlopen(xml_url).read()
	xml = ET.fromstring(url)
	Node = xml.find('metData')
	Humidity = Node.find("rh").text

	return Humidity


