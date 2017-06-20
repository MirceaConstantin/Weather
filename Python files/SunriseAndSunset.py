# folosim urllib pentru a lua codul html de pe pagina cu datele xml 
# iar daca exista vreo eroare folosim urllib2
# folosim xml.etree.ElementTree pentru a interoga fisierul xml si a extrage datele
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

# pentru fiecare camp <metData> gasit, cauta <sunrise> si <sunset> si printeaza valorile 
# in fisierul "weather_Sunrise_Sunset.txt"
for Nodes in xml.findall('metData'):
    sunrise = Nodes.find('sunrise')
    file_out.write(sunrise.text + '\n')
    
    sunset = Nodes.find('sunset')
    file_out.write(sunset.text + '\n\n')










