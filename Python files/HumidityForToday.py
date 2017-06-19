# folosim urllib pentru a lua codul html de pe pagina cu datele xml
# iar daca exista vreo eroare folosim urllib2
# folosim xml.etree.ElementTree pentru a interoga fisierul xml si a extrage datele

import xml.etree.ElementTree as ET
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

#URL-ul paginii xml
xml_url = "http://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_BUCUR-BAN_latest.xml"

# creeare si scrierea in fisier a datelor
file_out = open("weather_Humidity.txt", 'w')

# luam codul html din pagina si il stocam in memorie ca string (linia 16)
# din string, convertam in fisier xml                          (linia 17)
# gasim unde in xml exista campul <metDAta>                    (linia 18)
# in <metData> cautam <rh>                                     (linia 19)
# printam in fisier valoarea campului                          (linia 21)

url = urlopen(xml_url).read()
xml = ET.fromstring(url)
Node = xml.find('metData')
Humidity = Node.find("rh")

file_out.write(Humidity.text)


